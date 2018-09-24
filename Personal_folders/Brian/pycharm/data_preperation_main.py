"""
Shifr+F9 (Debug first, then plots will appear in SciView)
"""

import pandas as pd
import numpy as np
import glob
import time
import datetime

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
mpl.style.use('default')



def clean_datetime(df):
    """
    Input should be a df with a column called 'datetime'.
    This function checks wether a row in the df.datetime column can be parsed to a pandas datetime object,
    by trying pd.to_datetime() on it.
    If it fails it will replace that row with np.nan().
    Finally this function will return the df with the NaN rows dropped.
    It only drops the row if the datetime column contains a NaN.
    """
    for i in range(len(df)):
        try:
            pd.to_datetime(df.datetime[i])
        except ValueError:
            print('-----')
            print('ValueError at index = %s' % i)
            print(df.datetime[i])
            df.datetime = df.datetime.replace(df.datetime[i], np.nan)
    df = df.dropna(subset=['datetime'])
    return df


def clean_prepare_smart_gas(file_path):
    """
    Input is a dwelling_id.csv file.
    Output are cleaned & prepared dataframes (smart, gas).
    Return: smart, gas
    """
    df = pd.read_csv(file_path, delimiter=';', header=0)
    df = df.rename(index=str, columns={'Timestamp': 'datetime', 'gasTimestamp': 'datetime'})

    smart = df.iloc[:, :7]
    gas = df.iloc[:, 7:]

    #smart = clean_datetime(smart)
    #gas = clean_datetime(gas)

    try:
        smart['datetime'] = pd.to_datetime(smart['datetime'])
        gas['datetime'] = pd.to_datetime(gas['datetime'])
    except:
        print('datetime column contains non-datetime values')
        smart = clean_datetime(smart)
        gas = clean_datetime(gas)
        smart['datetime'] = pd.to_datetime(smart['datetime'])
        gas['datetime'] = pd.to_datetime(gas['datetime'])

    smart = smart.set_index(['datetime'])
    gas = gas.set_index(['datetime'])

    smart = smart.astype(dtype='float32')
    gas = gas.astype(dtype='float32')

    return smart, gas


def df_nan_checker(df, threshold_percentage):
    """
    df: input pandas dataframe
    threshold_percentage: Filter output based on NaN streaks being larger than x % of the total length of the dataframe.

    Checks each column in the input dataframe for NaNs.
    Outputs the amount of NaNs behind each other, including the start and stop index, per column as a sublist.
    For example when the dataframe has three columns.
    Output is in the form of:
    [[column_one_info], [column_two_info], [column_three_info]]
    With the column_..._info being in the form of:
    [start_index, stop_index, amount_of_NaNs]

    TODO: Parellalize, as in one column per core/worker?
    """
    columns = df.columns
    df = df.isnull()
    output = []

    for i in range(len(columns)):
        column_name = columns[i]

        column_info = []
        temp = []
        x = False

        for j, value in enumerate(df[column_name]):
            if x == False and value == True:
                temp.append(df.index[j])
                x = True
            elif x == True and value == True:
                temp.append(df.index[j])
            elif x == True and value == False:
                column_info.append(temp)
                temp = []
                x = False

        lengths = []

        for array in column_info:
            lengths.append([array[0], array[-1], len(array)])

        output.append(lengths)

    # Convert df_info to a readable dataframe instead of list

    """
    Row per column from the 'output' list
    Columns: start-index, stop-index, NaN streak
    """
    columns = df.columns

    df_info = pd.DataFrame(columns=['Column name', 'Start index', 'Stop index', 'Amount of NaNs'])

    for column in range(len(output)):
        for i in range(len(output[column])):
            column_name = df.columns[column]
            start = output[column][i][0]
            stop = output[column][i][1]
            amount = output[column][i][2]
            df_info = df_info.append(
                {'Column name': column_name, 'Start index': start, 'Stop index': stop, 'Amount of NaNs': amount},
                ignore_index=True)
        pass

    percentage = (df_info['Amount of NaNs'] / len(df)) * 100

    df_info.drop(df_info[percentage < threshold_percentage].index, inplace=True)

    return df_info


