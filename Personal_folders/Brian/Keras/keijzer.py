import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def setup_multi_gpus():
    """
    Setup multi GPU usage

    Example usage:
    model = Sequential()
    ...
    multi_model = multi_gpu_model(model, gpus=num_gpu)
    multi_model.fit()

    About memory usage:
    https://stackoverflow.com/questions/34199233/how-to-prevent-tensorflow-from-allocating-the-totality-of-a-gpu-memory
    """
    import tensorflow as tf
    from keras.utils.training_utils import multi_gpu_model
    from tensorflow.python.client import device_lib

    # IMPORTANT: Tells tf to not occupy a specific amount of memory
    from keras.backend.tensorflow_backend import set_session  
    config = tf.ConfigProto()  
    config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU  
    sess = tf.Session(config=config)  
    set_session(sess)  # set this TensorFlow session as the default session for Keras.

    
    # getting the number of GPUs 
    def get_available_gpus():
       local_device_protos = device_lib.list_local_devices()
       return [x.name for x in local_device_protos if x.device_type    == 'GPU']
    
    num_gpu = len(get_available_gpus())
    print('Amount of GPUs available: %s' % num_gpu)
    
    return num_gpu


def create_corr_matrix(df, dwelling_id, annot, size=(25,25)):
    """
    Pearson correlation coefficient matrix. 
    The Pearson correlation coefficient is a measure of the linear correlation between two variables.
    """
    plt.clf()
    
    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    if annot:
        fig, ax = plt.subplots(figsize=size)
    else:
        fig, ax = plt.subplots()

    fig = sns.heatmap(corr, mask=mask, square=False, cmap='RdYlGn', annot=annot, ax=ax, 
                cbar_kws={'label':'Pearson correlation coefficient [-]'})

    fig.set_title('Correlation matrix of dwelling ID: '+dwelling_id)
    fig.tick_params(axis='x', rotation=90)
    fig.tick_params(axis='y', rotation=0)

    fig = fig.get_figure()
    fig.tight_layout()
    fig.show()
    
    print('Saving heatmap')
    #fig.savefig('//datc//opschaler//EDA//Pearson_corr//' + dwelling_id + '.png', dpi=300)
    return fig


def reduce_memory(df):
    """
    Reduces memory footprint of the input dataframe.
    Changes float64 columns to float32 dtype.
    """
    columns = df.columns
    memory_before = df.memory_usage(deep=False).sum() / 2**30 # convert bytes to GB

    for column in tqdm(columns):
        if df[column].dtype == 'float64':
            df[column] = df[column].astype('float32')
        
    memory_after = df.memory_usage(deep=False).sum() / 2**30 # convert bytes to GB
    print('Memory uasge reduced from %.3f GB to %.3f GB' % (memory_before, memory_after))
    
    return df


def resample_df(df, sample_rate, combine_all_dwellings=False):
    """
    Resampled a (un)processed dataframe to the specified sample_rate.
    Input is a (un)processed df.
    Input df may also be multiple dwelling dfs combined.
    Sample rate must be a string. 
    For example '1H', '1D', '60s'.
    
    Combine all dwellings: resamples the df and ignores the fact that there are unique dwellings.
    
    TODO: add std to ePower, gasPower when combine_all_dwellings=False
    """
    df = df.copy()
    
    def resample_dwelling(df, sample_rate, dwelling_id):
        df = df.resample(sample_rate).mean() # resample to rest by mean
        df['dwelling'] = dwelling_id
        return df
        
                      
    resampled_dwellings = []
    
    if combine_all_dwellings: # Ignore dwelling_ids
        df = df.drop(['eMeter', 'eMeterReturn', 'eMeterLow', 'eMeterLowReturn', 'gasMeter'], axis=1) # Drop columns because they are meaningless when ignoring dwelling ids
        resampled_df = resample_dwelling(df, sample_rate, 'All dwellings')
        resampled_dwellings.append(resampled_df)
    else:
        dwellings = df['dwelling'].unique() # Get dwelling ids
        for dwelling_id in tqdm(dwellings):
            dwelling_df = df[df['dwelling'] == dwelling_id] # Get the data from only that dwelling_id
            resampled_dwelling = resample_dwelling(dwelling_df, sample_rate, dwelling_id)
            resampled_dwellings.append(resampled_dwelling)
    
    resampled_df = pd.concat(resampled_dwellings)
    
    return resampled_df


def abs_percentage_error(y_true, y_pred):
    import keras.backend as K
    """
    Returns the absolute value of the difference between y_true and y_pred (in percentage).
    For examples on losses see:
    https://github.com/keras-team/keras/blob/master/keras/losses.py
    """
    return (K.abs(y_true - y_pred) / K.abs(y_pred)) * 100


def create_timeseries_history(df, columns_to_lookback, n_lookback, dropnan=True):
    """
    df, pandas dataframe
    columns_to_lookback, the columns to gather historical data from
    n_lookback, amount of samples to look back for. 
    
    Example:
    df = dwelling_df['FF']
    columns_to_lookback = df.columns
    n_lookback = 3
    
    
    Output columns:
    FF, FF (t-1), FF (t-2), FF (t-3)
    
    Where FF (t-3) contains the FF value of 3 samples (indices) back.
    """
    n_lookback += 1 # +1 because iteration starts at 0.
    df = df.copy()
    
    for column in columns_to_lookback:
        if column == 'datetime':
            pass
        else:
            for dt in range(n_lookback):
                if dt == 0:
                    pass
                else: 
                    df[column+'(t-%s)' % dt ] = df[column].shift(dt)
    if dropnan:
        df = df.dropna()
        
    return df


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    columns = data.columns
    
    n_vars = 1 if type(data) is list else data.shape[1]
    dff = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(dff.shift(i))
        names += [('%s(t-%d)' % (columns[j], i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(dff.shift(-i))
        if i == 0:
            names += [('%s(t)' % (columns[j])) for j in range(n_vars)]
        else:
            names += [('%s(t+%d)' % (columns[j], i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg