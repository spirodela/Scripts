#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:31:08 2017

@author: yi.yan
"""
import re 
import xlrd
from Bio import Entrez
import pickle

Entrez.email = "yi.yan@hhs.fda.gov"

sFileName = '/Users/yi.yan/Documents/FDA-ARGOS/Accessions_batch1-4.xlsx'
workbook = xlrd.open_workbook(sFileName)
worksheet = workbook.sheet_by_index(0)

lBioSample = [worksheet.cell(i,6).value for i in range(1,worksheet.nrows)] 
lRecords = [] 
lProblematicRecords = [] 
for sBioSample in lBioSample:
    handle = Entrez.efetch(db="biosample", id=sBioSample, retmode = 'text')
    nSwitch = 0
    try:
        record = handle.readlines()
    except:
        nSwitch = 1
    if nSwitch == 0:
        nAttributes = record.index('Attributes:\n')
        for i in range(nAttributes+1,len(record)):
            a = sBioSample 
            b = re.findall('(?<=/).*?(?==)',record[i])
            c = re.findall('(?<=").*?(?=")',record[i])
            if b != [] and c != []:
                entry = (a,b,c)
                lRecords.append(entry)
    else:
        lProblematicRecords.append(sBioSample)

f = open('Batch1-4Attrib.pckl', 'wb')
pickle.dump(lRecords, f)
f.close()

f = open('Batch1-4AttribError.pckl', 'wb')
pickle.dump(lProblematicRecords, f)
f.close()