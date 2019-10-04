import os
import sys

#Function part to test box_plot figure is in plot folder
def checkIm1():
    try: 
        if os.path.isfile('./plots/box_plot.png'):
            return True
    except Exception as e:
        print(e)

#Function part to test new.BP.L.csv file is in new_data folder
def checkcsv1():
    try: 
        if os.path.isfile('./src/new_data/new.BP.L.csv'):
            return True
    except Exception as e:
        print(e)

#Function part to test new.CNE.L.csv file is in new_data folder
def checkcsv2():
    try: 
        if os.path.isfile('./src/new_data/new.CNE.L.csv'):
            return True
    except Exception as e:
        print(e)

#Function part to test new.PMO.L.csv file is in new_data folder
def checkcsv3():
    try: 
        if os.path.isfile('./src/new_data/new.PMO.L.csv'):
            return True
    except Exception as e:
        print(e)

#Function part to test new.RDSB.L.csv file is in new_data folder
def checkcsv4():
    try: 
        if os.path.isfile('./src/new_data/new.RDSB.L.csv'):
            return True
    except Exception as e:
        print(e)

#Function part to test download_data folder is not empty
def download_data():
    try: 
        if any(os.scandir('./src/downloaded_data')):
            return True
    except Exception as e:
        print(e)


print("testing completed successfully")
#Execution Part
def test_checkIm1():
    assert checkIm1() == True

def test_checkcsv1():
    assert checkcsv1() == True

def test_checkcsv2():
    assert checkcsv2() == True

def test_checkcsv3():
    assert checkcsv3() == True

def test_checkcsv4():
    assert checkcsv4() == True

def test_download_data():
    assert download_data() == True
