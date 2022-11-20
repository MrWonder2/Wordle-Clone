from time import sleep
import mysql.connector as sql


con = sql.connect(host='localhost', user='root',
                  password='KnockKnockOpenUpTheDoor#69420$', database='wordle', auth_plugin='mysql_native_password')

cur = con.cursor()

try:
    st = "create table users(id int primary key, username varchar(20), password varchar (20));"
    cur.execute(st)
except:
    pass


def add_user():
    uid = int(input("Enter ID: "))
    name = input("Enter the username: ").upper()
    password = input("Enter the password: ").upper()
    st = "Insert into users values({}, '{}', '{}');".format(
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


def main():
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
        main()
    elif n == 2:
        show_user()
        main()
    elif n == 3:
        remove_user()
        main()
    elif n == 4:
        exit()


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

    main()
else:
    print("Wrong username or password.. Try again")
    exit()
