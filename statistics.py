import pandas, matplotlib

data = pandas.read_excel('./EN0203AD.xlsx')
print(data.describe())
print(data.head(20))
print(data.tail(20))