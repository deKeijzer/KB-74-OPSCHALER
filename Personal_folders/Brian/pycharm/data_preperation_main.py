import pandas as pd
import numpy as np
import glob
import time


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

    smart = clean_datetime(smart)
    gas = clean_datetime(gas)

    smart['datetime'] = pd.to_datetime(smart['datetime'])
    gas['datetime'] = pd.to_datetime(gas['datetime'])

    smart = smart.set_index(['datetime'])
    gas = gas.set_index(['datetime'])

    smart = smart.astype(dtype='float32')
    gas = gas.astype(dtype='float32')

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
    df.to_csv(dir + dwelling_id + '.csv', sep='\t', index=True)
    print('Saved %s' % dwelling_id)


def main():
    for i, file_path in enumerate(file_paths):
        t1 = time.time()
        # dwelling_id = file_paths[i][-15:-4]
        dwelling_id = file_paths[i][-15:-4]
        print('Started iteration %s, processing dwelling_id: %s' % (i, dwelling_id))

        smart, gas = clean_prepare_smart_gas(file_paths[i])
        smart_resampled, gas_resampled = resample_smart_gas(smart, gas)
        df = merge_smart_gas_weather(smart_resampled, gas_resampled, weather)
        save_df(df, dwelling_id)
        t2 = time.time()
        print('Finished iteration %s in %.1f [s], Finished processing dwelling_id: %s, ' % (i, (t2 - t1), dwelling_id))
        print('-----')


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


file_paths, dwelling_ids = smartmeter_data()

# index 48 is the 0000 test dataframe
smart, gas = clean_prepare_smart_gas(file_paths[48])