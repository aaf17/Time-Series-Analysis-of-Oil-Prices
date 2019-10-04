#importing the required libraries
import os, kaggle, requests, argparse, sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#using Kaggle username and token to connect to Kaggle API (using the requests library)
os.environ['KAGGLE_USERNAME'] = "aafia17"
os.environ['KAGGLE_KEY'] = "f4be31ef1046c27c8ca104372e18df14"

#argument parser for parsing to download the data
ap = argparse.ArgumentParser()
ap.add_argument('-d', metavar='D', help='Dataset Name')
ap.add_argument('-c', metavar='C', help='Columns', type=str, nargs='+')

#function to automatically download the data using Kaggle API (requests library)
def DownloadDataset(dataset):
   kaggle.api.dataset_download_files(
    "javierbravo/oil-price-and-share-price-of-a-few-companies", "./src/downloaded_data", unzip=True)

if __name__ == "__main__":
  args = ap.parse_args()

  root_folder = "./src/downloaded_data"
  default_dataset = "time-series-analysis-of-oil-prices"
  DownloadDataset("/javierbravo/oil-price-and-share-price-of-a-few-companies")
  columns = "Date Open High Low Close Adj Close Volume".split(" ")
  bp_rawData_df = pd.read_csv( root_folder+"/"+ "BP.L.csv" )
  df = pd.read_csv( root_folder+"/"+ "CNE.L.csv" )
  shell_rawData_df = pd.read_csv( root_folder+"/"+ "RDSB.L.csv" )
  pmo_rawData_df = pd.read_csv( root_folder+"/"+ "PMO.L.csv" )

  print(bp_rawData_df.head())
  print(df.head())
  print(shell_rawData_df.head())
  print(pmo_rawData_df.head())

  if args.d:
    default_dataset = args.d
    print("\nChanging the dataset: ", args.d)
  if args.c:
    columns = args.c
    print("\nChanging the column name: ", args.c)

  print("\n{} Downloading the dataset: {} from Kaggle to the folder:{}".format(sys.argv[0], default_dataset, root_folder))

#Plotting histogram for each numerical attribute to understand the type of data 
print("Plotting histogram for each numerical attribute to understand the type of data")

plt.suptitle("Histogram depicting the columns for Cairn Energy (CNE)")
plt.subplot(2, 3, 1)
plt.hist(df['Open'])
plt.xticks([])
plt.title("Open")

plt.subplot(2, 3, 2)
plt.hist(df['Close'])
plt.xticks([])
plt.title("Close")

plt.subplot(2, 3, 3)
plt.hist(df['High'])
plt.xticks([])
plt.title("High")

plt.subplot(2, 3, 4)
plt.hist(df['Low'])
plt.xticks([])
plt.title("Low")

plt.subplot(2, 3, 5)
plt.hist(df['Adj Close'])
plt.xticks([])
plt.title("Adj Close")

plt.subplot(2, 3, 6)
plt.hist(df['Volume'])
plt.xticks([])
plt.title("Volume")

plt.savefig("./plots/histogram_columns_cne.png", format="png") 
plt.show(block = False)
plt.pause(8)
