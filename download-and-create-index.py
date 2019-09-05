#(C) Tsubasa Kato 2019 - 9/6/2019
import requests
import ssl
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
import shutil
#URL to download csv data (BTC / JPY 1 hour)
url = 'https://www.cryptodatadownload.com/cdd/Bitflyer_BTCJPY_1h.csv'

r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open("./csv1.csv", 'wb') as f:
        shutil.copyfileobj(r.raw, f)

next_num = 0
prev_num = 0
counter = 0
df = pd.read_csv('./csv1.csv',skiprows=1)
print (df.head())

modifier = ['High', 'Low']

limit = len(df.index)

csv_columns = {'Date':'2019-09-05 10-AM'}
#Outputs to csv2.csv
writer = csv.writer(open('./csv2.csv', 'w'))

date_header = 'Date'
high_header = 'High'
low_header = 'Low'
#These are for the index values created
index_header = 'Index'
index_header2 = 'Index2'

#date_header = date_header.encode()
#high_header = high_header.encode()
#low_header = low_header.encode()
#index_header = index_header.encode()

writer.writerow([date_header,high_header,low_header,index_header,index_header2])
while counter < limit - 1: 
	print (counter)
	if (counter > 1):
		next_num = counter + 1
		prev_num = counter - 1

		nextnum_val = pd.to_numeric(df.at[next_num, 'High'], errors='coerce').astype(np.int64)
		currentnum_val  = pd.to_numeric(df.at[counter, 'High'], errors='coerce').astype(np.int64)
		currentnum_val2 = pd.to_numeric(df.at[counter, 'Low'], errors='coerce').astype(np.int64)
		prevnum_val = pd.to_numeric(df.at[prev_num, 'High'], errors='coerce').astype(np.int64)

		current_date = df.at[counter, 'Date']
		#print(nextnum_val)
		#print(currentnum_val)
		#print(prevnum_val)

		if (nextnum_val < currentnum_val and prevnum_val < currentnum_val):
			writer.writerow([current_date,currentnum_val,currentnum_val2,currentnum_val,""])
			print ('Next: ')
			print (nextnum_val)
			print ('Current: ')
			print (currentnum_val)
			print ('Prev: ')
			print (prevnum_val)
			print('Found!\n')
		if (nextnum_val > currentnum_val and prevnum_val > currentnum_val):
			writer.writerow([current_date,currentnum_val,currentnum_val2,"",currentnum_val])
			print ('Next: ')
			print (nextnum_val)
			print ('Current: ')
			print (currentnum_val)
			print ('Prev: ')
			print (prevnum_val)
			print('Found!\n')
		else:

			writer.writerow([current_date,currentnum_val,currentnum_val2,"",""])
			#date = pd.to_numeric(df.at[counter, 'High'], errors='coerce').astype(np.int64)
			#data = pd.to_numeric(df.at[counter, 'High'], errors='coerce').astype(np.int64)
			#csv_columns.update({'Date'}:data)


	counter = counter + 1

os.system('python3 ./plot-to-chart.py')


