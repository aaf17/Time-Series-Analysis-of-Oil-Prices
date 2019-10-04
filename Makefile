# Makefile to process datafile

# Source folder path from root directory
path = ./src/
d = ./src/downloaded_data
processed_data	=	./src/new_data


# Provide the arguments for argparse to download the data
dataset = -d 'time-series-analysis-of-oil-prices'
columns = -c 'Date Open High Low Close Adj Close Volume'


# executing test suite (using the Python Assert statement)
tests    :    clean  download   processData   plotting
	py.test $(path)test_all_cases.py


#plotting will execute the various plot files and will save the images in the plots folder
plotting	:	clean	download	processData
	python $(path)dot_plot.py
	python $(path)box_plot.py
	python $(path)histogram.py
	python $(path)Bar_Chart.py
	python $(path)pie_chart.py
	python $(path)swarm_plot.py


#download will create the folder downloaded_data and will download the data from Kaggle automatically using the Kaggle API(requests library)
#argparse is used to set the desired dataset name and column names 
download : clean	#prequisite for download
	python $(path)download.py $(dataset) $(columns)


#this command will execute cleanData.py and plotting.py
#cleanData.py will clean the xml and csv files and will create a main dataFrame
#plotting.py gets the cleaned data from cleanData.py and is further used for plotting.
processData	:	clean	download
	python	$(path)cleanData.py


#to specify that make shouldnot expect a file named clean
.PHONY	:	clean


#this command will remove the already downloaded data, processed or cleaned data and .png files
clean:
	rm -rf $(d)
	rm	-rf	./plots/*.png
	rm	-rf	./plots/*.html
	rm -rf $(processed_data)
