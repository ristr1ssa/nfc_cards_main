import psycopg2
import random
try:
    connection = psycopg2.connect(
        user="postgres",
        database="fa_nfc_cards",
        password="9009",
        host="localhost",)

    connection.autocommit = True
    db = connection.cursor()

    db.execute("""CREATE TABLE IF NOT EXISTS main_data(
        hash TEXT PRIMARY KEY,
        
        name TEXT, 
        
        photo_link TEXT, 
        
        soc1 TEXT,
        
        soc2 TEXT,
        
        soc3 TEXT,
        
        soc4 TEXT)
        """)

    print("Успешно подключился к БД")

except Exception as _ex:
    print("Возникла ошибка во время подключения к БД\n", _ex)
    connection.close()


def get_data(user_hash: str) -> list:
    db.execute("SELECT * FROM main_data WHERE hash = ('%s')" % (user_hash, ))
    data = db.fetchall()
    return data


def insert_data(link1: str = " ", link2: str = " ", link3: str = " ", link4: str = " "):
    user_hash = gen_hash()
    db.execute("INSERT INTO main_data VALUES ('%s', '%s', '%s', '%s', '%s')" %
               (link1, link2, link3, link4, user_hash))
    return True


def gen_hash():
    user_hash = random.getrandbits(128)
    user_hash = "%032x" % user_hash
    db.execute("SELECT * FROM main_data WHERE hash = ('%s')" % (user_hash, ))
    data = db.fetchone()

    if len(data) == 0:
        return user_hash

    return gen_hash()
