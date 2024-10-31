import os
import time

clear = lambda:os.system('clear')

def print_triangle_1 (n):
    for i in range(n, 0, -1):
        print('*' * i)

def print_triangle_2 (n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)
        
def print_triangle_3 (n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * i)  
        
def print_box_1 (n, o):
    for i in range(n):
        print('*' * o)
    
def print_box_2 (n, o):
    for i in range(n):
        if i == 0 or i == n - 1:
            # Cetak baris pertama dan terakhir penuh dengan bintang
            print('*' * o)
        else:
            # Cetak baris dengan bintang di kedua sisi dan spasi di tengah
            print('*' + ' ' * (o - 2) + '*')

while True:
    
    print("""
     _____                 _   _             
    |  ___|   _ _ __   ___| |_(_) ___  _ __  
    | |_ | | | | '_ \ / __| __| |/ _ \| '_ \ 
    |  _|| |_| | | | | (__| |_| | (_) | | | |
    |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|

    Pilih fungsi:
    1. Membuat segitiga
    2. Mencetak segitiga angka                                          
        """)

    user = int(input("> "))

    if user == 1:
        print("""
              1. Triangle 1
              2. Triangle 2
              3. Triangle 3
              4. Box 1
              5. Box 2
              """)
        user = int(input("> "))
        if user == 1:
            print("""
                  Berapa jumlah n nya?
                  """)
            n = int(input("> "))
            print_triangle_1(n)
            break;
        elif user == 2:
            print("""
                  Berapa jumlah n nya?
                  """)
            n = int(input("> "))
            print_triangle_2(n)
            break;
        elif user == 3:
            print("""
                  Berapa jumlah n nya?
                  """)
            n = int(input("> "))
            print_triangle_3(n)
            break;
        elif user == 4:
            print("""
                  Berapa jumlah panjangnya?
                  """)
            n = int(input("> "))
            print("""
                  Berapa jumlah lebarnya?
                  """)
            o = int(input("> "))
            print_box_1(n, o)
            break;
        elif user == 5:
            print("""
                  Berapa jumlah panjangnya?
                  """)
            n = int(input("> "))
            print("""
                  Berapa jumlah lebarnya?
                  """)
            o = int(input("> "))
            print_box_2(n, o)
            break;
        else:
            print("""
                  Pilihan anda tidak sesuai!
                  """)
            continue;
    elif user == 2:
        print("""
              
              """)
    else:
        print("Anda harus memilih 1 atau 2!")
        print("merestart...")
        time.sleep(4)
        clear()
