"""
Shifr+F9 (Debug first, then plots will appear in SciView)

TODO: add legend to plot_nans
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
    TODO: Speed up the function
    Input should be a df with a column called 'datetime'.
    This function checks wether a row in the df.datetime column can be parsed to a Pandas datetime object,
    by trying pd.to_datetime() on it.
    If it fails it will replace that row with np.nan().
    Finally this function will return the df with the NaN rows dropped.
    It only drops the row if the datetime column contains a NaN.

    :param df: Pandas DataFrame containing a datetime column called 'datetime'.
    :return: Pandas DataFrame
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

    :param file_path: path to 'dwelling_id.csv' file
    :return: Smart and gas Pandas DataFrames
    """
    df = pd.read_csv(file_path, delimiter=';', header=0)
    df = df.rename(index=str, columns={'Timestamp': 'datetime', 'gasTimestamp': 'datetime'})

    smart = df.iloc[:, :7]
    gas = df.iloc[:, 7:]

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
    TODO: Parellalize, as in one column per core/worker?
    Checks each column in the input dataframe for NaNs.
    Outputs the amount of NaNs behind each other, including the start and stop index, per column as a sublist.
    For example when the dataframe has three columns.
    Output is in the form of:
    [[column_one_info], [column_two_info], [column_three_info]]
    With the column_..._info being in the form of:
    [start_index, stop_index, amount_of_NaNs]

    :param df: Pandas DataFrame
    :param threshold_percentage: Filter output based on NaN streaks being larger than x % of the total length of the dataframe.
    :return: Pandas DataFrame
    """

    columns = df.columns
    df = df.isnull()
    output = []
    length = len(columns)

    for i in range(length):
        #print('At iteration %s of %s' % (i, length))
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

    df_info = pd.DataFrame(columns=['Column name', 'Start index', 'Stop index', 'Amount of NaNs'])
    length = len(output)
    column_names = []
    starts = []
    stops = []
    amounts = []

    for column in range(length):
        #print('At iteration %s of %s' % (column, length))
        for i in range(len(output[column])):
            column_names.append(df.columns[column])
            starts.append(output[column][i][0])
            stops.append(output[column][i][1])
            amounts.append(output[column][i][2])

    print('Appending NaN info to df')
    # Convert list to pd series
    column_names = pd.Series(column_names)
    starts = pd.Series(starts)
    stops = pd.Series(stops)
    amounts = pd.Series(amounts)
    # Append pd series to a column
    df_info['Column name'] = column_names.values
    df_info['Start index'] = starts.values
    df_info['Stop index'] = stops.values
    df_info['Amount of NaNs'] = amounts.values

    percentage = (df_info['Amount of NaNs'] / len(df)) * 100
    df_info.drop(df_info[percentage < threshold_percentage].index, inplace=True)

    return df_info


def smart_gas_nan_checker(smart, gas, weather, dwelling_id):
    """
    Resamples the (smart, gas) dfs to 10s.
    Also calculates gasPower.
    Returns (smart_resampled, gas_resampled)

    Original sample rates are as follows:
    smart: 10 seconds
    gas: 1 hour
    weather: 10 minutes

    :param smart: Pandas DataFrame
    :param gas: Pandas DataFrame
    :param weather: Pandas DataFrame
    :param dwelling_id: String
    :return: smart_resampled, gas_resampled as a Pandas DataFrame
    """

    print('Resampling smart, gas, weather')
    # For more resampling info see: https://pandas.pydata.org/pandas-docs/stable/api.html#id41
    # Makes missing gaps appear as NaN, these are the general raw dataframes to work with
    smart_10s = smart.resample('10s').mean()
    gas_h = gas.resample('H').mean()
    weather_10min = weather.resample('10min').mean()

    """
    Create a dataframe with a 1 hour sample rate
    """
    gas_h['gasPower'] = gas_h['gasMeter'].diff()  # Calculate gasPower column
    gas_h['gasPower'][0] = gas_h['gasPower'][1]  # Replace 1st entry (NaN) with 2nd entry

    smart_h = smart_10s.resample('H').mean()  # Down sample smart
    weather_h = weather_10min.resample('H').mean()  # Down sample weather

    # Combine gas, smart, weather
    df_hour = pd.merge(smart_h, gas_h, left_index=True, right_index=True)
    df_hour = pd.merge(df_hour, weather_h, left_index=True, right_index=True)

    """
    Create smartmeter dataframe with a 10s sample rate
    """
    gas_10s = gas_h.resample('10s').ffill()  # Up sample gas to 10s
    # Calculate gasPower column, is this rhe right way? Or should we ffill it?
    # Currently this code makes it so there is one gasPower value per hour, we could ffill this also?
    gas_10s['gasPower'] = gas_10s['gasMeter'].diff()
    gas_10s['gasPower'][0] = gas_10s['gasPower'][1]  # Replace 1st entry (NaN) with 2nd entry

    weather_10s = weather_10min.resample('10s').ffill()  # forward fill because the raw data is the 10 minute mean

    # Combine gas, smart, weather
    df_10s = pd.merge(smart_10s, gas_10s, left_index=True, right_index=True)
    df_10s = pd.merge(df_10s, weather_10s, left_index=True, right_index=True)

    """
    Do NaN analysis on the 10s and hour sample rate dataframes
    """
    print('Length of combined df_10s: %s' % len(df_10s))
    print('df_nan_fig_10s')
    df_nan_fig_10s = plot_nans(df_10s, dwelling_id+' 10s sample rate')
    print('df_nan_table_10s')
    df_nan_table_10s = df_nan_checker(df_10s, 0)

    print('Length of combined df_hour: %s' % len(df_hour))
    print('df_nan_fig_hour')
    df_nan_fig_hour = plot_nans(df_hour, dwelling_id+' 1 hour sample rate')
    print('df_nan_table_hour')
    df_nan_table_hour = df_nan_checker(df_hour, 0)

    return df_10s, df_hour, df_nan_table_10s, df_nan_table_hour, df_nan_fig_hour, df_nan_fig_10s


def drop_nan_streaks_above_threshold(df, df_nan_table, thresholds):
    """
    Drops NaN streaks from the df when they are larger then the threshold value.
    This function also inputs df_nan_table because it already has been made in the smart_gas_nan_checker.
    :param df: Pandas DataDrame to process NaNs off
    :param df_nan_table: NaN info Pandas DataFrame of the input df
    :param thresholds: Dictionary {'column_name':column_threshold}, column_threshold has to be an integer.
    :return: Pandas DataFrame
    """

    # Check for NaN streaks > threshold and drop them from the df
    length = len(df_nan_table['Amount of NaNs'])
    print('df_nan_table length: %s' % length)

    indices_to_drop = []
    for i, amount in enumerate(df_nan_table['Amount of NaNs']):
        selected_column = df_nan_table['Column name'][i]
        try:
            if amount > thresholds[selected_column]:
                start_index = (df_nan_table['Start index'][i])
                stop_index = (df_nan_table['Stop index'][i])
                indices = df[start_index:stop_index].index
                print('Enumeration %s of %s | From \t %s \t to \t %s | column %s | NaN streak length: %s'
                      % (i, length, start_index, stop_index, selected_column, (len(indices))))
                try:
                    indices_to_drop += indices
                except:
                    print('Could not add indices to indices_to_drop list')
            else:
                #print('amount < threshold')
                pass
        except:
            #print('No threshold detected for %s' % selected_column)
            pass

    print('Dropping NaN streaks > threshold')
    l1 = len(df)
    df = df.drop(indices_to_drop)
    l2 = len(df)
    print('Removed %s rows' % (l1-l2))
    return df


def plot_nans(df, dwelling_id):
    """
    Create a heatmap of the NaNs in the input DataFrame.
    :param df: Pandas DataFrame
    :param dwelling_id: String
    :return: Seaborn heatmap as a Figure
    """
    plt.clf()
    df = df.isnull()
    # Downsample to make all data visible
    df = df.resample('1T').sum()  # Downsample to make small NaNs visible
    df = df.apply(lambda x: x > 0, 1)  # Replace values >0 with 1

    # Reindex datetimes
    # https://stackoverflow.com/questions/41046630/set-time-formatting-on-a-datetime-index-when-plotting-pandas-series
    try:
        df.index = df.index.to_period('D')
    except:
        print('plot_nans could not set df.index.to_period')

    # Plot heatmap
    n = int(len(df)*0.1)  # Choose amount of yticklabels to show

    try:
        fig = sns.heatmap(df, cmap='Reds', square=False, vmin=0, cbar=False, yticklabels=n*2, cbar_kws={})
    except TypeError:
        print('plot_nans ValueError')
        fig = sns.heatmap(df, cmap='Reds', square=False, vmin=0, cbar=False, cbar_kws={})

    # Set cbar ticks manually
    #cbar = fig.collections[0].colorbar
    #cbar.set_ticks([0, 1])
    #cbar.set_ticklabels(['Not NaN', 'NaN'])

    # Correct layout
    fig.invert_yaxis()
    fig.tick_params(axis='x', rotation=90)
    fig.tick_params(axis='y', rotation=0)
    fig.set(xlabel='Column [-]', ylabel='Index [-]')
    plt.title('Dwelling ID: '+dwelling_id)

    fig = fig.get_figure()
    fig.tight_layout()
    fig.show()
    print('Saving heatmap')
    fig.savefig('//datc//opschaler//nan_information//figures//' + dwelling_id + '.png', dpi=1200)

    return fig


def save_df_processed(df, dwelling_id):
    """
    Save interpolated dataframe.
    :param df: Pandas DataFrame
    :param dwelling_id: String
    :return: None
    """
    dir = '//datc//opschaler//combined_gas_smart_weather_dfs//processed//'
    df.to_csv(dir + dwelling_id + '.csv', sep='\t', index=True)
    print('Saved processed df: %s' % dwelling_id)
    return


def save_df_unprocessed(df, dwelling_id):
    """
    Save unprocessed dataframe.
    :param df: Pandas DataFrame
    :param dwelling_id: String
    :return: None
    """
    dir = '//datc//opschaler//combined_gas_smart_weather_dfs//unprocessed//'
    df.to_csv(dir + dwelling_id + '.csv', sep='\t', index=True)
    print('Saved not unprocessed df: %s' % dwelling_id)
    return


def dwelling_information (smart_gas_weather_resampled_combined, df_nan_table):
    # create dataframe to store all information from the different files
    df_dwelling_information = pd.DataFrame(columns={'Dwelling ID', 'file size [MB]', 'initial date', 'final date',
                                                    'days', 'total amount of NaNs', 'largest max consecutive NaNs',
                                                    'second largest max consecutive NaNs',
                                                    'third_largest_max_consecutive_NaNs'})

    # order of column names changed for some reason, line(below) fixes this, although ugly
    df_dwelling_information = df_dwelling_information[['Dwelling ID', 'file size [MB]', 'initial date', 'final date',
                                                       'days', 'total amount of NaNs', 'largest max consecutive NaNs',
                                                       'second largest max consecutive NaNs',
                                                       'third_largest_max_consecutive_NaNs']]

    # smart needs to be replaced with name of df that is read in (raw, combined)
    df_dwelling_information.loc[len(df_nan_table.index)] = [dwelling_id,
                                                 smart_gas_weather_resampled_combined.memory_usage(index=True).sum()/1000000,
                                                 smart_gas_weather_resampled_combined.index[0],
                                                 smart_gas_weather_resampled_combined.index[-1],
                                             smart_gas_weather_resampled_combined.index[-1] - smart_gas_weather_resampled_combined.index[0],
                                             df_nan_table['Amount of NaNs'].sum(),
                                                 df_nan_table['Amount of NaNs'].nlargest(1),
                                             df_nan_table['Amount of NaNs'].nlargest(2),
                                                 df_nan_table['Amount of NaNs'].nlargest(3)]
    return df_dwelling_information


def read_weather_data():
    """
    Reads in the weather Pandas DataFrame.
    :return: Pandas DataFrame
    """
    # Check if UTC to gmt+1 conversion is being handled correctly
    weather = pd.read_csv('//datc//opschaler//weather_data//knmi_10_min_raw_data//output//df_combined_uncleaned.csv',
                          delimiter='\t', comment='#',
                          parse_dates=['datetime'])
    weather = weather.set_index(['datetime'])
    return weather


def smartmeter_data():
    """
    Reads in the file paths and dwelling id's of the smartmeter data.
    :return: file_paths, dwelling_ids, both as lists.
    """
    path = '/datc/opschaler/smartmeter_data'
    file_paths = np.array(glob.glob(path + "/*.csv"))

    print('Detected %s smartmeter_data files.' % len(file_paths))
    dwelling_ids = np.array(list((map(lambda x: x[-15:-4], file_paths))))

    return file_paths, dwelling_ids


def process_dfs(df_10s, df_hour):
    """
    Forward fill all weather data.
    Interpolate: smart & gas data, except for ePower, ePowerReturn and gasPower.
    ePower, ePowerReturn and gasPower might still contains NaNs.
    These can be dropped after reading in the processed df, if required.

    :param df_10s: Pandas DataFrame
    :param df_hour:  Pandas DataFrame
    :return: Pandas DataFrame
    """
    columns_to_ffill = ['DD', 'DR', 'FF', 'FX', 'N', 'P', 'Q', 'RG', 'SQ', 'T', 'T10', 'TD', 'U', 'VV', 'WW']
    columns_to_interpolate = ['eMeter', 'eMeterReturn', 'eMeterLowReturn', 'gasMeter']

    print('Processing df_10s')
    df_10s[columns_to_ffill] = df_10s[columns_to_ffill].fillna(method='ffill')
    df_10s[columns_to_interpolate] = df_10s[columns_to_interpolate].interpolate(method='time')
    df_10s_processed = df_10s
    print('Amount of NaNs left in df_10s_processed: %s' % df_10s_processed.isnull().sum().sum())

    print('Processing df_hour')
    df_hour[columns_to_ffill] = df_hour[columns_to_ffill].fillna(method='ffill')
    df_hour[columns_to_interpolate] = df_hour[columns_to_interpolate].interpolate(method='time')
    df_hour_processed = df_hour
    print('Amount of NaNs left in df_hour_processed: %s' % df_hour_processed.isnull().sum().sum())

    return df_10s_processed, df_hour_processed


# Start the main loop
t1 = time.time()

print('Reading in weather data')
weather = read_weather_data()
file_paths, dwelling_ids = smartmeter_data()

print(dwelling_ids)

file_paths = file_paths[0:1]
dwelling_ids = dwelling_ids[0:1]

"""
index 49 is the 'export_P01S01W0000.csv' test dataframe
smart/gasMeter contains a NaN streak of 4 NaNs, this is 28.6 % of the total length.
N=27:28 is the smallest test df
daan 21:22
"""
for N in range(len(file_paths)):
    t2 = time.time()
    print('---------- N=%s ----------' % N)

    file_path = file_paths[N]
    dwelling_id = dwelling_ids[N]
    print('Selected dwelling_id: '+dwelling_ids[N])

    print('----- clean_prepare_smart_gas -----')
    # Read in raw smartmeter dataframe, split them into smart, gas df
    smart, gas = clean_prepare_smart_gas(file_path)

    print('----- smart_gas_nan_checker -----')
    # Resample dataframes (using mean()), then upsample to 10s using ffill and output nan_info
    df_10s, df_hour, df_nan_table_10s, df_nan_table_hour, df_nan_fig_hhour, df_nan_fig_10s = smart_gas_nan_checker(smart, gas, weather, dwelling_id)

    print('----- save_df_unprocessed -----')
    save_df_unprocessed(df_10s, dwelling_id+'_10s')
    save_df_unprocessed(df_hour, dwelling_id+'_hour')

    print('----- df_nan_table.to_csv -----')
    df_nan_table_10s.to_csv('//datc//opschaler//nan_information//'+dwelling_id+'_10s.csv', sep='\t')
    df_nan_table_hour.to_csv('//datc//opschaler//nan_information//' + dwelling_id + '_hour.csv', sep='\t')

    print('----- smart_gas_resampled_combined NaNs -----')
    print('df_10s NaNs: %s' % df_10s.isnull().sum())
    print('df_hour NaNs: %s' % df_10s.isnull().sum())

    """
    Original sample rate:
    Electricity: 10 seconds
    gas: 1 hour
    weather: 10 minutes
    
    So for example setting the thresholds for the 10s dataframe:
    
    eMeter   6 -> equals a 60 seconds gap
    ePower   6 -> equals a 60 seconds gap
    gasMeter 360 -> equals a 1 hour gap
    T       6 -> equals a 1 hour gap
    Q       6 -> equals a 1 hour gap 
    """
    print('----- drop_nan_streaks_above_threshold -----')
    thresholds_10s = {'eMeter': 6, 'ePower': 6, 'gasMeter': 720, 'T': 12, 'Q': 12}
    df_10s_partly_processed = drop_nan_streaks_above_threshold(df_10s, df_nan_table_10s, thresholds_10s)

    thresholds_hour = {'eMeter': 2, 'ePower': 2, 'gasMeter': 2, 'T': 2, 'Q': 2}
    df_hour_partly_processed = drop_nan_streaks_above_threshold(df_hour, df_nan_table_hour, thresholds_hour)

    print('----- dwelling_information -----')
    dwelling_info_df_10s = dwelling_information(df_10s, df_nan_table_10s)
    dwelling_info_df_10s.to_csv('//datc//opschaler//dwelling_information//'+dwelling_id+'_10s.csv', sep='\t')

    dwelling_info_df_hour = dwelling_information(df_hour, df_nan_table_hour)
    dwelling_info_df_hour.to_csv('//datc//opschaler//dwelling_information//'+dwelling_id+'_hour.csv', sep='\t')

    """
    Resample & interpolate dataframes
    Should NOT interpolate ePower, interpolate eMeter... 
    """

    print('----- process_dfs -----')
    # Process NaNs
    df_10s_processed, df_hour_processed = process_dfs(df_10s, df_hour)


    print('----- save_df_interpolated -----')
    save_df_processed(df_10s_processed, dwelling_id+'_10s')
    save_df_processed(df_hour_processed, dwelling_id+'_hour')

    t3 = time.time()
    print('------------------------------ FINISHED iteration %s in %.1f [s]' % (N, (t3-t2)))

t4 = time.time()
print('Total runtime: %.1f [s]' % (t4-t1))

"""
What slows down the code a lot:
df_nan_checker
clean_datetime
"""

