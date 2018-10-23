import sqlite3
import pprint

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None


connexion = create_connection("spells.db")
cursor = connexion.cursor()
cursor.execute("SELECT name, level, components FROM spells WHERE (level <= 4 AND components = 'V')")

pprint.pprint(cursor.fetchall())

