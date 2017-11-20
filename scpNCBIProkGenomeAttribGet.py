#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:49:36 2017

@author: yi.yan
"""

import re 
from Bio import Entrez
import pickle

Entrez.email = "yi.yan@hhs.fda.gov"
file = open('ncbi_genomes_prokaryotes_biosample.txt','r')
BioSampleNames = file.readlines()
BioSampleNames = BioSampleNames[1:len(BioSampleNames)]
lRecords = [] 
lProblematicRecords = [] 
lEmptyRecords =[]
count = 1;
for k in range(35721,len(BioSampleNames)):
    sBioSample = BioSampleNames[k]
    nSwitch = 0
    print('Processing BioSample' + str(count))
    count = count+1
    if sBioSample[0:4] == 'SAMN':
        handle = Entrez.efetch(db="biosample", id=sBioSample[0:-1], retmode = 'text')

        try:
            record = handle.readlines()
        except:
            nSwitch = 1
        if nSwitch == 0:
            try:
                nAttributes = record.index('Attributes:\n')
            except:
                nAttributes = 0
            if nAttributes != 0:
                for i in range(nAttributes+1,len(record)):
                    a = sBioSample 
                    b = re.findall('(?<=/).*?(?==)',record[i])
                    c = re.findall('(?<=").*?(?=")',record[i])
                    if b != [] and c != []:
                        entry = (a,b,c)
                        lRecords.append(entry)
            else:
                lEmptyRecords.append(sBioSample)
        else:
            lProblematicRecords.append(sBioSample)

f = open('NCBIProkGenomeAttribBatch2.pckl', 'wb')
pickle.dump(lRecords, f)
f.close()

f = open('NCBIProkGenomeAttribErrorBatch2.pckl', 'wb')
pickle.dump(lProblematicRecords, f)
f.close()

f = open('NCBIProkGenomeAttribEmptyBatch2.pckl', 'wb')
pickle.dump(lEmptyRecords, f)
f.close()