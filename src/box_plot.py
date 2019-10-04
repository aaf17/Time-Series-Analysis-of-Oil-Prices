#import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the csv files
root_folder = "./src/new_data"
df=pd.read_csv(root_folder+"/"+ "new.BP.L.csv")
df = df[['Month', 'Year', 'High', 'Low']]

y= df['High'].add(df['Low']) / 2

df = df[(df['Month'].isin([1,2,3,4,5,6,7,8,9,10,11,12]))&(df['Year']==2015)]
print(df)

x='Month'
z= 2015

# style
plt.style.use('seaborn-darkgrid')

# Add titles
plt.title("Box Plot for British Petroleum (BP) of the Average Share Price for the year {}".format(z), 
loc='center', fontsize=16, fontweight=0, color='black')
plt.xlabel('Years')
plt.ylabel('Average Price')
plt.legend(loc='lower right')

ax = sns.boxplot(x=x, y=y, data=df)
#ax = sns.swarmplot(x=x, y=y, data=df, color = "grey")
plt.savefig("./plots/box_plot.png", format="png")
plt.show(block=False)
plt.pause(8)