import pandas as pd
import json
datapath=r"messmenu.csv"
df = pd.read_csv(datapath,header=None)
df.drop([0,12,22], axis=0, inplace=True)
df.fillna(' ',inplace=True)
df.iloc[0]=pd.to_datetime(df.iloc[0], format ='mixed').dt.strftime("%Y-%m-%d")
print(df)
df2 = df.astype("string")
df2.reset_index(drop = True, inplace = True)
print(df2)

