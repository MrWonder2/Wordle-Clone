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
