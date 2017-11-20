#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:00:14 2017

@author: yi.yan
"""

import pickle
import numpy as np 
import matplotlib.pyplot as plt

f = open('NCBIProkGenomeAttribBatch2.pckl', 'rb')
lMetaData = pickle.load(f)
f.close()

lBioSample = [j[0] for j in lMetaData]
UniqueBioSample = set(lBioSample)
lNumAttrib = []

for biosample in UniqueBioSample:
    lNumAttrib.append(lBioSample.count(biosample))

fig = plt.figure()
plt.hist(lNumAttrib,bins = 51,range=(0,50))
plt.xlabel('Number of Metadata Term')
plt.ylabel('Count')
plt.title('NCBI Distribution of Number of Meta Data Terms')
 
fig.savefig('MetaDataCountDistributionNCBISmaller50.png')  

fig = plt.figure()
plt.hist(lNumAttrib,bins = 100)
plt.xlabel('Number of Metadata Term')
plt.ylabel('Count')
plt.title('NCBI Distribution of Number of Meta Data Terms')
 
fig.savefig('MetaDataCountDistributionNCBI.png')  

f = open('NCBIAttribDistributionDetailed.txt','w')
for temp in lMetaData:
    f.write(temp[1][0] + '\t' + temp[2][0]+'\n')
f.close()

f = open('NCBIAttribDistribution.txt','w')
for temp in lMetaData:
    f.write(temp[1][0] + '\n')
f.close()

lAttribs = [j[1][0] for j in lMetaData]

uAttribs = set(lAttribs)

cAttribs = [] 

for temp in uAttribs :
    cAttribs.append(lAttribs.count(temp))
    
PercentileCAttribs = [j*100/len(UniqueBioSample) for j in cAttribs]   

x = np.array(PercentileCAttribs) 
idx = np.argsort(x)
idx = list(reversed(idx))

sCategories = [list(uAttribs)[j] for j in idx]
Percentile = x[idx]

y_pos = np.arange(len(sCategories))

fig = plt.figure()
plt.bar(y_pos, Percentile, align='center', alpha=0.5)
plt.ylabel('Percentile')
plt.title('Accension Distribution')
 
fig.savefig('AttributePercentile.png')

n = 24 
tempCategories = sCategories[0:n]
tempCategories = list(reversed(tempCategories))
tempPercentile = Percentile[0:n]
tempPercentile = list(reversed(tempPercentile))

y_pos = np.arange(len(tempCategories))

fig = plt.figure()
plt.barh(y_pos, tempPercentile, align='center', alpha=0.5)
plt.yticks(y_pos, tempCategories)
plt.xlabel('Percentile')
plt.title('Accension Distribution')
 
fig.savefig('AttributePercentileTop25.png')

f = open('NCBITop25AttribDistributionDetailed.txt','w')
for temp in lMetaData:
    for stuff in tempCategories:
        if temp[1][0] == stuff:
            f.write(temp[1][0] + '\t' + temp[2][0]+'\n')
f.close()

n = 49 
tempCategories = sCategories[0:n]
tempCategories = list(reversed(tempCategories))
tempPercentile = Percentile[0:n]
tempPercentile = list(reversed(tempPercentile))

y_pos = np.arange(len(tempCategories))

fig = plt.figure()
plt.barh(y_pos, tempPercentile, align='center', alpha=0.5)
plt.yticks(y_pos, tempCategories)
plt.xlabel('Percentile')
plt.title('Accension Distribution')
 
fig.savefig('AttributePercentileTop50.png')

f = open('NCBITop50AttribDistributionDetailed.txt','w')
for temp in lMetaData:
    for stuff in tempCategories:
        if temp[1][0] == stuff:
            f.write(temp[1][0] + '\t' + temp[2][0]+'\n')
f.close()