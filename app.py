import os
from time import sleep
import mysql.connector as sql

con = sql.connect(host='localhost', user='root',
                  password='KnockKnockOpenUpTheDoor#69420$', database='wordle', auth_plugin='mysql_native_password')

cur = con.cursor()


def main():
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


main()
