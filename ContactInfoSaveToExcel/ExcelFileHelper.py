import shutil
import os
from openpyxl.styles import Font
import openpyxl as xl
def copyFile(email):

    shutil.copy("PR.04-FR.06 PERSONEL IS BASVURU FORMU.xlsx", f"AppealFormExcels/{email}.xlsx")
    if os.path.exists(f"AppealFormExcels/{email}.xlsx"):
        os.remove(f"AppealFormExcels/{email}.xlsx")
        shutil.copy("PR.04-FR.06 PERSONEL IS BASVURU FORMU.xlsx", f"AppealFormExcels/{email}.xlsx")


def xlWrite(row,column,file,value):
    wb=xl.load_workbook(f"AppealFormExcels/{file}.xlsx")
    sheet = wb.active
    font = Font(name='PT Sans', size=11,)

    a = sheet.cell(row=row, column=column)
    a.font = font
    a.value = value
    wb.save(f"AppealFormExcels/{file}.xlsx")