def smart_gas_nan_checker(smart, gas, dwelling_id):
    """
    Resamples the (smart, gas) dfs to 10s.
    Also calculates gasPower.
    Returns (smart_resampled, gas_resampled)
    """

    # Implement NaN checker here
    # Resample to the same sampling time, use .mean, that way empty gaps will apear as NaNs
    # Generalize it for any df? Resample and handle NaNs based on... threshold.. do stuff..
    print('-- smart, gas resampling --')
    smart_resampled = smart.resample('10s').mean()
    gas_resampled = gas.resample('H').mean() #Needs a check wether cols are 0
    #gas_resampled = gas.resample('10s').mean()

    # Merge the two dfs
    print('-- merge smart gas resampled --')
    smart_gas_resampled_combined = pd.merge(smart_resampled, gas_resampled, left_index=True, right_index=True)

    print('-- smart,gas nan_fig')
    df_nan_fig = plot_nans(smart_gas_resampled_combined, dwelling_id)

    print('-- smart, gas nan_info --')
    df_nan_info = df_nan_checker(smart_gas_resampled_combined, 0)
    #df_nan_info = pd.DataFrame() #empty placeholder
    print('-- resampling smart_gas_resampled_merged --')

    return smart_gas_resampled_combined, df_nan_info, df_nan_fig


def drop_nan_streaks_above_threshold(df, df_nan_info, threshold):
    """
    Drops NaN streaks from the df when they are larger then the threshold value.
    This function also inputs df_nan_info because it already has been made in the smart_gas_nan_checker.
    :param df: Dataframe to process NaNs off
    :param df_nan_info: NaN info dataframe of the input df
    :param threshold: Interpolate if 'Amount of NaNs' from detected NaN streak is below this number.
    :return: dataframe
    """

    # Check for NaN streaks > threshold and drop them form the df
    for i, amount in enumerate(df_nan_info['Amount of NaNs']):
        if amount > threshold:
            start_index = (df_nan_info['Start index'][i])
            stop_index = (df_nan_info['Stop index'][i])
            index_list = df[start_index:stop_index].index
            df = df.drop(index_list)

    return df


def plot_nans(df, dwelling_id):
    plt.clf()
    df = df.isnull()
    #df = df.resample('10D').sum() #resample make amount of NaNs visible

    # Reindex datetimes
    # https://stackoverflow.com/questions/41046630/set-time-formatting-on-a-datetime-index-when-plotting-pandas-series
    try:
        df.index = df.index.to_period('D')
    except:
        print('plot_nans could not set df.index.to_period')

    # Plot heatmap

    n = int(len(df)*0.1) # Choose amount of yticklabels to show
    #fig = sns.heatmap(df, cmap='RdYlGn_r', square=False, yticklabels=n)
    #fig = sns.heatmap(df, cmap='Reds', square=False, vmin=0, cbar_kws={"label": "Amount of NaNs [-]"},
    #                  yticklabels=n)
    try:
        fig = sns.heatmap(df, cmap='Reds', square=False, vmin=0, cbar=True,
                      yticklabels=n*2, cbar_kws={})
    except TypeError:
        print('plot_nans ValueError')
        fig = sns.heatmap(df, cmap='Reds', square=False, vmin=0, cbar=True, cbar_kws={})


    # Set cbar ticks manually
    cbar = fig.collections[0].colorbar
    cbar.set_ticks([0, 1])
    cbar.set_ticklabels(['Not NaN', 'NaN'])

    fig.invert_yaxis()

    # Correct layout
    fig.tick_params(axis='x', rotation=90)
    fig.tick_params(axis='y', rotation=0)
    #fig.grid(alpha=1)
    fig.set(xlabel='Column [-]', ylabel='Index [-]')
    plt.title('Dwelling ID: '+dwelling_id)

    fig = fig.get_figure()
    fig.tight_layout()
    fig.show()
    fig.savefig('//datc//opschaler//nan_information//figures//'+dwelling_id+'.png', dpi=1000)
    return fig


