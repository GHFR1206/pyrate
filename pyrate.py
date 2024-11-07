import os
import pandas as pd
import time
from tabulate import tabulate
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

clear = lambda:os.system('clear')
exit = lambda:os.system('exit')
restart = lambda:os.system('py pyrate.py')

file_path = "data/film.xlsx"
film = pd.read_excel(file_path)
wb = load_workbook(file_path)
ws = wb.active
df = pd.DataFrame(film)
# print(film.index)
film.index += 1
# print(film.index)

def movie_list():
    print(tabulate(film, headers='keys', tablefmt='grid'))

def create(name, year):
    data = {
        'id': len(film)+1,
        'name': [name.title()],
        'year': [year]
        }
    data_new = pd.DataFrame(data)
    create = pd.concat([film, data_new], ignore_index=False)
    create.to_excel(file_path, index=False)
    
def edit(id, name, year):
    data = {
        'name': [name.title()],
        'year': [year]
        }
    data_old = df.iloc[id-1]
    data_new = pd.DataFrame(data)
    df = pd.DataFrame(film)
    create.to_excel(file_path, index=False)
    
    

# for row in range(1,11):
#     for col in range(1,3):
#         char = get_column_letter(col)
#         table = [[ws[char + str(row)].value]]
#         print(ws[char + str(row)].value , "\t", end="")
#     print()
    
while True:
    clear()
    print(df.iloc[0]['id'])
    break
    print("""
██████╗ ██╗   ██╗██████╗  █████╗ ████████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝███████║   ██║   █████╗  
██╔═══╝   ╚██╔╝  ██╔══██╗██╔══██║   ██║   ██╔══╝  
██║        ██║   ██║  ██║██║  ██║   ██║   ███████╗
╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
Save your movies here!

what'u want?
[1] Movie list
[0] Exit
        """)
    user = int(input("> "))
    if user == 1:
        clear()
        movie_list()
        print("""
Action:
[1] Add movie
[2] Delete movie
[3] Edit Movie
[4] Select movie
[0] Back
              """)
        user = int(input("> "))
        
        if user == 1:
            print("insert movie name then year")
            name = input('Movie name > ')
            year = input('Movie year > ')
            create(name, year)
            print("Completed!")
            time.sleep(2)
            restart()
        if user == 3:
            print("Select movie you want to edit")
            id = int(input(print("> ")))
            print("Input new movie name")
            name = int(input(print("> ")))
            print("Input new movie year")
            year = int(input(print("> ")))
            
            edit(id, name, year)
            
            print("Edited succesfully!")
            time.sleep(2)
            continue
        if user == 0:
            continue
        
    elif user == 0:
        print("Bye bye :(")
        exit()
        break
    else:
        print("Oops, wrong input!")
        print("restarting..")
        time.sleep(2)
        continue
        
