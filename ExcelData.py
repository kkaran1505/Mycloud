import pandas as pd
import numpy as np
filepath= r"C:\Users\MY\Desktop\Book1.xlsx"
df = pd.read_excel(filepath)
print(df.head(3))
data= df["Labor_Hours"]
sum= data.sum()
print("Sum of Labor_Hours is: ",sum)
#Mean= df["Production"].mean()
Mean= np.mean(data)
print("Mean of Labor_Hours is: ",Mean)
s_dev= np.std(data)
print("Standard deviation of Labor_Hours is : ",s_dev)