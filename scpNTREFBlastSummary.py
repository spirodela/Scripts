#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:56:50 2017

@author: yi.yan
"""
import os 
import sys
import xlsxwriter 
import xlrd

sDir = '/Users/yi.yan/Documents/FDA-ARGOS/Batch6-QC/PFDA1_Batch6_Final_assemblies/' 
lFiles = os.listdir(sDir)
wFileName = 'Batch_6_REFSM.xlsx' 
REFworkbook = xlsxwriter.Workbook(wFileName)
wFileName = 'Batch_6_NTSM.xlsx' 
NTworkbook = xlsxwriter.Workbook(wFileName)
for file in lFiles :
    if file[-4:] == 'xlsx' and file[-7:] != 'SM.xlsx':
        sFile = sDir + file
        sName = file[0:-5]
        bookFile = xlrd.open_workbook(sFile)
        Refsheet = bookFile.sheet_by_index(1)
        NTsheet = bookFile.sheet_by_index(3)
        REFworksheet = REFworkbook.add_worksheet(sName)
        for i in range(0,Refsheet.nrows):
            for j in range(0,Refsheet.ncols):
                REFworksheet.write(i,j,Refsheet.cell(i,j).value)
        NTworksheet = NTworkbook.add_worksheet(sName)
        for i in range(0,NTsheet.nrows):
            for j in range(0,NTsheet.ncols):
                NTworksheet.write(i,j,NTsheet.cell(i,j).value)

REFworkbook.close()
NTworkbook.close()