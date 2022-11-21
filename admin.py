import os
from time import sleep
import mysql.connector as sql
con = sql.connect(host='localhost', user='root',
                  password='KnockKnockOpenUpTheDoor#69420$', auth_plugin='mysql_native_password')
cur = con.cursor()
try:
    cur.execute("create database wordle")
    print("Database created succefully")
except:
    pass

con = sql.connect(host='localhost', user='root',
                  password='KnockKnockOpenUpTheDoor#69420$', database='wordle', auth_plugin='mysql_native_password')
cur = con.cursor()

try:
    st = "create table users(id int primary key, username varchar(20), password varchar (20), attempts int(20));"
    cur.execute(st)
except:
    pass


def add_user():
    uid = int(input("Enter ID: "))
    name = input("Enter the username: ").upper()
    password = input("Enter the password: ").upper()
    st = "Insert into users values({}, '{}', '{}',0);".format(
        uid, name, password)
    cur.execute(st)
    con.commit()


def show_user():
    st = "Select * from users;"
    cur.execute(st)
    data = cur.fetchall()
    print()
    if data == []:
        print("Table is empty")
    else:
        for row in data:
            print(row)


def remove_user():
    uid = int(input("Enter the ID you want to delete: "))
    st = "Delete from users where id = {}".format(uid)
    cur.execute(st)
    con.commit()


def admin_main():
    sleep(0.1)
    print()
    print("1. Add user")
    print("2. Show users")
    print("3. Delete users")
    print("4. Exit")
    print()
    print("-"*50)
    print()
    n = int(input('Enter your option: '))
    if n not in (1, 2, 3, 4):
        print("Invalid option")
    elif n == 1:
        add_user()
        admin_main()
    elif n == 2:
        show_user()
        admin_main()
    elif n == 3:
        remove_user()
        admin_main()
    elif n == 4:
        exit()


def launch():
    print()
    print("ADMIN LOGIN")
    uname = input("Username: ")
    pws = input("Password: ")
    if uname == pws == "admin":
        print()
        print("Loading..")
        sleep(0.5)
        print()

        print("Welcome, Admin")

        admin_main()
    else:
        print("Wrong username or password.. Try again")
        exit()


def user_or_admin():
    print()
    print("1. USER")
    print("2. ADMIN")
    print()
    choice = int(input("Enter your choice (1/2): "))
    if choice in (1, 2):
        if choice == 1:
            user_main()
        elif choice == 2:
            launch()
    else:
        print("Invalid choice")
        user_or_admin()


def user_main():
    st = "Select username from users;"
    cur.execute(st)
    data = cur.fetchall()
    user_list = []
    for row in data:
        user_list.append(row[0])

    uname = input("Enter your username: ")
    if uname.upper() in user_list:
        pws = input("Enter your password: ")
        st2 = "Select password from users where username = '{}';".format(
            uname.upper())
        cur.execute(st2)
        data2 = cur.fetchall()
        password_list = []
        for row in data2:
            password_list.append(row[0])
        if pws.upper() in password_list:
            print("Succesfully logged in..")
            print()
            print("Opening game...")
            sleep(0.5)
            os.system("py wordle.py")
            print()
            print("Exiting the game..")
            sleep(0.5)
        else:
            print("Wrong password")
    else:
        print("Invalid username")


user_or_admin()
