import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('./EnergyAndFuelUsage.xlsx')
print(data.describe())
print(data.dtypes)