
# coding: utf-8

# In[1]:

import numpy as np
import glob
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import time

# In[2]:

def test1(x):
    return x

def test2(x):
    y = test1(x)+test1(x)
    return y
    


# def datetime_layout(dwelling_id, y, y2=None, y3=None, y4=None):
#     def layout():
#         plt.xticks(rotation=45)
#         plt.grid()
#         plt.tight_layout()

#     x = df[datetime]
    
    
#     plt.subplot(3,2,1)
#     plt.plot(x, df[y], '-', color='r', linewidth=0.3)
#     #plt.xlabel('Date [-]')
#     plt.ylabel('Global Radiation [J/m$^2$]')
#     datetime_layout()

#     plt.subplot(3,2,2)
#     plt.plot(x, data['T'], '-', color='r', linewidth=0.3)
#     #plt.xlabel('Date [-]')
#     plt.ylabel('Temperature [°C]')
#     datetime_layout()

#     plt.subplot(3,2,3)
#     plt.plot(x, data['ePower'], '-', color='r', linewidth=0.3)
#     #plt.xlabel('Date [-]')
#     plt.ylabel('ePower [kWh]')
#     datetime_layout()

#     plt.subplot(3,2,4)
#     plt.plot(x, data['gasPower'], '-', color='r', linewidth=0.3)
#     #plt.xlabel('Date [-]')
#     plt.ylabel('gasPower [m$^3$]')
#     datetime_layout()

def read_(select, sample_rate='_hour',processed=True):
    path = '//datc//opschaler//combined_gas_smart_weather_dfs//'
    folder_ = 'processed//'
    if processed == False:
        folder_ = 'unprocessed//'
    if sample_rate == '10s':
        sample_rate = '_10s'    
    complete_path = path+folder_+select+sample_rate+".csv"
    df = pd.read_csv(complete_path,sep='\t',index_col=None)
        
    return df, select, complete_path, sample_rate, processed


def dwel_path_id(sample_rate, folder, combined):
    """
    Reads in the file paths and dwelling id's of the combined smartmeter data.
    :return: file_paths, dwelling_ids, both as lists.
    """
    path = '//datc//opschaler//combined_gas_smart_weather_dfs//'
    map_ = 'processed//'
    subscript = '_hour'
    combined_ = 'P*'

    if sample_rate == '10s':
        subscript = '_10s'
    if folder == 'unprocessed':
        map_ = 'unprocessed//'
    if combined == 'yes':
        combined_ = 'all_dwellings_combined'
        
    complete_path = path+map_+combined_+subscript+".csv"
    file_paths = np.array(glob.glob(complete_path))

    print('complete_path: '+complete_path)
    print('Detected %s smartmeter_data files.' % len(file_paths))
    
    dwelling_ids = np.array(list((map(lambda x: x[-20:-9], file_paths)))) 
    
    if sample_rate == '10s':
        dwelling_ids = np.array(list((map(lambda x: x[-19:-8], file_paths)))) # 10s ids slicing
    if combined == 'yes':
        dwelling_ids = 'Used all dwellings to make this df'    
    
    return file_paths, dwelling_ids

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
    df = df.dropna(subset = ['datetime'])
    return df

def clean_prepare_smart_gas(file_path):
    """
    Input is a dwelling_id.csv file.
    Output are cleaned & prepared dataframes (smart, gas).
    Return: smart, gas
    """
    df = pd.read_csv(file_path, delimiter=';', header=0)
    smart = df.iloc[:,:7]
    gas = df.iloc[:,7:]
    
    smart = smart.rename(index=str,columns={"Timestamp":"datetime"})
    gas = gas.rename(index=str,columns={"gasTimestamp":"datetime"})

    smart = clean_datetime(smart)
    gas = clean_datetime(gas)
    
    smart['datetime'] = pd.to_datetime(smart['datetime'])
    gas['datetime'] = pd.to_datetime(gas['datetime'])

    
    smart = smart.set_index(['datetime'])
    gas = gas.set_index(['datetime'])

    return smart, gas

