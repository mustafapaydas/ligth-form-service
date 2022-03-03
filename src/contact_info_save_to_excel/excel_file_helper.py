import shutil
import os
from openpyxl.styles import Font
import openpyxl as xl

def copy_file(email):

    shutil.copy("PR.04-FR.06 PERSONEL IS BASVURU FORMU.xlsx", f"appeal_form_excels/{email}.xlsx")
    if os.path.exists(f"appeal_form_excels/{email}.xlsx"):
        os.remove(f"appeal_form_excels/{email}.xlsx")
        shutil.copy("PR.04-FR.06 PERSONEL IS BASVURU FORMU.xlsx", f"appeal_form_excels/{email}.xlsx")


def write_to_xlsx(row, column, file, value):
    wb=xl.load_workbook(f"appeal_form_excels/{file}.xlsx")
    sheet = wb.active
    font = Font(name='PT Sans', size=11,)

    a = sheet.cell(row=row, column=column)
    a.font = font
    a.value = value
    wb.save(f"appeal_form_excels/{file}.xlsx")