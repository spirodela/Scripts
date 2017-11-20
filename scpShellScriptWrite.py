#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:46:43 2017

@author: yi.yan
"""

sDir = '/scratch/yi.yan/Clinical/Makona/'
fileName = ['1-1_S1_L001_R1_001__paired_.fastq',
 '1-2_S2_L001_R1_001__paired_.fastq',
 '1-3_S3_L001_R1_001__paired_.fastq',
 '10-1_S12_L001_R1_001__paired_.fastq',
 '10-2_S13_L001_R1_001__paired_.fastq',
 '10-3_S14_L001_R1_001__paired_.fastq',
 '11-1_S20_L001_R1_001__paired_.fastq',
 '11-2_S21_L001_R1_001__paired_.fastq',
 '11-3_S22_L001_R1_001__paired_.fastq',
 '12-1_S28_L001_R1_001__paired_.fastq',
 '12-2_S29_L001_R1_001__paired_.fastq',
 '12-3_S30_L001_R1_001__paired_.fastq',
 '13-1_S35_L001_R1_001__paired_.fastq',
 '13-2_S36_L001_R1_001__paired_.fastq',
 '13-3_S37_L001_R1_001__paired_.fastq',
 '14-1_S40_L001_R1_001__paired_.fastq',
 '14-2_S41_L001_R1_001__paired_.fastq',
 '14-3_S42_L001_R1_001__paired_.fastq',
 '15-1_S45_L001_R1_001__paired_.fastq',
 '15-2_S46_L001_R1_001__paired_.fastq',
 '15-3_S47_L001_R1_001__paired_.fastq',
 '2-1_S9_L001_R1_001__paired_.fastq',
 '2-2_S10_L001_R1_001__paired_.fastq',
 '2-3_S11_L001_R1_001__paired_.fastq',
 '3-1_S17_L001_R1_001__paired_.fastq',
 '3-2_S18_L001_R1_001__paired_.fastq',
 '3-3_S19_L001_R1_001__paired_.fastq',
 '4-1_S25_L001_R1_001__paired_.fastq',
 '4-2_S26_L001_R1_001__paired_.fastq',
 '4-3_S27_L001_R1_001__paired_.fastq',
 '5-1_S8_L001_R1_001__paired_.fastq',
 '5-2_S33_L001_R1_001__paired_.fastq',
 '5-3_S34_L001_R1_001__paired_.fastq',
 '6-1_S16_L001_R1_001__paired_.fastq',
 '6-2_S38_L001_R1_001__paired_.fastq',
 '6-3_S39_L001_R1_001__paired_.fastq',
 '7-1_S24_L001_R1_001__paired_.fastq',
 '7-2_S43_L001_R1_001__paired_.fastq',
 '7-3_S44_L001_R1_001__paired_.fastq',
 '8-1_S32_L001_R1_001__paired_.fastq',
 '8-2_S48_L001_R1_001__paired_.fastq',
 '8-3_S49_L001_R1_001__paired_.fastq',
 '9-1_S4_L001_R1_001__paired_.fastq',
 '9-2_S5_L001_R1_001__paired_.fastq',
 '9-3_S6_L001_R1_001__paired_.fastq',
 'NTC1_S7_L001_R1_001__paired_.fastq',
 'NTC2_S15_L001_R1_001__paired_.fastq',
 'NTC3_S23_L001_R1_001__paired_.fastq',
 'NTC4_S31_L001_R1_001__paired_.fastq',
 'NYC5_S53_L001_R1_001__paired_.fastq']

wFile = open('BLASTCCountMakona.sh','w')
wFile.write('#!/bin/bash\n')
wFile.write('export PATH=/scratch/yi.yan/Clinical/Makona:$PATH\n')
#wFile.write('export PATH=/home/yi.yan/ManuscriptData/Scripts:$PATH\n')
for stuff in fileName :
    s1 = sDir + stuff[0:-6] + '_' + '100000' + '_BLAST_nt'
    s2 = sDir + stuff[0:-6] + '_' + '100000' + '_BLAST_NT_ARGOS'
    s3 = sDir + stuff[0:-6] + '_' + '100000' + '_BLAST_FDA_ARGOS'
    s11 =stuff[0:-6] + '_' + '100000' + '_BLAST_nt'
    s22 = stuff[0:-6] + '_' + '100000' + '_BLAST_NT_ARGOS'
    s33 = stuff[0:-6] + '_' + '100000' + '_BLAST_FDA_ARGOS'
    wFile.write('BLASTCOUNT2.sh' + ' ' + s1 + '.txt' + ' BlastResult/' + s11 + '_Result.txt\n')
    wFile.write('BLASTCOUNT2.sh' + ' ' + s2 + '.txt' + ' BlastResult/' + s22 + '_Result.txt\n')
    wFile.write('BLASTCOUNT2.sh' + ' ' + s3 + '.txt' + ' BlastResult/' + s33 + '_Result.txt\n')
    
    #wFile.write('SubSampleBLAST ' + sDir + stuff + ' 100000 nt\n')
    #wFile.write('SubSampleBLAST ' + sDir + stuff + ' 100000 NT_ARGOS\n')
    #wFile.write('SubSampleBLAST ' + sDir + stuff + ' 100000 FDA_ARGOS\n')



wFile.close()     