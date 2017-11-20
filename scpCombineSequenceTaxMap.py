#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:11:25 2017

@author: yi.yan
"""

from Bio import SeqIO

o_file = '/Users/yi.yan/Documents/FDA-ARGOS/FDAARGOS_BLASTDB/FDAARGOS_DB.fasta'
w_file = open('/Users/yi.yan/Documents/FDA-ARGOS/FDAARGOS_BLASTDB/FDAARGOS_DB_TaxID.txt','w')
for seq_record in SeqIO.parse(o_file, 'fasta'):
            seqName = seq_record.id
            temp = seqName.split('|')
            w_file.write(seqName + ' ' + temp[-1] + '\n')
w_file.close() 