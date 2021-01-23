import csv
import os
import glob
import pandas as pd

path = 'examples-data//financial-data//'
file_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_dir, path)

for filename in os.listdir(file_path):
        if filename.endswith(".csv") : #or filename.endswith(".py"): 
         # print(os.path.join(directory, filename))
            reader = csv.reader(filename)
            lines= len(list(reader))
            print(filename)
            print(lines)
            continue
        else:
            continue

"""
files = glob.glob(file_path +'/*.csv')
d = {f: rawincount(f) for f in files}
df = pd.Series(d).to_frame('rows')

df = pd.DataFrame(columns=(file_path, 'rows'))
for index,i in enumerate(os.listdir('.')):
    df.loc[index] = [i,len(pd.read_csv(i).index)]
"""
"""
print(file_dir)

with open(file_dir) as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        pass
    print(csv_reader.line_num)




files = glob.glob('files/*.csv')

d = {f: sum(1 for line in open(f)) for f in files}

print (pd.Series(d))

print (pd.Series(d).rename('rows').rename_axis('filename').reset_index())
"""