#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:56:48 2017

@author: yi.yan
"""
from os import listdir

sDir = '/Users/yi.yan/Documents/FDA-ARGOS/CBER7-13_QCs'
cFileNames =  ['PFDA1_20160510_M01994_IL100070146_CGTACTA_L001_R1.blast.topHits.txt',
 'PFDA1_20160510_M01994_IL100070147_AGGCAGA_L001_R1.blast.topHits.txt',
 'PFDA1_20160510_M01994_IL100070148_TCCTGAG_L001_R1.blast.topHits.txt',
 'PFDA1_20160510_M01994_IL100070149_GGACTCC_L001_R1.blast.topHits.txt',
 'PFDA1_20160510_M01994_IL100070446_CGATGTA_L001_R1.blast.topHits.txt',
 'PFDA1_20160510_M01994_IL100070447_TTAGGCA_L001_R1.blast.topHits.txt',
 'PFDA1_20160510_M01994_IL100070448_TGACCAA_L001_R1.blast.topHits.txt',
 'PFDA1_20160510_M01994_IL100070449_ACAGTGA_L001_R1.blast.topHits.txt',
 'PFDA1_20170216_M01994_IL100080299_CGACCTG_L001_R1.blast.topHits.txt',
 'PFDA1_20170216_M01994_IL100081347_CGTACTA_L001_R1.blast.topHits.txt',
 'PFDA1_20170908_M00708_IL100092258_CGACCTG_L001_R1.blast.topHits.txt',
 'PFDA1_20170908_M00708_IL100092259_TAATGCG_L001_R1.blast.topHits.txt',
 'PFDA1_20170908_M00708_IL100092375_CGTACTAG-TATCCTCT_L001_R1.blast.topHits.txt',
 'PFDA1_20170908_M00708_IL100092376_AGGCAGAA-AGAGTAGA_L001_R1.blast.topHits.txt']
for filen in cFileNames :
    print('Processing' + ' ' + filen)
    fileName = sDir + '/' + filen
    tempFile = open(fileName,'r')
    outFileName = fileName[0:-3] + 'Krona_Report' + '.txt' 
    outFile = open(outFileName,'w')
    cEntries = tempFile.readlines()    
    tempFile.close()
    for i in range(8,len(cEntries)):
        tempL = cEntries[i].split() 
        numRead = tempL[0]
        taxid = tempL[-1]
        for j in range(0,int(numRead)):
            outFile.write(str(taxid) + '\n')
    outFile.close() 