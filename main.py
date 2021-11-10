import sqlite3
from random import randint
global main_db, sql
main_db = sqlite3.connect("main.db")
sql = main_db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

main_db.commit()
def registration():
    user_login = input("Login: ")
    user_password = input("Password: ")

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}' ")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        main_db.commit()
        print("Registration completed successfully!!! ")
    else:
        print("Such a record already exists! ")

def gachi_casino():
    user_login = input("Log in: ")
    users_choose = int(input("Choose the number in range 0-3: "))
    number = randint(0,3)

    sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'")
    balance = sql.fetchone()[0]

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print("There is no such login. Please register at Gachi Casino")
        registration()
    else:
        if number == users_choose:
            sql.execute(f'UPDATE users SET cash = {balance + 400} WHERE login = "{user_login}" ')
            main_db.commit()
            print("YOU WON!")
        else:
            print("YOU LOSE!")
            sql.execute(f'UPDATE users SET cash = {balance - 100} WHERE login = "{user_login}" ')
            main_db.commit()
def enter():
    for i in sql.execute('SELECT login, cash FROM users'):
        print(i)

def main():
    gachi_casino()
    enter()

main()
