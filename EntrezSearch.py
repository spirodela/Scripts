#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:15:59 2017

@author: yi.yan
"""
import xlrd
from Bio import Entrez
Entrez.email = "yi.yan@hhs.fda.gov"

sFileName = '/Users/yi.yan/Documents/FDA-ARGOS/Accessions_batch1-4.xlsx'
workbook = xlrd.open_workbook(sFileName)
worksheet = workbook.sheet_by_index(0)

lBioSample = [worksheet.cell(i,6).value for i in range(1,worksheet.nrows)] 
lTaxID = []
lProblematicEntries = []
for sBioSample in lBioSample:
    #handle = Entrez.efetch(db="biosample", id="SAMN04875531", retmode = 'text')
    
    handle = Entrez.esearch(db="assembly",term= sBioSample)
    
    ID = Entrez.read(handle)
    if ID['Count'] != '0':
        Info = Entrez.read(Entrez.esummary(db='assembly',id=ID['IdList'][0]))
        lTaxID.append(Info['DocumentSummarySet']['DocumentSummary'][0]['Taxid'])
    else:
        lProblematicEntries.append(sBioSample)

sTaxIDFileName = 'Batch1-4Taxid.txt' 
sFile = open(sTaxIDFileName,'w')
for taxid in lTaxID:
    sFile.write(taxid+'\n')

sFile.close()

sFaultyBioSampleName = 'Batch1-4BioSampleWithoutAssembly.txt' 
sFile = open(sFaultyBioSampleName,'w')
for biosample in lProblematicEntries:
    sFile.write(biosample+'\n')

sFile.close()

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