#imported libraries
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv
root_folder = "./src/new_data"
df=pd.read_csv(root_folder+"/"+ "new.BP.L.csv")

#Plotting Part
df = df.set_index('Date')
df.sort_index(inplace=True)
df['High'].plot()
plt.title("Histogram of the Highest Price for British Petroleum (BP)")
plt.ylabel('Highest Price')

#save the figure in plots folder and show it
plt.savefig("./plots/histogram_bp.png", format="png")
plt.show(block=False)
plt.pause(8)