# Time Series Analysis of Oil Prices

In this project, we are working with the oil price dataset to analyse the prices of oil with respect to time and also the stock prices of different companies like Shell, British Petroleum, Cairn Energy and Premier Oil. Since machine learning has been widely used in Oil and Gas sector, and the economy of a country is greatly affected by its oil prices, therefore we have chosen this dataset to work with.

### Prerequisites

Make sure you have Python 3 and pipenv installed.
To install pipenv, run:

    $pip install pipenv

## Getting Started

1.  Activate the virtual environment and the shell:

    ```
    $pipenv shell

    ```

2.  Since we are using Kaggle dataset and API, install kaggle by executing:

    ```    
    $pipenv install kaggle                  #it has been added to pipfile but still doesn't get tracked. So, make sure to install it.

    ```
3. To run the project:

    ```
    $make
    
    ```

   This command will execute the Makefile in the order - clean, download, processData, plotting, tests.
 

##### To run the project through Makefile:

```
# To call the Makefile and execute all:
$ make 

# to remove the downloaded data, processed data and other generated files (png and html):
$ make clean

# to download the data and generate histogram of numerical attributes in dataset:
$ make download    

# to clean the downloaded data and generate cleaned csv files:
$ make processData

# to generate plots:
$ make plotting

# to execute different test cases through test suite:
$ make tests

```

### Download the data

```
$python .src/download.py -d time-series-analysis-of-oil-prices -c Date Open High Low Close Adj Close Volume

```
    
    -d represents the name of the dataset.

    -c represents the column names in the csv files.


-   This command should create a folder named downloaded_data with all the unzipped csv files. It will  print the top rows and columns of the selected csv files:

    Shell (RDSB.L.csv)

    British Petroleum (BP.L.csv)
    
    Cairn Energy (CNE.L.csv)

    Premier Oil (PMO.L.csv) 
    
-   To analyse the dataset, a histogram of all the numerical attributes is generated using matplotlib.pyplot.

### Clean the data

```
$python ./src/cleanData.py                      # run this from root folder

```

-   This command will clean the xml and csv files and will store the data in a main data frame called all_data.
-   It will also generate new cleaned csv files with two additional fields - Year and Month.

```
$python ./src/plotting.py                      # optional (not used for plotting)

```

-   plotting.py imports the module from cleanData.py file. This file can be used to generate clean dataFrame for individual csv files. 
-   We can also generate the shrink data by specifying the value for 'last' and 'year' (last 5 years data)
-   Arguments like 'all' or 'brate' can be passed with data function:

    ```
    -   cleandata("all")    :   for getting the combined dataframe
    -   cleandata("brate")  :   for getting the oil prices

    ```

### Plotting

```
$python ./src/dot_plot.py                     

```

-   This file will generate the bokeh html dot plot for the average share price of four companies namely British Petroleum (BP), Shell (RDSB), Premier Oil (PMO) and Cairn Energy (CNE) and will save the generated html in plots folder

```
$python ./src/box_plot.py                             

```

-   This file will generate a box plot for the average share price for British Petroleum (BP) for the year 2015. It will save the generated png file in plots folder.


```
$python ./src/Bar_Chart.py                             

```

-   This file will generate the bokeh bar chart as html for the average share price for the company British Petroleum (BP), Cairn Energy (CNE) and Premier Oil (PMO) for the years 2015, 2016 and 2017. It will save the generated html file in plots folder


```
$python ./src/histogram.py                             

```

-   This file will generate a histogram for the highest oil price (y-axis) according to time period (x-axis) for the company British Petroleum (BP). It will save the generated png file in plots folder.

```
$python ./src/swarm_plot.py                             

```

-   This file will generate a swarm plot depicting the average share price for the year 2015 for the company British Petroleum (BP). The Month is plotted on x-axis while the Average Share Price is on y-axis. The generated png will be saved in the plots folder.

```
$python ./src/pie_chart.py                             

```

-   This file will generate a pie chart for the highest share price for the company Premier Oil (PMO). It will save the generated png file in plots folder.

## Test suite

```
$py.test ./src/test_all_cases.py                     

```

-   This file will execute test suite and report the test execution status.

##  Contributors

Group 5

*   Aafia Jabeen

    pipenv, Makefile, Download the Data, Histogram depicting numerical attributes of Cairn Energy (CNE), ReadMe, Report, Presentation

*   Rabeya Akhter

    Clean the data, Test suite, Report, Presentation, ReadMe

*   Shiplu Das

    Report, Analysis and Plotting - Dot plot (Bokeh), Box plot, Swarm Plot, Bar Chart (Bokeh), Histogram (British Petroleum), Pie Chart
    
*   Sanusi Musa

    Plotting - Pie Chart