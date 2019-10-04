#imported libraries
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
import pandas as pd

#save the output html file in plots folder
output_file("./plots/bar_chart.html")

#selected the companies and year
company = ['BP.L', 'CNE.L', 'PMO.L']
years = ['2015', '2016', '2017']

#defining root folder for cleaned csv files
root_folder = "./src/new_data"

###################################    BP.L    #################################

df=pd.read_csv(root_folder+"/"+ "new.BP.L.csv" )
df = df[['Month', 'Year', 'High', 'Low']]
df = df[(df['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df['Year']==2015)]
b5= df['High'].add(df['Low']) / 2
bp5= sum(b5)/len(df)

df1 = pd.read_csv(root_folder+"/"+ "new.BP.L.csv")
df1 = df1[['Month', 'Year', 'High', 'Low']]
df1 = df1[(df1['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df1['Year']==2016)]
b6= df1['High'].add(df1['Low']) / 2
bp6= sum(b6)/len(df1)

df2 = pd.read_csv(root_folder+"/"+ "new.BP.L.csv")
df2 = df2[['Month', 'Year', 'High', 'Low']]
df2 = df2[(df2['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df2['Year']==2017)]
b7= df2['High'].add(df2['Low']) / 2
bp7= sum(b7)/len(df2)

###################################    CNE.L    #################################

df3 = pd.read_csv(root_folder +"/"+ "new.CNE.L.csv")
df3 = df3[['Month', 'Year', 'High', 'Low']]
df3 = df3[(df3['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df3['Year']==2015)]
c5= df3['High'].add(df3['Low']) / 2
cn5= sum(c5)/len(df)

df4 = pd.read_csv(root_folder +"/"+ "new.CNE.L.csv")
df4 = df4[['Month', 'Year', 'High', 'Low']]
df4 = df4[(df4['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df4['Year']==2016)]
c6= df4['High'].add(df4['Low']) / 2
cn6= sum(c6)/len(df4)

df5 = pd.read_csv(root_folder +"/"+ "new.CNE.L.csv")
df5 = df5[['Month', 'Year', 'High', 'Low']]
df5 = df5[(df5['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df5['Year']==2017)]
c7= df5['High'].add(df5['Low']) / 2
cn7= sum(c7)/len(df5)

###############################    PMO.L    ####################################

df6 = pd.read_csv(root_folder +"/"+ "new.PMO.L.csv")
df6 = df6[['Month', 'Year', 'High', 'Low']]
df6 = df6[(df6['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df6['Year']==2015)]
p5= df6['High'].add(df6['Low']) / 2
pm5= sum(p5)/len(df6)

df7 = pd.read_csv(root_folder +"/"+ "new.PMO.L.csv")
df7 = df7[['Month', 'Year', 'High', 'Low']]
df7 = df7[(df7['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df7['Year']==2016)]
p6= df7['High'].add(df7['Low']) / 2
pm6= sum(p6)/len(df7)

df8 = pd.read_csv(root_folder +"/"+ "new.PMO.L.csv")
df8 = df8[['Month', 'Year', 'High', 'Low']]
df8 = df8[(df8['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df8['Year']==2017)]
p7= df8['High'].add(df8['Low']) / 2
pm7= sum(p7)/len(df8)

##################################    Plot    ######################################

data = {'company' : company,
        '2015'   : [bp5, cn5, pm5],
        '2016'   : [bp6, cn6, pm6],
        '2017'   : [bp7, cn7, pm7]}

source = ColumnDataSource(data=data)

p = figure(x_range=company, y_range=(0, 600), plot_height=350, plot_width = 900, 
title="Average Share Price for British Petroleum (BP), Cairn Energy (CNE) and Premier Oil (PMO) for the year 2015, 2016 and 2017",
toolbar_location=None)

p.vbar(x=dodge('company', -0.25, range=p.x_range), top='2015', width=0.2, source=source,
       color="#c9d9d3", legend=value("2015"))

p.vbar(x=dodge('company',  0.0,  range=p.x_range), top='2016', width=0.2, source=source,
       color="#718dbf", legend=value("2016"))

p.vbar(x=dodge('company',  0.25, range=p.x_range), top='2017', width=0.2, source=source,
       color="#e84d60", legend=value("2017"))

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
show(p)