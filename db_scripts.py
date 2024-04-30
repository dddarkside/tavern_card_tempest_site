import sqlite3

db_name = "database.sqlite"
conn = None
cursor = None


def db_open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def db_close():
    global conn, cursor
    cursor.close()
    conn.close()


def db_do(query, mode=0, many=False):
    global conn, cursor
    if not mode:
        cursor.execute(query)
        conn.commit()
        if many:
            return cursor.fetchall()
        return cursor.fetchone()
    else:
        cursor.executescript(query)
        conn.commit()
        return 'There is no answer because of executescript()'


#--------------------------------------------------------------------------------------------------------------

def restart_database():
    with open("restart.sql") as file:
        db_do(file.read(), mode=1)


def add_user():
    # db_do("insert into users(mail, name) values ( 'admin@admin', 'admin');")
    db_do("insert into auth(id, password) values (1, 'admin');")  # TODO Сделать хеширование паролей

def takeAlook():
    print(db_do("select * from users;", mode=0, many=True))
    print(db_do("select * from auth;", mode=0, many=True))


if __name__=="__main__":
    db_open()

    # restart_database()
    # add_user()
    takeAlook()

    db_close()
    pass