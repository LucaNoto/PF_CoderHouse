from __future__ import unicode_literals
import os
import pandas as pd
import xlrd
# Changing the data types of all strings in the module at once

# Used to save the file as excel workbook
# Need to install this library
from xlwt import Workbook
# Used to open to corrupt excel file
import io


crimes = ['Furto Celular',"Furto Veículos","Registros de Obitos IML","Roubo Celular","Roubo Veículos"]
years = [2019,2020,2021,2022]

for c in crimes:
    columnsDf = pd.DataFrame()
    recoveredFilesPath = os.getcwd()+f"/../data/{c}/recovered/"
    
    try:
        os.mkdir(recoveredFilesPath)
    except:pass

    for y in years:
        corruptedFilesPath = os.getcwd()+f"/../data/{c}/{y}/"
        
        corruptedfiles = [f for f in os.listdir(corruptedFilesPath) if os.path.isfile(corruptedFilesPath+f)]

        for f in corruptedfiles:
            if f.split('.')[1]=='xls':
            
                filename = corruptedFilesPath+f
                # Opening the file using 'utf-16' encoding
                file1 = io.open(filename, "r", encoding="utf-16-le")
                data = file1.readlines()

                # Creating a workbook object
                xldoc = Workbook()
                # Adding a sheet to the workbook object
                sheet = xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)
                # Iterating and saving the data to sheet
                for i, row in enumerate(data):
                    # Two things are done here
                    # Removing the '\n' which comes while reading the file using io.open
                    # Getting the values after splitting using '\t'
                    for j, val in enumerate(row.replace('\n', '').split('\t')):
                        sheet.write(i, j, val)
                    
                # Saving the file as an excel file
                xldoc.save(recoveredFilesPath+f.split('.')[0]+".xlsx")


        
    recoveredFiles = [f for f in os.listdir(recoveredFilesPath) if os.path.isfile(recoveredFilesPath+f)]
    for f in recoveredFiles:
        if f.split('.')[1]=='xlsx':
            df =pd.read_excel(recoveredFilesPath+f)
            # print(df.columns)
            columnsDf[f] = list(df.columns)

    columnsDf.to_excel(os.getcwd()+f"/../data/{c}/columns{c.replace(' ','')}.xlsx",index=False)