#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:30:34 2017

@author: yi.yan
"""

import xlrd
import os 
import matplotlib.pyplot as plt
import numpy as np

sDir  = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Sample/BlastCountResult/'  
sLabel = 'Sample' 

lFiles = os.listdir(sDir)
numFile = 0
lNumHit = [] 
lSigSpecies = []
lFoldChange = []; 
for filename in lFiles :
    if filename[-12:] == 'Summary.xlsx' :
        numFile = numFile + 1 
        sFile = sDir + filename
        bookSummary = xlrd.open_workbook(sFile)
        sheetSummary = bookSummary.sheet_by_index(0) 
        rowVal = sheetSummary.row_values(1)
        numHit = [rowVal[5],rowVal[12],rowVal[-2]]
        lNumHit.append(numHit)
        Pval = sheetSummary.col_values(18)
        Pval[0] = 1
        for i in range(0,len(Pval)):
            if Pval[i] == '' :
                Pval[i] = 1
                
        idx = [i for i,x in enumerate(Pval) if float(x) <= 0.05]
        Species = sheetSummary.col_values(15)
        numNT = sheetSummary.col_values(16)
        numARGOS = sheetSummary.col_values(17)
        for i in idx :
            FoldChange = float(numNT[i])/float(numARGOS[i])
            lFoldChange.append(FoldChange)
            lSigSpecies.append(Species[i])


data = np.array(lNumHit)
fig = plt.figure()
plt.boxplot(data)
plt.xlabel('Database Used')
plt.ylabel('Number of Megablast Hit')
plt.xticks([1,2,3],['nt','nt-ARGOS','ARGOS'])
plt.title(sLabel)
fig.savefig('/Users/yi.yan/Documents/Image/' + sLabel + 'Hits.png',format='png', dpi=1200,bbox_inches='tight')         
        
uSpecies = list(set(lSigSpecies))

lCoverage = [] 
for species in uSpecies :
    lCoverage.append(lSigSpecies.count(species)/numFile)

x = np.array(lCoverage) 
idx = np.argsort(x)
idx = list(reversed(idx))

sortedMetaData = [uSpecies[j] for j in idx]
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
plt.xlabel('Percent Output Coverage')
plt.title('Top Significantly different species')
 
fig.savefig('/Users/yi.yan/Documents/Image/'+sLabel+'SigSpecies.png',format='png',dpi=1200,bbox_inches='tight')

lLogFoldChange = [] 
for species in uSpecies :
    idx = [i for i,x in enumerate(lSigSpecies) if x == species]
    temp = []
    for i in idx :
        temp.append(np.log(lFoldChange[i]))
    lLogFoldChange.append(temp)

lSortedLFC = [] 
lSortedLFCMean = []
lName = []
n = 19 

lCoverage = [] 
for species in uSpecies :
    lCoverage.append(lSigSpecies.count(species)/numFile)

x = np.array(lCoverage) 
idx = np.argsort(x)
idx = list(reversed(idx))

for i in range(0,n):
    lSortedLFC.append(lLogFoldChange[idx[i]])   
    lSortedLFCMean.append(np.mean(lLogFoldChange[idx[i]]))
    lName.append(uSpecies[idx[i]])

x = np.array(lSortedLFCMean)
idx = np.argsort(x)
idx = list(reversed(idx))

fig = plt.figure()
Data =[lSortedLFC[i] for i in idx]
Name = [lName[i] for i in idx]
plt.boxplot(Data,vert=0)
plt.xlabel('log(Fold Change)')
plt.yticks(list(range(1,20)),Name)

fig.savefig('/Users/yi.yan/Documents/Image/'+sLabel+'SigSpeciesMagnitude.png',format='png',dpi=1200,bbox_inches='tight')
  
sDir  = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/MockClinical/BlastCountResult/'  
sLabel = 'MockClinical' 

lFiles = os.listdir(sDir)
numFile = 0
lNumHit = [] 
lSigSpecies = [] 
lFoldChange = []
for filename in lFiles :
    if filename[-12:] == 'Summary.xlsx' :
        numFile = numFile + 1 
        sFile = sDir + filename
        bookSummary = xlrd.open_workbook(sFile)
        sheetSummary = bookSummary.sheet_by_index(0) 
        rowVal = sheetSummary.row_values(1)
        numHit = [rowVal[5],rowVal[12],rowVal[-2]]
        lNumHit.append(numHit)
        Pval = sheetSummary.col_values(18)
        Pval[0] = 1
        for i in range(0,len(Pval)):
            if Pval[i] == '' :
                Pval[i] = 1
                
        idx = [i for i,x in enumerate(Pval) if float(x) <= 0.05]
        Species = sheetSummary.col_values(15)
        numNT = sheetSummary.col_values(16)
        numARGOS = sheetSummary.col_values(17)
        for i in idx :
            FoldChange = float(numNT[i])/float(numARGOS[i])
            lFoldChange.append(FoldChange)
            lSigSpecies.append(Species[i])


data = np.array(lNumHit)
fig = plt.figure()
plt.boxplot(data)
plt.xlabel('Database Used')
plt.ylabel('Number of Megablast Hit')
plt.xticks([1,2,3],['nt','nt-ARGOS','ARGOS'])
plt.title(sLabel)
fig.savefig('/Users/yi.yan/Documents/Image/' + sLabel + 'Hits.png',format='png', dpi=1200,bbox_inches='tight')         
        
uSpecies = list(set(lSigSpecies))

lCoverage = [] 
for species in uSpecies :
    lCoverage.append(lSigSpecies.count(species)/numFile)

x = np.array(lCoverage) 
idx = np.argsort(x)
idx = list(reversed(idx))

sortedMetaData = [uSpecies[j] for j in idx]
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
plt.xlabel('Percent Output Coverage')
plt.title('Top Significantly different species')
 
fig.savefig('/Users/yi.yan/Documents/Image/'+sLabel+'SigSpecies.png',format='png',dpi=1200,bbox_inches='tight')

lLogFoldChange = [] 
for species in uSpecies :
    idx = [i for i,x in enumerate(lSigSpecies) if x == species]
    temp = []
    for i in idx :
        temp.append(np.log(lFoldChange[i]))
    lLogFoldChange.append(temp)

lSortedLFC = [] 
lSortedLFCMean = []
lName = []
n = 19 

lCoverage = [] 
for species in uSpecies :
    lCoverage.append(lSigSpecies.count(species)/numFile)

x = np.array(lCoverage) 
idx = np.argsort(x)
idx = list(reversed(idx))

if n > len(lLogFoldChange):
    n = len(lLogFoldChange)
for i in range(0,n):
    lSortedLFC.append(lLogFoldChange[idx[i]])   
    lSortedLFCMean.append(np.mean(lLogFoldChange[idx[i]]))
    lName.append(uSpecies[idx[i]])

x = np.array(lSortedLFCMean)
idx = np.argsort(x)
idx = list(reversed(idx))

fig = plt.figure()
Data =[lSortedLFC[i] for i in idx]
Name = [lName[i] for i in idx]
plt.boxplot(Data,vert=0)
plt.xlabel('log(Fold Change)')
plt.yticks(list(range(1,n+1)),Name)

fig.savefig('/Users/yi.yan/Documents/Image/'+sLabel+'SigSpeciesMagnitude.png',format='png',dpi=1200,bbox_inches='tight')
  
sDir  = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Bundi/BlastCountResult/'  
sLabel = 'Bundi' 

lFiles = os.listdir(sDir)
numFile = 0
lNumHit = [] 
lSigSpecies = [] 
lFoldChange = [] 
for filename in lFiles :
    if filename[-12:] == 'Summary.xlsx' :
        numFile = numFile + 1 
        sFile = sDir + filename
        bookSummary = xlrd.open_workbook(sFile)
        sheetSummary = bookSummary.sheet_by_index(0) 
        rowVal = sheetSummary.row_values(1)
        numHit = [rowVal[5],rowVal[12],rowVal[-2]]
        lNumHit.append(numHit)
        Pval = sheetSummary.col_values(18)
        Pval[0] = 1
        for i in range(0,len(Pval)):
            if Pval[i] == '' :
                Pval[i] = 1
                
        idx = [i for i,x in enumerate(Pval) if float(x) <= 0.05]
        Species = sheetSummary.col_values(15)
        numNT = sheetSummary.col_values(16)
        numARGOS = sheetSummary.col_values(17)
        for i in idx :
            FoldChange = float(numNT[i])/float(numARGOS[i])
            lFoldChange.append(FoldChange)
            lSigSpecies.append(Species[i])

lData = [] 
for temp in lNumHit :
    if '' not in temp: 
        lData.append(temp)
data = np.array(lData)
fig = plt.figure()
plt.boxplot(data)
plt.xlabel('Database Used')
plt.ylabel('Number of Megablast Hit')
plt.xticks([1,2,3],['nt','nt-ARGOS','ARGOS'])
plt.title(sLabel)
fig.savefig('/Users/yi.yan/Documents/Image/' + sLabel + 'Hits.png',format='png', dpi=1200,bbox_inches='tight')         
        
uSpecies = list(set(lSigSpecies))

lCoverage = [] 
for species in uSpecies :
    lCoverage.append(lSigSpecies.count(species)/numFile)

x = np.array(lCoverage) 
idx = np.argsort(x)
idx = list(reversed(idx))

sortedMetaData = [uSpecies[j] for j in idx]
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
plt.xlabel('Percent Output Coverage')
plt.title('Top Significantly different species')
 
fig.savefig('/Users/yi.yan/Documents/Image/'+sLabel+'SigSpecies.png',format='png',dpi=1200,bbox_inches='tight')

lLogFoldChange = [] 
for species in uSpecies :
    idx = [i for i,x in enumerate(lSigSpecies) if x == species]
    temp = []
    for i in idx :
        temp.append(np.log(lFoldChange[i]))
    lLogFoldChange.append(temp)

lSortedLFC = [] 
lSortedLFCMean = []
lName = []
n = 19 
if n > len(lLogFoldChange):
    n = len(lLogFoldChange)
    
lCoverage = [] 
for species in uSpecies :
    lCoverage.append(lSigSpecies.count(species)/numFile)

x = np.array(lCoverage) 
idx = np.argsort(x)
idx = list(reversed(idx))

for i in range(0,n):
    lSortedLFC.append(lLogFoldChange[idx[i]])   
    lSortedLFCMean.append(np.mean(lLogFoldChange[idx[i]]))
    lName.append(uSpecies[idx[i]])

x = np.array(lSortedLFCMean)
idx = np.argsort(x)
idx = list(reversed(idx))

fig = plt.figure()
Data =[lSortedLFC[i] for i in idx]
Name = [lName[i] for i in idx]
plt.boxplot(Data,vert=0)
plt.xlabel('log(Fold Change)')
plt.yticks(list(range(1,n+1)),Name)

fig.savefig('/Users/yi.yan/Documents/Image/'+sLabel+'SigSpeciesMagnitude.png',format='png',dpi=1200,bbox_inches='tight')
  
sDir  = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Makona/BlastCountResult/'  
sLabel = 'Makona' 

lFiles = os.listdir(sDir)
numFile = 0
lNumHit = [] 
lSigSpecies = [] 
lFoldChange = [] 
for filename in lFiles :
    if filename[-12:] == 'Summary.xlsx' :
        numFile = numFile + 1 
        sFile = sDir + filename
        bookSummary = xlrd.open_workbook(sFile)
        sheetSummary = bookSummary.sheet_by_index(0) 
        if sheetSummary.nrows > 1 :
            rowVal = sheetSummary.row_values(1)
            numHit = [rowVal[5],rowVal[12],rowVal[-2]]
            lNumHit.append(numHit)
            Pval = sheetSummary.col_values(18)
            Pval[0] = 1
            for i in range(0,len(Pval)):
                if Pval[i] == '' :
                    Pval[i] = 1
                    
            idx = [i for i,x in enumerate(Pval) if float(x) <= 0.05]
            Species = sheetSummary.col_values(15)
            numNT = sheetSummary.col_values(16)
            numARGOS = sheetSummary.col_values(17)
            for i in idx :
                FoldChange = float(numNT[i])/float(numARGOS[i])
                lFoldChange.append(FoldChange)
                lSigSpecies.append(Species[i])


lData = [] 
for temp in lNumHit :
    if '' not in temp: 
        lData.append(temp)
data = np.array(lData)
fig = plt.figure()
plt.boxplot(data)
plt.xlabel('Database Used')
plt.ylabel('Number of Megablast Hit')
plt.xticks([1,2,3],['nt','nt-ARGOS','ARGOS'])
plt.title(sLabel)
fig.savefig('/Users/yi.yan/Documents/Image/' + sLabel + 'Hits.png',format='png', dpi=1200,bbox_inches='tight')         
        
uSpecies = list(set(lSigSpecies))

lCoverage = [] 
for species in uSpecies :
    lCoverage.append(lSigSpecies.count(species)/numFile)

x = np.array(lCoverage) 
idx = np.argsort(x)
idx = list(reversed(idx))

sortedMetaData = [uSpecies[j] for j in idx]
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
plt.xlabel('Percent Output Coverage')
plt.title('Top Significantly different species')
 
fig.savefig('/Users/yi.yan/Documents/Image/'+sLabel+'SigSpecies.png',format='png',dpi=1200,bbox_inches='tight')

lLogFoldChange = [] 
for species in uSpecies :
    idx = [i for i,x in enumerate(lSigSpecies) if x == species]
    temp = []
    for i in idx :
        temp.append(np.log(lFoldChange[i]))
    lLogFoldChange.append(temp)

lSortedLFC = [] 
lSortedLFCMean = []
lName = []
n = 19 
if n > len(lLogFoldChange):
    n = len(lLogFoldChange)
    
lCoverage = [] 
for species in uSpecies :
    lCoverage.append(lSigSpecies.count(species)/numFile)

x = np.array(lCoverage) 
idx = np.argsort(x)
idx = list(reversed(idx))

for i in range(0,n):
    lSortedLFC.append(lLogFoldChange[idx[i]])   
    lSortedLFCMean.append(np.mean(lLogFoldChange[idx[i]]))
    lName.append(uSpecies[idx[i]])

x = np.array(lSortedLFCMean)
idx = np.argsort(x)
idx = list(reversed(idx))

fig = plt.figure()
Data =[lSortedLFC[i] for i in idx]
Name = [lName[i] for i in idx]
plt.boxplot(Data,vert=0)
plt.xlabel('log(Fold Change)')
plt.yticks(list(range(1,n+1)),Name)

fig.savefig('/Users/yi.yan/Documents/Image/'+sLabel+'SigSpeciesMagnitude.png',format='png',dpi=1200,bbox_inches='tight')
  