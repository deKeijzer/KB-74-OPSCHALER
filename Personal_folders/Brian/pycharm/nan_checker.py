import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/datc/opschaler/smartmeter_data/export_P01S01W0373.csv', delimiter=';', parse_dates=['Timestamp'])

plt.plot(df['Timestamp'], df['eMeter'])
plt.show()
