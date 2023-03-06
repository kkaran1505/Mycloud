import pandas as pd
filepath = r'C:\Users\MY\Desktop\melb_data.csv'
data = pd.read_csv(filepath)
print(data.describe())