def merge_dfs(df1, df2, df3):
    """
    Merges the dataframes, outputs one df.
    """
    df = pd.merge(df1, df2, left_index=True, right_index=True)
    df = pd.merge(df, df3, left_index=True, right_index=True)

    return df


def save_df(df, dwelling_id):
    dir = '//datc//opschaler//combined_dfs_gas_smart_weather//'
    df.to_csv(dir + dwelling_id + '.csv', sep='\t', index=True)
    print('Saved %s' % dwelling_id)


def read_weather_data():
    weather = pd.read_csv('//datc//opschaler//weather_data//weather.csv', delimiter='\t', comment='#',
                          parse_dates=['datetime'])
    weather = weather.set_index(['datetime'])
    return weather


def smartmeter_data():
    path = '/datc/opschaler/smartmeter_data'
    file_paths = np.array(glob.glob(path + "/*.csv"))
    print('Detected %s smartmeter_data files.' % len(file_paths))
    #
    dwelling_ids = np.array(list((map(lambda x: x[-15:-4], file_paths))))

    return file_paths, dwelling_ids


weather = read_weather_data()
file_paths, dwelling_ids = smartmeter_data()
#file_paths = file_paths[28:29] #10,11 not saved, needs to run for 50+ minutes...
#dwelling_ids = dwelling_ids[28:29]


"""
index 49 is the 'export_P01S01W0000.csv' test dataframe
smart/gasMeter contains a NaN streak of 4 NaNs, this is 28.6 % of the total length.
N=29 is the smallest test df
N=24 is the smallest real df
13 is largest real df
"""
for i in range(len(file_paths)):
    t1 = time.time()
    N = i
    print('---------- N=%s ----------' % i)

    file_path = file_paths[N]
    dwelling_id = dwelling_ids[N]
    print('Selected dwelling_id: '+dwelling_ids[N])

    # Read in raw smartmeter dataframe, split them into smart, gas df
    smart, gas = clean_prepare_smart_gas(file_path)

    print('----- Resampling -----')
    # Resample dataframes (using mean()) and output nan_info
    smart_gas_resampled_combined, df_nan_info, df_nan_fig = smart_gas_nan_checker(smart, gas, dwelling_id)

    print('----- Saving NaN information -----')
    # Save NaN information
    df_nan_info.to_csv('//datc//opschaler//nan_information//'+dwelling_id+'.csv', sep='\t')

    print('----- smart_gas_resampled_combined NaNs -----')
    print(smart_gas_resampled_combined.isnull().sum())


    print('----- Drop NaN streak above threshold -----')
    # drop NaN streaks above threshold
    smart_gas_partly_processed = drop_nan_streaks_above_threshold(smart_gas_resampled_combined, df_nan_info, 6)

    """
    Resample & interpolate dataframes
    Should NOT interpolate ePower, interpolate eMeter... 
    """

    print('----- Interpolating -----')
    # Do you need to resample to 10s again?
    # Problem with this is that it also interpolates ePower
    combined_processed = smart_gas_resampled_combined.resample('10s').interpolate(method='time')

    # After interpolation, ready to combine & save output
    print('----- merge_dfs -----')
    #df = pd.merge(combined_processed, weather, left_index=True, right_index=True)

    print('----- save_df -----')
    save_df(combined_processed, dwelling_id)

    t2 = time.time()
    print('---------- FINISHED iteration %s IN %s ----------' % (i, (t2-t1)))

"""
What slows down the code a lot:
df_nan_checker
clean_datetime
"""
