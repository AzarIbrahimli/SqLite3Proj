import sqlite3 as sql

def create_table():
    conn = sql.connect('lesson.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS (
    id integer PRIMARY KEY,
    name text,
    surname text,
    username text,
    password text)""")
    print("Created successfully")

    conn.cursor()
    conn.close()

def insert(name,surname,username,password):
    conn = sql.connect('lesson.db')
    cursor = conn.cursor()

    insert_command = """INSERT INTO USERS (name, surname, username, password) VALUES {} """
    data = (name, surname,username, password)
    cursor.execute(insert_command.format(data))
#    print("Inserted successfully")
    conn.commit()
    conn.close()

def update(username, newPassword):
    conn = sql.connect('lesson.db')
    cursor = conn.cursor()

    update_command = """UPDATE USERS SET password = '{}' WHERE username = '{}' """
    cursor.execute(update_command.format(newPassword, username))

    print("Updated successfully")
    conn.commit()
    conn.close()

def delete(username):
    conn = sql.connect('lesson.db')
    cursor = conn.cursor()

    delete_command = """DELETE from USERS WHERE username = '{}' """
    cursor.execute(delete_command.format(username))

    print("Deleted successfully")
    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect('lesson.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM USERS""")
    users_list = cursor.fetchall()
    for user in users_list:
        print(f"""Name: {user[1]}     Surname: {user[2]}     Username: {user[3]}\n""")
    conn.commit()
    conn.close()

def delete_table():
    conn = sql.connect('lesson.db')
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE IF EXISTS USERS""")

    conn.commit()
    conn.close()

def search(username):
    conn = sql.connect('lesson.db')
    cursor = conn.cursor()

    search_command = """SELECT * from USERS WHERE username = '{}' """
    cursor.execute(search_command.format(username))
    user = cursor.fetchone()

    conn.close()
    return user

def login(username, password):
    conn = sql.connect('lesson.db')
    cursor = conn.cursor()

    search_command = """SELECT * from USERS WHERE username = '{}'AND password = {} """
    cursor.execute(search_command.format(username,password))
    user = cursor.fetchone()

    conn.close()
    return user
#search('aliyev100')