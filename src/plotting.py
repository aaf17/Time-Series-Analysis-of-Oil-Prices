#!/usr/bin/python
# importing the required module 
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



#Cleaning data and storing into a data frame for individual csv file
def eachfile(name):
    try:
        df = pd.read_csv("downloaded_data/"+name+".csv")
        del df['Volume'] #dropping Volume column
        df["Date"] = pd.to_datetime(df['Date']) #converting string to a datetime
        #df= df[(df["Date"].dt.year >=2017-n)]  #deleting rows based on date column
        df = df.set_index('Date')
        df = df.dropna() # get rid of all the NAN rows.
        #print(df)
        return df
    except AttributeError:
        print("NoneType object has no attribute empty")
    except TypeError:
        print("Input is not a file name or last year")
    except FileNotFoundError:
       print("File not exist")

#eachfile("BP1.L")