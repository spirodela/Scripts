#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:18:35 2017

@author: yi.yan
"""
import xlrd
import matplotlib.pyplot as plt
import numpy as np 

sFile = '/Users/yi.yan/Documents/Data/FDA_ARGOS_Metadata.xlsx' 
strucBook = xlrd.open_workbook(sFile)
strucSheet = strucBook.sheet_by_index(0)

lMetaData = strucSheet.row_values(0)
lNumMetaData = [] 

numSample = strucSheet.nrows - 1 
numMetaData = strucSheet.ncols

for i in range(1,strucSheet.nrows):
    lRow = strucSheet.row_values(i)
    nMetaData = numMetaData - lRow.count('missing') - lRow.count('') \
                - lRow.count('Missing') - lRow.count('Not Applicable') \
                - lRow.count('not applicable') - lRow.count('Unknown') - lRow.count('unknown')
    lNumMetaData.append(nMetaData)

fig = plt.figure()
plt.hist(lNumMetaData)
plt.xlabel('Number of Metadata Term Associated with Sample')
plt.ylabel('Number of Samples')
plt.title('Distribution of Number of Metadata Terms Associated With Samples')

fig.savefig('/Users/yi.yan/Documents/Image/FDAARGOSMetaDataNumber.png',format='png', dpi=1200,bbox_inches='tight')  

####Top 25 percentile metadata terms 

lMetaDataPercentile = [] 
for i in range(0,strucSheet.ncols):
    lCol = strucSheet.col_values(i)
    P = numSample - lCol.count('missing') - lCol.count('') \
                - lCol.count('Missing') - lCol.count('Not Applicable') \
                - lCol.count('not applicable') - lCol.count('Unknown') - lCol.count('unknown')
    lMetaDataPercentile.append(P/numSample)



x = np.array(lMetaDataPercentile) 
idx = np.argsort(x)
idx = list(reversed(idx))

sortedMetaData = [lMetaData[j] for j in idx]
Percentile = x[idx]
    
n = 19 

tempCategories = sortedMetaData[0:n]
tempCategories = list(reversed(tempCategories))
tempPercentile = Percentile[0:n]
tempPercentile = list(reversed(tempPercentile))

y_pos = np.arange(len(tempCategories))

fig = plt.figure()
plt.barh(y_pos, tempPercentile, align='center', alpha=0.5)
plt.yticks(y_pos, tempCategories)
plt.xlabel('Percent Metadata Coverage')
plt.title('Top Metadata Coverage')
 
fig.savefig('/Users/yi.yan/Documents/Image/Top20FDAARGOSMetaDataCoverage.png',format='png',dpi=1200,bbox_inches='tight')

wFile = open('/Users/yi.yan/Documents/Data/ARGOSKronaInput.txt','w')

lMissing = ['missing','','Missing',
            'Not Applicable','not applicable','Unknown','unknown']

for i in range(0,strucSheet.ncols):
    for j in range(1,strucSheet.nrows):
        if strucSheet.cell(j,i).value not in lMissing:
            temp = strucSheet.cell(j,i).value
            if type(temp) != str :
                temp = str(temp)
            string = lMetaData[i] + '\t' + temp + '\n'
            string = string.encode('ascii', 'ignore').decode('ascii')
            wFile.write(string)

wFile.close()