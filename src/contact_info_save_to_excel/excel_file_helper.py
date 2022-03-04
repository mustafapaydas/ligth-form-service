import shutil
import os
from openpyxl.styles import Font
import openpyxl as xl
import  file_helper
def copy_file(email):
    folder = "appeal_form_excels"
    file_helper.exists_path(folder)
    shutil.copy("PR.04-FR.06 PERSONEL IS BASVURU FORMU.xlsx", f"{folder}/{email}.xlsx")
    if os.path.exists(f"{folder}/{email}.xlsx"):
        os.remove(f"{folder}/{email}.xlsx")
        shutil.copy("PR.04-FR.06 PERSONEL IS BASVURU FORMU.xlsx", f"{folder}/{email}.xlsx")


def write_to_xlsx(row, column, file, value):

    wb=xl.load_workbook(f"appeal_form_excels/{file}.xlsx")
    sheet = wb.active
    font = Font(name='PT Sans', size=11,)

    a = sheet.cell(row=row, column=column)
    a.font = font
    a.value = value
    wb.save(f"appeal_form_excels/{file}.xlsx")