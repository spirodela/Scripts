#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:42:48 2017

@author: yi.yan
"""

import xlrd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from Bio import Entrez
Entrez.email = "yi.yan@hhs.fda.gov"

sFileName = '/Users/yi.yan/Documents/FDA-ARGOS/Accessions_batch1-4.xlsx'
workbook = xlrd.open_workbook(sFileName)
worksheet = workbook.sheet_by_index(0)

lCategory = []

for i in range(1,worksheet.nrows):
    n1 = 0 
    temp = worksheet.cell(i,3).value 
    if temp != '':
        n1 = len(temp.split())
    n2 = 0 
    temp = worksheet.cell(i,4).value 
    if temp != '':
        n2 = len(temp.split())
    n3 = 0 
    temp = worksheet.cell(i,5).value 
    if temp != '':
        n3 = len(temp.split())
    lCategory.append((n1,n2,n3))    

nRecord = worksheet.nrows - 1 
nCh = [temp[0] for temp in lCategory]
nPL = [temp[1] for temp in lCategory]
nWGS = [temp[2] for temp in lCategory]

sCategories = ['Chr Accession', 'Plasmid Accession', 'WGS']
Percentile = [sum(nCh)*100/nRecord, sum(nPL)*100/nRecord, sum(nWGS)*100/nRecord]

y_pos = np.arange(len(sCategories))

fig = plt.figure()
plt.bar(y_pos, Percentile, align='center', alpha=0.5)
plt.xticks(y_pos, sCategories)
plt.ylabel('Percentile')
plt.title('Accension Distribution')
 
fig.savefig('Accension_DIstribution.png')