#import the libraries
from bokeh.plotting import figure, output_file, show
import pandas as pd
import numpy as np

#Taking start year and end year as input
sy = int(input("Enter Start Year:"))
ey = int(input("Enter End Year:"))

#Read the csv
root_folder = "./src/new_data"
df=pd.read_csv(root_folder+"/"+ "new.BP.L.csv" )
df = df[['Month', 'Year', 'High', 'Low']]
df = df[(df['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df['Year'].isin(np.arange(sy, ey, 1)))]

print(df)

root_folder = "./src/new_data"
df1=pd.read_csv(root_folder+"/"+"new.RDSB.L.csv" )
df1 = df1[['Month', 'Year', 'High', 'Low']]
df1 = df1[(df1['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df1['Year'].isin(np.arange(sy, ey, 1)))]
print(df1)

root_folder = "./src/new_data"
df2=pd.read_csv(root_folder+"/"+ "new.CNE.L.csv" )
df2 = df2[['Month', 'Year', 'High', 'Low']]
df2 = df2[(df2['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df2['Year'].isin(np.arange(sy, ey, 1)))]
print(df2)

root_folder = "./src/new_data"
df3=pd.read_csv(root_folder+"/"+"new.PMO.L.csv" )
df3 = df3[['Month', 'Year', 'High', 'Low']]
df3 = df3[(df3['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df3['Year'].isin(np.arange(sy, ey, 1)))]
print(df3)

#Plotting Part
p=figure(width=1500, height=750, title= "Dot Plot of the Average Share Price for British Petroleum (BP), Shell (RDSB), Cairn Energy (CNE) and Premier Oil (PMO)",
title_location = 'above')

p.circle(df["Year"], df['High'].add(df['Low']) / 2, color="red", alpha=0.5)

p.circle(df1["Year"], df1['High'].add(df1['Low']) / 2, color="blue", alpha=0.5)

p.circle(df2["Year"], df2['High'].add(df2['Low']) / 2, color="green", alpha=0.5)

p.circle(df3["Year"], df3['High'].add(df3['Low']) / 2, color="yellow", alpha=0.5)

# Add titles
p.xaxis.axis_label= "Years"
p.yaxis.axis_label= "Average Price"
output_file("./plots/dot_plot.html")
show(p)