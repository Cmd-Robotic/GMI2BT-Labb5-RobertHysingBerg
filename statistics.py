import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# this script should print out some basic plots for the EnergyAndFuelUsage.xlsx file that follows,
# it's static and won't handle changes to the file very well. You have been warned.
# Also the region changes every 40 rows, the specific category every 8 rows and fuel type every row. Noted here for posterity
title = 'Elproduktion och Bränsleanvändning'
data = pd.read_excel('./EnergyAndFuelUsage.xlsx')
data.dropna(inplace=True) # dropping the nan values makes our life easier since it also gets rid of the trailing info text
# print(data)
data.rename(columns={'Elproduktion och bränsleanvändning (MWh) efter region, produktionssätt, bränsletyp och år': 'Län', 'Unnamed: 1': 'Produktionssätt', 'Unnamed: 2': 'Bränsletyp'}, inplace=True)
# print(data.dtypes)
data = data.replace('..', np.nan)
data.iloc[:, 4:20].astype('float64', copy=False)
# print(data.dtypes)
# print(data.iloc[:,4] + data.iloc[:,5])
# fig, axes = plt.subplots(nrows=1,ncols=2)
plottingPosition = 24  #Should be incremented in steps of 8
startPlotPosition = plottingPosition
plotType = 'line'
plotCounter = 0     #where to start plotting from
plottingStop = 21   #the number of regions to plot - 1 or it's gonna throw an exception
subplotRow = 0
subplotColumn = 0
# Plotting the country first so it doesn't overshadow the rest of the data
data.iloc[plottingPosition:plottingPosition+1,3:].transpose().set_axis(data.iloc[plottingPosition:plottingPosition+1,0], axis=1).plot(kind=plotType, legend=True, title=(data.iloc[plottingPosition,1] + ', ' + data.iloc[plottingPosition,2]))
plottingPosition += 40
plt.xlabel('År')
plt.ylabel('MWh')
#Initial plot so we can conatenate two dataframes together
plotData = data.iloc[plottingPosition:plottingPosition+1,3:].transpose().set_axis(data.iloc[plottingPosition:plottingPosition+1,0], axis=1)
plottingPosition += 40
while(plotCounter < plottingStop / 2 - 1):
    plotData = pd.concat([plotData, data.iloc[plottingPosition:plottingPosition+1,3:].transpose().set_axis(data.iloc[plottingPosition:plottingPosition+1,0], axis=1)], axis=1, sort=False)
    plottingPosition += 40
    plotCounter += 1
# Splitting the graph into two
plotData.plot(kind=plotType, legend=True, title=(data.iloc[startPlotPosition,1] + ', ' + data.iloc[startPlotPosition,2]))
plt.xlabel('År')
plt.ylabel('MWh')
plotData = data.iloc[plottingPosition:plottingPosition+1,3:].transpose().set_axis(data.iloc[plottingPosition:plottingPosition+1,0], axis=1)
plottingPosition += 40
while(plotCounter < plottingStop):
    plotData = pd.concat([plotData, data.iloc[plottingPosition:plottingPosition+1,3:].transpose().set_axis(data.iloc[plottingPosition:plottingPosition+1,0], axis=1)], axis=1, sort=False)
    plottingPosition += 40
    plotCounter += 1
plotData.plot(kind=plotType, legend=True, title=(data.iloc[startPlotPosition,1] + ', ' + data.iloc[startPlotPosition,2]))
plt.xlabel('År')
plt.ylabel('MWh')
plt.show()