#Data Driven Testing
#WritingExcel

import openpyxl

file = r"C:\\Users\\oguzh\\Documents\\Data.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook["Sheet3"]

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value="Welcome"

workbook.save(file)