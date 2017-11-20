# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:41:37 2017

@author: yihen
"""
"""def funAutoBlast(sFastaFolder,sGenBankFolder):"""
import os 
import sys
sys.path += ["/Users/yi.yan/Documents/Functions/"]   
from funContigLocalBlast import funLocalBlast
from funGenusLocalBlast import funGenusLocalBlast
 
#sFastaFolder = "/Users/yi.yan/Documents/PythonBlast/TestFolderFasta/"
#sFastaFolder = "/Users/yi.yan/Documents/FDA-ARGOS/Batch6/PFDA1_Batch6_Misidentified_Contaminated/"

#sGenBankFolder = "/Users/yi.yan/Documents/PythonBlast/TestFolderGenbank/"
#sOutPutName = 'Batch_6_MisClassify' 
#lFastaFileNames = os.listdir(sFastaFolder)
#lGenBankFileNames = os.listdir(sGenBankFolder)

"""Start File to Write to"""
sDir = '/Users/yi.yan/Documents/FDA-ARGOS/Batch6-QC/PFDA1_Batch6_Final_assemblies/'

lFiles = ['CNH_1200.fasta',
 'CNH_1201.fasta',
 'CNH_1202.fasta',
 'CNH_1204.fasta',
 'CNH_1205.fasta',
 'CNH_1206.fasta',
 'CNH_1207.fasta',
 'CNH_1211.fasta',
 'CNH_1212.fasta',
 'CNH_1213.fasta',
 'CNH_1214.fasta',
 'CNH_1215.fasta',
 'CNH_1216.fasta',
 'CNH_1217.fasta',
 'CNH_1221.fasta',
 'CNH_1223.fasta',
 'CNH_1224.fasta',
 'CNH_1225.fasta',
 'CNH_1227.fasta',
 'CNH_1228.fasta',
 'CNH_1229.fasta',
 'CNH_1230.fasta',
 'CNH_1232.fasta',
 'CNH_1233.fasta',
 'CNH_1234.fasta',
 'CNH_1236.fasta',
 'CNH_1239.fasta',
 'CNH_1240.fasta',
 'CNH_1241.fasta',
 'CNH_1242.fasta',
 'CNH_1243.fasta',
 'CNH_1244.fasta',
 'CNH_1245.fasta',
 'CNH_1246.fasta',
 'CNH_540.fasta',
 'NCCH_003.fasta',
 'NCCH_005.fasta',
 'NCCH_010.fasta',
 'NCCH_011.fasta',
 'NCTR1.fasta',
 'NCTR2.fasta',
 'RIID_127.fasta',
 'RIID_128.fasta',
 'RIID_129.fasta',
 'RIID_130.fasta',
 'RIID_131.fasta',
 'RIID_133.fasta',
 'RIID_134.fasta',
 'RIID_135.fasta',
 'RIID_136.fasta',
 'RIID_137.fasta',
 'RIID_141.fasta',
 'RIID_142.fasta',
 'RIID_144.fasta',
 'RIID_146.fasta',
 'RIID_148.fasta',
 'RIID_149.fasta',
 'RIID_153.fasta',
 'RIID_154.fasta',
 'RIID_156.fasta',
 'RIID_158.fasta',
 'RIID_160.fasta',
 'RIID_162.fasta',
 'RIID_163.fasta',
 'RIID_166.fasta',
 'RIID_167.fasta',
 'UMJJ1887.fasta']


for i in range(0,len(lFiles)):
    print('Processing ' + lFiles[i])
    sFile = sDir + lFiles[i]
    funLocalBlast(sFile,\
                      'N/A','ref_prok_rep_genomes')
    
#funGenusLocalBlast(lFastaFileNames[0],\
              #lGBKFileNames[0],'ref_prok_rep_genomes')    