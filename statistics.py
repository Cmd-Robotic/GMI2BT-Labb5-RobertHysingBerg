import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# this script should print out some basic plots for the EnergyAndFuelUsage.xlsx file that follows,
# it's static and won't handle changes to the file very well. You have been warned.
# Also the region changes every 40 rows, the specific category every 8 rows and fuel type every row. Noted here for posterity
title = 'Elproduktion och Bränsleanvändning'
data = pd.read_excel('./EnergyAndFuelUsage.xlsx')
data.dropna(inplace=True) # dropping the nan values makes our life easier since it also gets rid of the trailing info text
print(data)
data.rename(columns={'Elproduktion och bränsleanvändning (MWh) efter region, produktionssätt, bränsletyp och år': 'Län', 'Unnamed: 1': 'Produktionssätt', 'Unnamed: 2': 'Bränsletyp'}, inplace=True)
print(data.dtypes)
data = data.replace('..', np.nan)
data.iloc[:, 4:20].astype('float64', copy=False)
print(data.dtypes)
print(data.iloc[:,4] + data.iloc[:,5])
#TODO put this in a while loop with variables so it plots everything
data.iloc[0:7,3:].transpose().set_axis(data.iloc[0:7,2], axis=1).plot(kind='line', legend=True, title=(data.iloc[0,0] + ', ' + data.iloc[0,1]))
plt.xlabel('År')
plt.ylabel('MWh')
plt.show()