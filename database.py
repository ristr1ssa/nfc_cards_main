import psycopg2
import random
try:
    connection = psycopg2.connect(
        user="postgres",
        password="9009",
        host="localhost",
        database="nfc_cards_bot"
    )

    connection.autocommit = True
    db = connection.cursor()

    db.execute("""CREATE TABLE IF NOT EXISTS main_data(
        email TEXT PRIMARY KEY,
        socials TEXT,
        nickname TEXT,
        photo_url TEXT,
        hash TEXT);""")

    db.execute("""CREATE TABLE IF NOT EXISTS vk(
        email TEXT,
        link TEXT);""")

    db.execute("""CREATE TABLE IF NOT EXISTS instagram(
        email TEXT,
        link TEXT);""")

    db.execute("""CREATE TABLE IF NOT EXISTS telegram(
        email TEXT,
        link TEXT);""")

    db.execute("""CREATE TABLE IF NOT EXISTS youtube(
        email TEXT,
        link TEXT);""")

    db.execute("""CREATE TABLE IF NOT EXISTS ozon(
        email TEXT,
        link TEXT);""")

    db.execute("""CREATE TABLE IF NOT EXISTS wildberries(
        email TEXT,
        link TEXT);""")

    print("DB: OK")

except Exception as _ex:
    print("DB: Error", _ex)
    connection.close()


def configure_profile(user_hash: str):
    db.execute("SELECT socials, email FROM main_data WHERE hash = '%s'" %
               (user_hash, ))

    socials, email = db.fetchone()
    data = {}

    for _ in socials.split(", "):
        db.execute("SELECT link FROM %s WHERE email = '%s'" % (_, email))
        link = db.fetchone()
        link = link[0]

        data[_] = link

    text = ""

    for elem in data:
        text += """<span>
  <a href="%s">
    <img alt="%sICO" src="/static/icons/%s.ico" height="25" width="25">
  </a>
</span>\n""" % (data[elem], elem, elem)

    db.execute("SELECT nickname, photo_url FROM main_data WHERE hash = '%s'" %
               (user_hash, ))

    nickname, photo_url = db.fetchone()
    data = [photo_url, nickname, text]
    return data
