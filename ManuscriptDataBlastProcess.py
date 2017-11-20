#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:16:54 2017

@author: yi.yan
"""

import sys
import os
sys.path += ["/Users/yi.yan/Documents/Functions/"]  
from funProcessSpeciesCount import funProcessSpeciesCount

sDir = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Bundi/BlastCountResult/' 
cFiles = os.listdir(sDir)

for fileName in cFiles:
    if fileName[-3:] == 'txt':
        file = sDir + fileName 
        funProcessSpeciesCount(file)

sDir = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Makona/BlastCountResult/'
cFiles = os.listdir(sDir)

for fileName in cFiles:
    if fileName[-3:] == 'txt':
        file = sDir + fileName 
        funProcessSpeciesCount(file)
    
sDir = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/MockClinical/BlastCountResult/'
cFiles = os.listdir(sDir)

for fileName in cFiles:
    if fileName[-3:] == 'txt':
        file = sDir + fileName 
        funProcessSpeciesCount(file)
    
sDir = '/Users/yi.yan/Documents/Data/NTARGOSBLASTRUN2/Sample/BlastCountResult/'
cFiles = os.listdir(sDir)

for fileName in cFiles:
    if fileName[-3:] == 'txt':
        file = sDir + fileName 
        funProcessSpeciesCount(file)