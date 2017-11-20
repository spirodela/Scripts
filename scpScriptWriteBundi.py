#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:02:33 2017

@author: yi.yan
"""

sDir = '/scratch/yi.yan/Clinical/Bundi/'
fileName = ['1-1_S1_L001_R1_001.fastq',
 '1-1_S1_L001_R2_001.fastq',
 '1-2_S2_L001_R1_001.fastq',
 '1-2_S2_L001_R2_001.fastq',
 '1-3_S3_L001_R1_001.fastq',
 '1-3_S3_L001_R2_001.fastq',
 '10-1_S8_L001_R1_001.fastq',
 '10-1_S8_L001_R2_001.fastq',
 '10-2_S16_L001_R1_001.fastq',
 '10-2_S16_L001_R2_001.fastq',
 '10-3_S24_L001_R1_001.fastq',
 '10-3_S24_L001_R2_001.fastq',
 '2-1_S9_L001_R1_001.fastq',
 '2-1_S9_L001_R2_001.fastq',
 '2-2_S10_L001_R1_001.fastq',
 '2-2_S10_L001_R2_001.fastq',
 '2-3_S11_L001_R1_001.fastq',
 '2-3_S11_L001_R2_001.fastq',
 '3-1_S17_L001_R1_001.fastq',
 '3-1_S17_L001_R2_001.fastq',
 '3-2_S18_L001_R1_001.fastq',
 '3-2_S18_L001_R2_001.fastq',
 '3-3_S19_L001_R1_001.fastq',
 '3-3_S19_L001_R2_001.fastq',
 '4-1_S25_L001_R1_001.fastq',
 '4-1_S25_L001_R2_001.fastq',
 '4-2_S26_L001_R1_001.fastq',
 '4-2_S26_L001_R2_001.fastq',
 '4-3_S27_L001_R1_001.fastq',
 '4-3_S27_L001_R2_001.fastq',
 '5-1_S4_L001_R1_001.fastq',
 '5-1_S4_L001_R2_001.fastq',
 '5-2_S5_L001_R1_001.fastq',
 '5-2_S5_L001_R2_001.fastq',
 '5-3_S6_L001_R1_001.fastq',
 '5-3_S6_L001_R2_001.fastq',
 '6-1_S12_L001_R1_001.fastq',
 '6-1_S12_L001_R2_001.fastq',
 '6-2_S13_L001_R1_001.fastq',
 '6-2_S13_L001_R2_001.fastq',
 '6-3_S14_L001_R1_001.fastq',
 '6-3_S14_L001_R2_001.fastq',
 '7-1_S20_L001_R1_001.fastq',
 '7-1_S20_L001_R2_001.fastq',
 '7-2_S21_L001_R1_001.fastq',
 '7-2_S21_L001_R2_001.fastq',
 '7-3_S22_L001_R1_001.fastq',
 '7-3_S22_L001_R2_001.fastq',
 '8-1_S28_L001_R1_001.fastq',
 '8-1_S28_L001_R2_001.fastq',
 '8-2_S29_L001_R1_001.fastq',
 '8-2_S29_L001_R2_001.fastq',
 '8-3_S30_L001_R1_001.fastq',
 '8-3_S30_L001_R2_001.fastq',
 '9-1_S7_L001_R1_001.fastq',
 '9-1_S7_L001_R2_001.fastq',
 '9-2_S15_L001_R1_001.fastq',
 '9-2_S15_L001_R2_001.fastq',
 '9-3_S23_L001_R1_001.fastq',
 '9-3_S23_L001_R2_001.fastq',
 'NTC1_S33_L001_R1_001.fastq',
 'NTC1_S33_L001_R2_001.fastq',
 'NTC2_S34_L001_R1_001.fastq',
 'NTC2_S34_L001_R2_001.fastq',
 'NTC3_S35_L001_R1_001.fastq',
 'NTC3_S35_L001_R2_001.fastq',
 'NTC4_S31_L001_R1_001.fastq',
 'NTC4_S31_L001_R2_001.fastq',
 'NTC5_S32_L001_R1_001.fastq',
 'NTC5_S32_L001_R2_001.fastq']

wFile = open('BLASTCCountBundi.sh','w')
wFile.write('#!/bin/bash\n')
wFile.write('export PATH=/home/yi.yan/ManuscriptData/Scripts:$PATH\n')

for stuff in fileName :
    s1 = sDir + stuff[0:-6] + '_' + '100000' + '_BLAST_nt'
    s2 = sDir + stuff[0:-6] + '_' + '100000' + '_BLAST_NT_ARGOS'
    s3 = sDir + stuff[0:-6] + '_' + '100000' + '_BLAST_FDA_ARGOS'
    s11 =stuff[0:-6] + '_' + '100000' + '_BLAST_nt'
    s22 = stuff[0:-6] + '_' + '100000' + '_BLAST_NT_ARGOS'
    s33 = stuff[0:-6] + '_' + '100000' + '_BLAST_FDA_ARGOS'
    wFile.write('BLASTCOUNT.sh' + ' ' + s1 + '.txt' + ' BlastResult/' + s11 + '_Result.txt\n')
    wFile.write('BLASTCOUNT.sh' + ' ' + s2 + '.txt' + ' BlastResult/' + s22 + '_Result.txt\n')
    wFile.write('BLASTCOUNT.sh' + ' ' + s3 + '.txt' + ' BlastResult/' + s33 + '_Result.txt\n')

    #wFile.write('SubSampleBLAST ' + sDir + stuff + ' 100000 nt\n')
    #wFile.write('SubSampleBLAST ' + sDir + stuff + ' 100000 NT_ARGOS\n')
    #wFile.write('SubSampleBLAST ' + sDir + stuff + ' 100000 FDA_ARGOS\n')
wFile.close()     