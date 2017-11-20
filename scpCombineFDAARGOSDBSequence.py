#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:27:54 2017

@author: yi.yan
"""

from Bio import SeqIO
from os import listdir
from Bio import Entrez

Entrez.email = "yi.yan@hhs.fda.gov"

sDir = '/Users/yi.yan/Documents/FDA-ARGOS/FDA_ARGOS_DB/Assemblies_All/'
cFiles = listdir(sDir)
cFiles = cFiles[1:len(cFiles)]

with open('/Users/yi.yan/Documents/FDA-ARGOS/FDAARGOS_BLASTDB/FDAARGOS_DB.fasta', 'w') as w_file:
    for filen in cFiles:
        sARGOSID = filen[0:-6]
        handle = Entrez.esearch(db="BioSample",term= sARGOSID) 
        ID = Entrez.read(handle)
        Info = Entrez.read(Entrez.esummary(db='BioSample',id=ID['IdList'][0]))
        sTaxid = Info['DocumentSummarySet']['DocumentSummary'][0]['Taxonomy']
        sOrganismName = Info['DocumentSummarySet']['DocumentSummary'][0]['Organism']
        o_file = sDir + filen 
        for seq_record in SeqIO.parse(o_file, 'fasta'):
            seqName = seq_record.id 
            seq_record.id = 'gnl|FDAARGOS|' + 'gnl|ID|' + sARGOSID + \
            '_' + seqName + '|gnl|FDAARGOSID|' + sARGOSID + '|kraken:taxid|' \
            + sTaxid 
            seq_record.name = seq_record.id
            seq_record.description = sOrganismName
            SeqIO.write(seq_record, w_file, 'fasta')

