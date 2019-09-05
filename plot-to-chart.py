import requests
import ssl
import shutil
import numpy as np
import pandas as pd2
import matplotlib.pyplot as plt
import numpy.ma as ma

df2 = pd2.read_csv('csv3.csv',skiprows=0)


#print(len(df2))

#xs = np.arange(len(df2))
xs = np.arange(168)
xs2 = np.arange(168)
xs3 = np.arange(168)

series0 = df2['Index2'].iloc[:168].astype(np.double)
s0mask = np.isfinite(series0)

series1 = df2['Index'].iloc[:168].astype(np.double)
s1mask = np.isfinite(series1)

series2 = df2['High'].iloc[:168].astype(np.double)
s2mask = np.isfinite(series2)

series3 = df2['Low'].iloc[:168].astype(np.double)
s3mask = np.isfinite(series3)


plt.plot(xs[s0mask], series0[s0mask], linestyle='-', marker='o', c="purple")
plt.plot(xs[s1mask], series1[s1mask], linestyle='-', marker='o', c="blue")
plt.plot(xs[s2mask], series2[s2mask], linestyle='--', marker='.', c="green")
plt.plot(xs[s3mask], series3[s3mask], linestyle='-', marker='.', c="red")
#plt.plot(xs[s3mask], series3[s3mask], linestyle='-', marker='o')
#print (df2.head())
#I think the dataframe should be limited.
#index = ma.masked_where(np.isnan(df2['Index'].iloc[:168]),df2['Index'].iloc[:168])

#print(index)
#df2.reindex(new_idx, fill_value=np.nan)
#print(df2['Date'])
#plt.plot(df2['Date'].iloc[:168],df2['High'].iloc[:168],linestyle='-',marker=".",c="green")
#plt.plot(df2['Date'].iloc[:168],df2['Low'].iloc[:168],linestyle='-',marker=".",c="blue")
#plt.plot(df2['Date'].iloc[:168],df2['Index'].iloc[:168],linestyle='-',marker=".",c="red")
plt.show()         # which is the result of opening req
