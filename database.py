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

    print("Успешно подключился к БД")

except Exception as _ex:
    print("Возникла ошибка во время подключения к БД\n", _ex)
    connection.close()


def configure_profile(user_hash: str):
    db.execute("SELECT socials FROM main_data WHERE hash = '%s'" %
               (user_hash, ))

    socials: str = db.fetchone()
    data = {}

    for _ in socials[0].split(", "):
        db.execute("SELECT link FROM %s " % (_, ))
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

    return text
