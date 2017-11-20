#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:22:20 2017

@author: yi.yan
"""

import os 
import sys
sys.path += ["/Users/yi.yan/Documents/Functions/"]   
from funProcessCountXL import funProcessCountXL 

sEaviumSampleDir = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Sample/BlastCountResult/' 
lEaviumSampleFiles = os.listdir(sEaviumSampleDir)

s1 = '_nt_BLASTCOUNT.xlsx'
s2 = '_NT_ARGOS_BLASTCOUNT.xlsx'
s3 = '_FDA_ARGOS_BLASTCOUNT.xlsx'

funProcessCountXL(sEaviumSampleDir,lEaviumSampleFiles,s1,s2,s3,100000)

sEaviumMCDir = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/MockClinical/BlastCountResult/' 
lEaviumMCFiles = os.listdir(sEaviumMCDir)

s1 = '_nt_PE2_BLASTResult.xlsx'
s2 = '_NT_ARGOS_PE2_BLASTResult.xlsx'
s3 = '_FDA_ARGOS_PE2_BLASTResult.xlsx'

funProcessCountXL(sEaviumMCDir,lEaviumMCFiles,s1,s2,s3,600000)

sBundiDir = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Bundi/BlastCountResult/' 
lBundiFile = os.listdir(sBundiDir)

s1 = '_nt_Result.xlsx'
s2 = '_NT_ARGOS_Result.xlsx'
s3 = '_FDA_ARGOS_Result.xlsx'

funProcessCountXL(sBundiDir,lBundiFile,s1,s2,s3,100000)

sMakonaDir = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Makona/BlastCountResult/' 
lMakonaFile = os.listdir(sMakonaDir)

s1 = '_nt_Result.xlsx'
s2 = '_NT_ARGOS_Result.xlsx'
s3 = '_FDA_ARGOS_Result.xlsx'

funProcessCountXL(sMakonaDir,lMakonaFile,s1,s2,s3,100000)
