#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:26:37 2017

@author: yi.yan
"""

import xlrd
from Bio import Entrez
import pickle
Entrez.email = "yi.yan@hhs.fda.gov"

sFileName = '/Users/yi.yan/Documents/Data/Accessions_batch1-4.xlsx'
workbook = xlrd.open_workbook(sFileName)
worksheet = workbook.sheet_by_index(0)

lBioSample = [worksheet.cell(i,6).value for i in range(1,worksheet.nrows)] 
lARGOSInfo = []
lProblematicEntries = []
lTaxID = []
for sBioSample in lBioSample:
    #handle = Entrez.efetch(db="biosample", id="SAMN04875531", retmode = 'text')
    print('working on biosample' + ' ' + sBioSample)
    handle = Entrez.esearch(db="assembly",term= sBioSample)
    
    ID = Entrez.read(handle)
    if ID['Count'] != '0':
        Info = Entrez.read(Entrez.esummary(db='assembly',id=ID['IdList'][0]))
        lTaxID.append(Info['DocumentSummarySet']['DocumentSummary'][0]['Taxid'])
        lARGOSInfo.append(Info['DocumentSummarySet']['DocumentSummary'][0])

    else:
        lProblematicEntries.append(sBioSample)


f = open('/Users/yi.yan/Documents/Data/Batch1-4AssemblyAttrib.pckl', 'wb')
pickle.dump(lARGOSInfo, f)
f.close()

uTaxID = set(lTaxID)
uTaxID = list(uTaxID)
lNCBIInfo = []
for sID in uTaxID:
    print('working on TaxID' + ' ' + sID)
    sID = sID + '[Taxid]'
    handle = Entrez.esearch(db="assembly",term= sID,RetMax = 5000)
    EntrezID = Entrez.read(handle)
    for AssemblyID in EntrezID['IdList']:
        Info = Entrez.read(Entrez.esummary(db='assembly',id=AssemblyID))
        lNCBIInfo.append(Info)
        
f = open('/Users/yi.yan/Documents/Data/NCBIAssemblyAttrib.pckl', 'wb')
pickle.dump(lNCBIInfo, f)
f.close()
