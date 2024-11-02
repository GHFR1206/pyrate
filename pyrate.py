import os
import pandas as pd
import time
from tabulate import tabulate
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

clear = lambda:os.system('clear')
exit = lambda:os.system('exit')

film = load_workbook('data/film.xlsx')
ws = film.active

def movie_list():
    file_path = 'data/film.xlsx'  
    df = pd.read_excel(file_path)
    print(tabulate(df, headers='keys', tablefmt='grid'))

# for row in range(1,11):
#     for col in range(1,3):
#         char = get_column_letter(col)
#         table = [[ws[char + str(row)].value]]
#         print(ws[char + str(row)].value , "\t", end="")
#     print()


    
    
while True:
    clear()
    print("""
██████╗ ██╗   ██╗██████╗  █████╗ ████████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝███████║   ██║   █████╗  
██╔═══╝   ╚██╔╝  ██╔══██╗██╔══██║   ██║   ██╔══╝  
██║        ██║   ██║  ██║██║  ██║   ██║   ███████╗
╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
Save your movies here!

what'cu want?
[1] Movie list
[0] Exit
        """)
    user = int(input("> "))
    if user == 1:
        clear()
        movie_list()
        print("""

[1] Add movie
[2] Delete movie
[3] Select movie
[0] Back
              """)
        user = int(input("> "))
        
        if user == 1:
            print("insert movie name, and year")
            print("> ")
        if user == 0:
            continue
        
    elif user == 2:
        clear()
        print("Bye bye :(")
        exit()
        break
    else:
        print("Oops, wrong input!")
        print("restarting..")
        time.sleep(2)
        continue
        
