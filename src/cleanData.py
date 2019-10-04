#import matplotlib.pyplot as plt
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
import warnings; warnings.simplefilter('ignore')
import csv
from pathlib import Path


shares=["RDSB.L","BP.L","CNE.L","PMO.L"]
def cleandata(data):
    # Read oil price and transform data

    shares=["RDSB.L","BP.L","CNE.L","PMO.L"]
    xls_file=pd.ExcelFile("/downloaded_data/RBRTEd.xls") # Read Excel
    brate=xls_file.parse("Data 1") # Read sheet Data 1
    brate.columns=brate.iloc[1] # set row 1 as column name
    brate=brate.ix[2:] # remove first 2 rows
    brate["Date"]=brate["Date"].astype('datetime64[ns]') # Convert column to date format
    brate.columns=["date","oil_price"]
    #print(brate.head())

    # here we will store all the data from all shares and oil price in a master dataframe
    all_data=pd.DataFrame() 
    for index in range(len(shares)):
        stock=pd.DataFrame()

        # 1.- Read files
        stock=pd.read_csv("src/downloaded_data/"+shares[index]+".csv")  
        # 2.- Transform data
        stock=stock[["Date","Close"]]       
        stock["Date"]=stock["Date"].astype('datetime64[ns]')
        stock.columns=["date","share_price"]
        test=pd.DataFrame(brate) # VLOOKUP equivalent in Python to merge 2 sets of data
        output=stock.merge(test,on="date",how="left")
        #print(output)
        stock["oil_price"]=output["oil_price"]
        stock['share_price']=pd.to_numeric(stock['share_price'], errors='coerce').dropna(0)
        stock['oil_price']=pd.to_numeric(stock['oil_price'], errors='coerce').dropna(0)
        stock["year"]=pd.to_datetime(stock["date"]).dt.year # Create a column with the year to filter later
        stock["name"]=shares[index]
        stock = stock.dropna() # get rid of all the NAN rows.
        #print(stock)

        # 4.- Append data to a master dataframe
        all_data=all_data.append(stock) #append data to one matrix
    
    #all_data.head()
    if data == "brate":
        return brate
    elif data == "all":
        return all_data


#value=cleandata("brate")
#print(value)

#creates csv file for raw data file in data/new_data/ directory
df1=pd.DataFrame() 
root_folder = "src"
for index in range(len(shares)):
    df1 = pd.read_csv("src/downloaded_data/"+shares[index]+".csv")
    #df = df.set_index('Date')
    del df1['Volume'] #dropping Volume column
    df1["Date"] = pd.to_datetime(df1['Date']) #converting string to a datetime
    df1 = df1.dropna() # get rid of all the NAN rows.
    df1["Month"]=pd.to_datetime(df1["Date"]).dt.month  # Create a column with the month to filter later
    df1["Year"]=pd.to_datetime(df1["Date"]).dt.year  # Create a column with the year to filter later
    df1 = df1.set_index('Date')
    #print(df)

    output_file = 'new.'+shares[index]+'.csv'
    output_dir = Path('src/new_data')
    output_dir.mkdir(parents=True, exist_ok=True) #Setting parents=True will also create any necessary parent directories, and exist_ok=True means it won't raise an error if the directory already exists.
    df1.to_csv(output_dir / output_file)
    #df.to_csv("data/cleanData/new."+name+".csv", index = None, header=True) #Don't forget to add '.csv' at the end of the path
    
print("Cleaned data files generated.")
#csvfile("BP.L")