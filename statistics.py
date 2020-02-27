import numpy as np
import pandas as pd
import matplotlib as mpl

data = pd.read_excel('./EN0203AD.xlsx')
print(data.describe())