#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 16:55:30 2017

@author: yi.yan
"""

import pickle
import numpy as np 
import matplotlib.pyplot as plt

f = open('Batch1-4Attrib.pckl', 'rb')
lMetaData = pickle.load(f)
f.close()

lBioSample = [j[0] for j in lMetaData]
UniqueBioSample = set(lBioSample)
lNumAttrib = []

for biosample in UniqueBioSample:
    lNumAttrib.append(lBioSample.count(biosample))

fig = plt.figure()
plt.hist(lNumAttrib)
plt.xlabel('Number of Metadata Term')
plt.ylabel('Percentile')
plt.title('Batch 1-4 Distribution of Number of Meta Data Terms')
 
fig.savefig('MetaDataCountDistributionBatch1-4.png')  

lAttribs = [j[1][0] for j in lMetaData]

f = open('Batch1-4AttribDistribution.txt','w')
for temp in lAttribs:
    f.write(temp + '\n')
f.close()

f = open('Batch1-4AttribDistributionDetailed.txt','w')
for temp in lMetaData:
    f.write(temp[1][0] + '\t' + temp[2][0]+'\n')
f.close()

lUniqueAttribs = set(lAttribs)
lNumAttrib = []

for biosample in UniqueBioSample:
    lNumAttrib.append(lBioSample.count(biosample))