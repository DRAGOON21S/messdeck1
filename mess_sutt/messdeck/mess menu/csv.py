#inporting panda as pd and json
import pandas as pd
import json
datapath=r"messmenu.csv"
df = pd.read_csv(datapath,header=None)
#removing NaN and assigning then empty string
df.fillna(' ',inplace=True)
#dropping rows with days,breakfast
df.drop([0,2,12,13,22,23], axis=0, inplace=True)
#to fix date format
df.iloc[0]=pd.to_datetime(df.iloc[0], format ='mixed').dt.strftime("%Y-%m-%d")
#to change datatype to strings
df2 = df.astype("string")
#to reset indexing bcz we dropped some rows
df2.reset_index(drop = True, inplace = True)
#creating a base directory
mess = {}
#assuming variable
x=0 
#Starting 2 nested loops to iterate each cell individually
while x<len(df2.columns):
    Breakfast = []
    Lunch = []
    Dinner = []
    y=0
    while y<len(df2):
        #checking if the cell is empty or *
        if df2.iloc[y,x][0] == " " or df2.iloc[y,x][0]=='*':
            y=y+1
            continue
        #if y falls within these values we are appending it to the Breakfast list
        elif y>0 and y<10:
            Breakfast.append(df2.iloc[y,x])
        #if y falls within these values we are appending it to the lunch list
        elif y>9 and y<18:
            Lunch.append(df2.iloc[y,x])
        #if y falls within these values we are appending it to the dinner list
        elif y>17 and y<=24:
            Dinner.append(df2.iloc[y,x])
        #increment in y to change row
        y=y+1
    #After creating list we are add them to the directory with respective date
    mess[ df2.iloc[0,x]] = {
        'BREAKFAST':Breakfast ,
        'LUNCH':Lunch,
        'DINNER':Dinner}
    #increment in x to change column
    x=x+1
    
    
# print(mess)
# =============================================================================
# creating a json object to store whole directory
# =============================================================================
qwerty = json.dumps(mess,indent=4)
with open("asdf.json","w") as outfile:
   outfile.write(qwerty)
    
    
    
        
        
        
        