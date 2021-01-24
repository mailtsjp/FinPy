import csv
import os
import glob
import pandas as pd

path = './examples-data/financial-data'
file_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_dir, path)

"""
file_path = os.path.join(path)
result = [i for i in glob.glob('*.{}'.format("csv"))]

for fn in glob.glob('*.csv'):

#for filename in os.listdir(file_dir):
    with open(fn, 'r') as fileObj:
     print("Rows Counted {} in the csv {}:".format(len(fileObj.readlines()) - 1, filename))  
  """

  #get current working dir, set count, and select file delimiter
os.chdir(path)

#parses through files and saves to a dict
series={}
for fn in glob.glob('*.csv'):
    with open(fn) as f:
        series[fn]=sum(1 for line in f if line.strip() and not line.startswith('#'))    

print(series)

#save the dictionary with key/val pairs to a csv
with open('seriescount.csv', 'wb') as f: 
    w = csv.DictWriter(f, series)
    #f.close()
