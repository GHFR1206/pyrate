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
film.index += 1


def movie_list():
    film = pd.read_excel(file_path)
    film.index += 1
    print(tabulate(film, headers='keys', tablefmt='grid'))

def create(name, year, desc):
    data = {
        'id': len(film)+1,
        'name': [name.title()],
        'year': [year],
        'watched': 'No',
        'rate': '-',
        'review': '-',
        }
    data_new = pd.DataFrame(data)
    create = pd.concat([film, data_new], ignore_index=False)
    create.to_excel(file_path, index=False)
    
def edit(id, name, year):
    df.at[id-1, 'name'] = name
    df.at[id-1, 'year'] = year
    pd.DataFrame(df).to_excel(file_path, index=False)
    
def delete(id):
    df.drop(id-1, inplace=True)
    pd.DataFrame(df).to_excel(file_path, index=False)
    
def detail(name):    
    data = df[df["name"] == name]
    if data.empty:
        return 0
    data.index+=1
    return data

def rating(id, rate):
    data = df[df["id"] == id]
    data.index += 1
    rateint = int(rate)
    max = 5
    star = "★" * rateint + "☆" * (max - rateint) + " (" + str(rate) + ")"
    
    data.at[id, 'rate'] = star
    data.at[id, 'watched'] = 'Yes'
    pd.DataFrame(data).to_excel(file_path, index=False)
    
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
[4] Search movie
[0] Back
              """)
        user = int(input("> "))
        print()
        
        # create
        if user == 1:
            print("insert movie name then year")
            name = input('Movie name > ')
            year = input('Movie year > ')
            create(name, year)
            print("Completed!")
            time.sleep(2)
            continue
            
        # delete
        if user == 2:
            print("Select movie you want to delete")
            id = int(input("> "))
            print(f"you sure want to delete '{df.iloc[id-1]['name']}'? y/n")
            confirm = input("> ")
            confirm.lower
            if confirm == "y":
                delete(id)
                print("Deleted successfully!")
                time.sleep(2)
                continue
            else:
                print("Cancelling..")
                time.sleep(2)
                continue
            
        # update
        if user == 3:
            print("Select movie you want to edit")
            id = int(input("> "))
            print("Input new movie name")
            name = input("> ")
            print("Input new movie year")
            year = input("> ")
                        
            edit(id, name, year)
            print("Edited succesfully!")
            time.sleep(2)
            continue
                       
        if user == 4:
            print("Type movie name")
            name = input("> ").title()
            data = detail(name)
            if data.empty:
                print("Movie not found!")
                time.sleep(2)
                continue
            
            clear()
            print(tabulate(data, headers='keys', tablefmt='grid'))
            print(f"""
What are you gonna do with that?
[1] Rate
[2] Review 
[0] Back
                  """)
            user = int(input("> "))
            
            if user == 1:
                print("Input rate number 1-5!")
                rate = float(input("> "))
                rating(data.at[1, 'id'], rate)
                print("Successfully rated!")
                print("restarting..")
                time.sleep(2)
                continue
            
            if user == 0:
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
        
