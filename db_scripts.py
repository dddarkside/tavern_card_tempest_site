import sqlite3

db_name = "database.sqlite"
conn = None
cursor = None


def db_open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def db_close():
    cursor.close()
    conn.close()


def db_do(query, mode=0):
    cursor.executescript(query)
    conn.commit()
    if not mode:
        return cursor.fetchone()
    return cursor.fetchall()


#--------------------------------------------------------------------------------------------------------------

def restart_database():
    db_open()
    with open("restart.sql") as file:
        db_do(file.read())
    db_close()


def add_user():
    db_open()
    db_do("insert into users(mail, name) values ('admin@admin', 'admin')")
    db_do("insert into auth(password) values ('admin')")  # TODO Сделать хеширование паролей
    db_close()

def takeAlook():
    db_open()
    print(db_do("select mail from users", mode=1))
    db_close()


if __name__=="__main__":
    # restart_database()
    # add_user()
    takeAlook()
    pass