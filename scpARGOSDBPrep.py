#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:36:23 2017

@author: yi.yan
"""


from Bio import SeqIO
o_file = '/Users/yi.yan/Documents/FDA-ARGOS/FDAARGOS_BLASTDB/FDAARGOS_DB.fasta'
tax_file = open('/Users/yi.yan/Documents/FDA-ARGOS/FDAARGOS_BLASTDB/FDAARGOS_DB_TaxID.txt','w')

with open('/Users/yi.yan/Documents/FDA-ARGOS/FDAARGOS_BLASTDB/FDAARGOS_DB_V2.fasta', 'w') as w_file:
    for seq_record in SeqIO.parse(o_file, 'fasta'):
        seqName = seq_record.id 
        temp = seqName.split('|')
        seq_record.id = 'gnl|FDAARGOS|' + temp[4]
        seq_record.name = seq_record.id
        lName = seq_record.description.split() 
        seq_record.description = lName[-2] + ' ' + lName[-1]
        SeqIO.write(seq_record, w_file, 'fasta')
        tax_file.write(seq_record.id + ' ' + temp[-1] + '\n')

