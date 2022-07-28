##import csv

#with open('sample.csv')as fp:
   # reader = csv.reader(fp)
   # headers = next(reader)        # The header row is now consumed
   # ncol = len(headers)
   # nrow = sum(1 for _ in reader) # What remains are the data rows


## pip install pandas
##from pathlib import Path
#import pandas as pd
#attnd_path = Path('..') / 'datasets' / 'sample.csv'
#attnd = pd.read_csv(attnd_path)
#print(attnd.head())


import pandas as pd

df = pd.read_csv('sample.csv')

print(df) 