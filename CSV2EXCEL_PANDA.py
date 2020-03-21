# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:53:38 2020

@author: rohit
"""

import os
os.getcwd()
import glob
import pandas as pd


Files = glob.glob(os.path.join('*.csv'))
print(Files)

File_Names = [file[:-4] for file in Files]
File_Names

for i,file in enumerate (Files):
    df = pd.read_csv(file)
    excel_writer = pd.ExcelWriter(File_Names[i] + ".xlsx", engine='xlsxwriter')
    df.to_excel(excel_writer, sheet_name='mysheet', index=False)
    excel_writer.save()