def resample_smart_gas(smart, gas):
    """
    Resamples the (smart, gas) dfs to 10s.
    Also calculates gasPower. 
    Returns (smart_resampled, gas_resampled)
    """
    smart_resampled = smart.resample('10s').mean()
    
    gas_resampled = gas.resample('H').mean()
    # replace 0s with NaNs
    gas_resampled = gas_resampled.resample('10s').interpolate(method='time')
    gas_resampled['gasPower'] = gas_resampled['gasMeter'].diff()
    
    return smart_resampled, gas_resampled

def merge_smart_gas_weather(smart_resampled, gas_resampled, weather):
    """
    Merges the dataframes, outputs one df.
    """
    df = pd.merge(smart_resampled, gas_resampled, left_index=True, right_index=True)
    df = pd.merge(df, weather, left_index=True, right_index=True)
    
    return df

def save_df(df, dwelling_id):
    dir = '//datc//opschaler//combined_dfs_gas_smart_weather//'
    df.to_csv(dir+dwelling_id+'.csv', sep='\t', index=True)
    print('Saved %s' % dwelling_id)
    
def main_df_prep():
    for i,file_path in enumerate(file_paths):
        t1 = time.time()
        dwelling_id = file_paths[i][-15:-4]
        print('Started iteration %s, processing dwelling_id: %s' % (i,dwelling_id))
        
        smart, gas = clean_prepare_smart_gas(file_paths[i])
        smart_resampled, gas_resampled = resample_smart_gas(smart, gas)
        df = merge_smart_gas_weather(smart_resampled, gas_resampled, weather)
        save_df(df, dwelling_id)
        t2 = time.time()
        print('Finished iteration %s in %.1f [s], Finished processing dwelling_id: %s, ' % (i,(t2-t1), dwelling_id))
        print('-----')
# def nan_table(sample_rate):
#     file_paths, dwelling_ids = dwelling_data_paths(sample_rate)
#     dfs_nan_table = []

#     for i, path in enumerate(paths):
#         dwelling_id = dwelling_ids[i]
#         df = read_combined_df(path, dwelling_id)
#         dfs_nan_table.append(df)
        
#     final_df = pd.concat(dfs_nan_table)
    
#     return final_df
    

def corr_df(dwelling_id, corr_dim):
    plt.style.use('default')

    df = pd.read_csv("/datc/opschaler/combined_gas_smart_weather_dfs/processed/"+dwelling_id+"_hour.csv",header=0,delimiter="\t",parse_dates = ['datetime'])
    df = df.set_index(['datetime'])

    if corr_dim == '1h':
        df = df
    if corr_dim == '3h':
        df = df.resample('3H').mean()
    if corr_dim == '6h':
        df = df.resample('6H').mean()
    if corr_dim == '12h':
        df = df.resample('12H').mean()
    if corr_dim == '1d':
        df = df.resample('1D').mean()
    if corr_dim == '1w':
        df = df.resample('1W').mean()
    
    rdf = df[df['T'] < 16]
    
    corr = rdf.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    fig, ax = plt.subplots(figsize=(25,25))

    sns.heatmap(corr, mask=mask, square=False, cmap='RdYlGn', annot=True, ax=ax,
                cbar_kws={'label':'Pearson correlation coefficient [-]'})

    plt.title('Correlation Matrix')
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    return plt.show()




def dwel_len(dwelling_id):
    """
    Get the total amount of days of an unprocessed dwelling_id.
    """
    dir = '//datc//opschaler//combined_gas_smart_weather_dfs//unprocessed//'
    df = pd.read_csv(dir+dwelling_id+'_10s.csv', delimiter='\t', parse_dates=['datetime'])
    df = df['datetime'] # only keep the datetime column
    start_date = df.iloc[0]
    stop_date = df.iloc[-1]
    
    del df # Free up memory
    
    recorded_days = (stop_date - start_date).days # total amount of recorded days

    return recorded_days, start_date, stop_date









#def read_in

#def read_in_10s

#def read_in_h



# In[ ]:



