import os
import pandas as pd
import time
from tabulate import tabulate
from colorama import Fore
from colorama import Style

clear = lambda:os.system('clear')
exit = lambda:os.system('exit')
restart = lambda:os.system('py pyrate.py')

def movie_list():
    df = pd.read_excel(file_path, converters={
        'year': str,
    })
    df.index+=1
    print(tabulate(df, headers='keys', tablefmt='simple_outline'))

def create(name, year, genre):
    
    genre = genre.replace(",", " ")
    genre = genre.replace("  ", " ")
    genre = genre.replace(" ", ", ")
    
    if df[df['id'] == len(df)+1].empty: 
        id = len(df)+1    
    else:
        id = len(df)+2
        
    data = {
        'id': [id],
        'name': [name.title()],
        'year': [year],
        'genre': [genre],
        'watched': 'No',
        'rate': '-',
        'review': '-',
        }
    
    data_new = pd.DataFrame(data)
    pd.concat([df, data_new], ignore_index=False).to_excel(file_path, index=False)
    
def edit():
    print("Insert new movie name (Leave blank if no change)")
    name = input(f"{Fore.GREEN}> ")
    print(Style.RESET_ALL)
    if df[df["name"] == name.title()].empty != True:
        print("Movie already exist!")
        time.sleep(2)
        restart()
    
    print("Insert new movie year (Leave blank if no change)")
    year = input(f"{Fore.GREEN}> ")
    print(Style.RESET_ALL)
        
    print("Insert new movie genre (Leave blank if no change)")
    genre = input(f"{Fore.GREEN}> ").title()
    print(Style.RESET_ALL)
        
    if data.iloc[:]['watched'].values[0] == 'Yes':
        print("Insert new rate number 1-5! (Leave blank if no change)")
        rate = input(f"{Fore.GREEN}> ")
        print(Style.RESET_ALL)
        try:
            rate = float(rate)
        except:
            print(f"{Fore.RED}Rate not changed!")
            print(Style.RESET_ALL)
            rate = data.iloc[:]['rate'].values[0]
            rate = float(rate[7:10])
        
        if rate > 5:
            print(f'{Fore.RED}Oops.. too much!')
            print(Style.RESET_ALL)
            time.sleep(1)
            restart()
        
        print("Insert new review! (Leave blank if no change)")
        review = input(f"{Fore.GREEN}> ")
        print(Style.RESET_ALL)
        
        if len(review) == 0:
            review = data.iloc[:]['review'].values[0]
        
        rating(data.at[1, 'id'], rate, review)
    
    if len(name) == 0:
        name = data.iloc[:]['name'].values[0]
    if len(year) == 0:
        year = data.iloc[:]['year'].values[0]
    if len(genre) == 0:
        genre = data.iloc[:]['genre'].values[0]
    
    genre = genre.replace(",", " ")
    genre = genre.replace("  ", " ")
    genre = genre.replace(" ", ", ")

    df.at[id, 'name'] = name
    df.at[id, 'year'] = str(year)
    df.at[id, 'genre'] = genre
    
    pd.DataFrame(df).to_excel(file_path, index=False)
    
def delete(id):
    df.drop(id, inplace=True)
    pd.DataFrame(df).to_excel(file_path, index=False)
    
def search(name):    
    data = df[df["name"].str.contains(name)].reset_index(drop=True)
    data.index+=1
    return data

def searchGenres(genre):    
    genre = genre.title()
    data = df[df["genre"].str.contains(genre)].reset_index(drop=True)
    data.index+=1
    return data

def select(id):    
    data = df[df["id"] == id].reset_index(drop=True)
    data.index+=1
    return data

def rating(id, rate, review):
    rateint = int(rate)
    max = 5
    star = "★" * rateint + "☆" * (max - rateint) + " (" + str(rate) + ")"
    
    df.at[id, 'rate'] = star
    df.at[id, 'watched'] = 'Yes'
    df.at[id, 'review'] = review
    pd.DataFrame(df).to_excel(file_path, index=False)
    
def sort(index, order):
    if index == 1:
        index = "name"
    else:
        index = "year"
        
    df.set_index(index, inplace=True)
    if order == 1:
        df.sort_index(inplace=True)
    else:
        df.sort_index(ascending=False, inplace=True)
        
    return df
    
while True:
    
    file_path = "data/film.xlsx"
    df = pd.read_excel(file_path, converters={
        'year': str,
    })
    df.index += 1
    
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
    user = input(f"{Fore.GREEN}> ")
    print(Style.RESET_ALL)
    
    try:
        user = int(user)
    except:
        print(f"{Fore.RED}Oops, numbers only!")
        print(Style.RESET_ALL)
        time.sleep(2)
        continue
    
    if user == 1:
        clear()
        movie_list()
        print("""
Action:
[1] Add movie
[2] Search movie
[3] Search genres
[4] Sort
[0] Back
              """)
        user = input(f"{Fore.GREEN}> ")
        print(Style.RESET_ALL)
        try:
            user = int(user)
        except:
            print(f"{Fore.RED}Oops, numbers only!")
            print(Style.RESET_ALL)
            time.sleep(2)
            continue
        
        # create
        if user == 1:
            print("insert movie name")
            name = input(f'{Fore.GREEN}> ').title()
            print(Style.RESET_ALL)
            
            if name == "":
                print(f"{Fore.RED}Name cant be empty!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            if df[df["name"] == name.title()].empty != True:
                print("Movie already exist!")
                time.sleep(2)
                restart()
            
            print("insert movie year")
            year = input(f'{Fore.GREEN}> ')
            print(Style.RESET_ALL)
            if year == "":
                print(f"{Fore.RED}Year cant be empty!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            print("insert movie genre")
            genre = input(f'{Fore.GREEN}> ').title()
            print(Style.RESET_ALL)
            if genre == "":
                print("fG{Fore.RED}enre cant be empty!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            create(name, year, genre)
            print("Completed!")
            time.sleep(2)
            continue
                      
        # Search 
        if user == 2:
            print("Type movie name")
            name = input(f"{Fore.GREEN}> ").title()
            print(Style.RESET_ALL)
            data = search(name)
            data = pd.DataFrame(data)
            if search(name).empty:
                print(f"{Fore.RED}Movie not found!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            clear()
            print(tabulate(data, headers='keys', tablefmt='simple_outline'))
            
            print(f"""
Select movie (id)!
[0] Back
                  """)
            
            # search->select
            id = input(f"{Fore.GREEN}> ")
            print(Style.RESET_ALL)
            try:
                id = int(id)
            except:
                print(f"{Fore.RED}Oops, numbers only!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            if id == 0:
                time.sleep(1)
                continue
            data = select(id)
            
            print(f"""
What are u gonna do with '{data.at[1, 'name']}'?
[1] Edit
[2] Delete
[3] Rate n Review!    
[0] Back  
                    """)
            
            user = input(f"{Fore.GREEN}> ")
            print(Style.RESET_ALL)
            try:
                user = int(user)
            except:
                print(f"{Fore.RED}Oops, numbers only!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            # search->update
            if user == 1:
                edit()
                print("Edited succesfully!")
                time.sleep(2)
                continue
                
            # search->delete
            if user == 2:
                print(f"you sure want to delete '{data.at[1, 'name']}'? y/n")
                confirm = input(f"{Fore.GREEN}> ")
                print(Style.RESET_ALL)
                confirm = confirm.lower()
                if confirm == "y":
                    delete([data.at[1, 'id']])
                    print("Deleted succesfully!")
                    time.sleep(2)
                    continue
                elif confirm == "n":
                    print("Cancelling..")
                    time.sleep(2)
                    continue
                else:
                    print(f"{Fore.RED}Oops, bad input!")
                    print(Style.RESET_ALL)
                    time.sleep(2)
                    continue
                
            # search->rating
            if user == 3:
                
                if data.at[1, 'watched'] == "Yes":
                    print(f"{Fore.RED}This movie already watched! go to edit if you want to change it!")
                    print(Style.RESET_ALL)
                    time.sleep(3)
                    continue
                
                print("Insert rate number 1-5!")
                rate = input(f"{Fore.GREEN}> ")
                print(Style.RESET_ALL)
                
                try:
                    rate = float(rate)
                except:
                    print(f"{Fore.RED}Oops, numbers only!")
                    print(Style.RESET_ALL)
                    time.sleep(2)
                    continue
                
                if rate > 5:
                    print(f'{Fore.RED}Oops.. too much!')
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    continue
                print("Insert ur review!")
                review = input(f"{Fore.GREEN}> ")
                print(Style.RESET_ALL)
                rating(data.at[1, 'id'], rate, review)
                print("Succesfully rated!")
                time.sleep(2)
                continue
            
            if user == 0:
                continue
                    
            else:
                print(f"{Fore.RED}Oops.. wrong input!")
                print(Style.RESET_ALL)
                time.sleep(1)
                continue 
         
        # genre
        if user == 3:
            print("What genre?")
            genre = input(f'{Fore.GREEN}> ')
            print(Style.RESET_ALL)
            clear()
            data = searchGenres(genre)
            print(tabulate(data, headers='keys', tablefmt='simple_outline'))
            print(f"""
Select movie (id)!
[0] Back
                    """)
            id = input(f"{Fore.GREEN}> ")
            print(Style.RESET_ALL)
            
            try:
                id = int(id)
            except:
                print(f"{Fore.RED}Oops, numbers only!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            if id == 0:
                continue
            
            # genre->select
            data = select(id)
            print(f"""
What are u gonna do with '{data.at[1, 'name']}'?
[1] Edit
[2] Delete
[3] Rate n Review!    
[0] Back  
                        """)
            
            user = input(f"{Fore.GREEN}> ")
            print(Style.RESET_ALL)
            try:
                user = int(user)
            except:
                print(f"{Fore.RED}Oops, numbers only!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            if id == 0:
                continue
            
            # genre->update
            if user == 1:
                edit()
                print("Edited succesfully!")
                time.sleep(2)
                continue
                
            # genre->delete
            if user == 2:
                print(f"you sure want to delete '{data.at[1, 'name']}'? y/n")
                confirm = input(f"{Fore.GREEN}> ")
                print(Style.RESET_ALL)
                confirm.lower
                if confirm == "y":
                    delete([data.at[1, 'id']])
                    print("Deleted succesfully!")
                    time.sleep(2)
                    continue
                else:
                    print("Cancelling..")
                    time.sleep(2)
                    continue
                
            # genre->rating
            if user == 3:
                print("Insert rate number 1-5!")
                rate = input(f"{Fore.GREEN}> ")
                print(Style.RESET_ALL)
                if rate == "":
                    print(f"{Fore.RED}Rate cant be empty!")
                    print(Style.RESET_ALL)
                    time.sleep(2)
                    restart()
                try:
                    rate = float(rate)
                except:
                    print(f"{Fore.RED}Oops, numbers only!")
                    print(Style.RESET_ALL)
                    time.sleep(2)
                    continue
                
                if rate > 5:
                    print(f'{Fore.RED}Oops.. too much!')
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    continue
                
                print("Insert ur review!")
                review = input(f"{Fore.GREEN}> ")
                print(Style.RESET_ALL)
                if review == "":
                    print("Rfe{Fore.RED}view cant be empty!")
                    print(Style.RESET_ALL)
                    time.sleep(2)
                    restart()
                
                rating(data.at[1, 'id'], rate, review)
                print("Succesfully rated!")
                time.sleep(2)
                continue
                    
            else:
                print(f"{Fore.RED}Oops.. wrong input!")
                print(Style.RESET_ALL)
                time.sleep(1)
                continue
         
        # sort
        if user == 4:
            print("""
What index are you gonna use?
[1] Name
[2] Year
[0] Back
                  """)
            index = input(f"{Fore.GREEN}> ")
            print(Style.RESET_ALL)
            try:
                index = int(index)
            except:
                print(f"{Fore.RED}Oops, numbers only!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            if index not in {1, 2}:
                print(f"{Fore.RED} Oops, wrong number!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            if index == 0:
                continue
            
            print("""
What order?
[1] Ascending
[2] Descending
[0] Back
                  """)
            order = input(f"{Fore.GREEN}> ")
            print(Style.RESET_ALL)
            try:
                order = int(order)
            except:
                print(f"{Fore.RED}Oops, numbers only!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            if order == 0:
                continue
            
            if order not in {1, 2}:
                print(f"{Fore.RED} Oops, wrong number!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
            
            clear()
            df = sort(index, order)
            print(tabulate(df, headers='keys', tablefmt='simple_outline'))
            print("[0] Back")
            user = input(f"{Fore.GREEN}> ")
            print(Style.RESET_ALL)
            try:
                user = int(user)
            except:
                print(f"{Fore.RED}Oops, numbers only!")
                print(Style.RESET_ALL)
                time.sleep(2)
                continue
             
        if user == 0:
            continue
        else:
            print(f"{Fore.RED} Oops, wrong number!")
            print(Style.RESET_ALL)
            time.sleep(2)
        
    elif user == 0:
        print("Bye bye :(")
        exit()
        break
    
    else:
        print(f"{Fore.RED}Oops, wrong input!")
        print(Style.RESET_ALL)
        time.sleep(2)
        continue
        
