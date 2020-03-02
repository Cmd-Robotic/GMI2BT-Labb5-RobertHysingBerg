import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# this script should print out some basic plots for the EnergyAndFuelUsage.xlsx file that follows,
# it's static and won't handle changes to the file very well. You have been warned.
title = 'Elproduktion och Bränsleanvändning'
data = pd.read_excel('./EnergyAndFuelUsage.xlsx')
print(data[860:900])
data.dropna(inplace=True) # dropping the nan values makes our life easier since it also gets rid of the trailing info text
print(data)
data.rename(columns={'Elproduktion och bränsleanvändning (MWh) efter region, produktionssätt, bränsletyp och år': 'Län', 'Unnamed: 1': 'Produktionssätt', 'Unnamed: 2': 'Bränsletyp'}, inplace=True)
print(data.dtypes)
data = data.replace('..', np.nan)
data.iloc[:, 4:20].astype('float64', copy=False)
print(data.dtypes)
