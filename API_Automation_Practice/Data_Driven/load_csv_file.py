import xlrd
import openpyxl

workbook = openpyxl.load_workbook("datadriven.xlsx")
print(workbook)
# sheet = workbook.wb["data"]
#
# #get total number of rows
# rowCount = sheet.ncols
# #colCount = sheet.ncols
# print(rowCount)
# #print(colCount)

