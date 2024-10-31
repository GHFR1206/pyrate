import os
from tabulate import tabulate
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

clear = lambda:os.system('clear')
clear()

film = load_workbook('data/film.xlsx')
ws = film.active

# for row in range(1,11):
#     for col in range(1,3):
#         char = get_column_letter(col)
#         table = [[ws[char + str(row)].value]]
#         print(ws[char + str(row)].value , "\t", end="")
#     print()

def table_gene():
    global film
    global ws
    for row in range(1,11):
        for col in range(1,3):
            char = get_column_letter(col)
            table = [[ws[char + str(row)].value]]
            table = table + table_gene()
            return table

print(table_gene())