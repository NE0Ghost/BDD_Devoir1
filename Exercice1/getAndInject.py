#!/usr/bin/python3
import re
import json
import requests
import sqlite3

def english_to_boolean(text):
    if text == "no":
        return True
    elif text == "yes":
        return False

def boolean_to_english(bool):
    if bool:
        return "true"
    else:
        return "false"

i = 1
x = 0
spell_list = []

# Spells getter
while(i>0):
    text = requests.get("http://www.dxcontent.com/SDB_SpellBlock.asp?SDBID="+str(i)).text
    if re.search("Source:", text) is not None:
        result = re.search("<div class='heading'><P>(.*)<\/p><\/div><P class.*<B>Level<\/b>.*sorcerer\/wizard ([0-9]*),.*<b>Components<\/b>(.*)<\/p><div class='Sep1'>Effect", text)
        result_resistance = re.search("<b>Spell Resistance<\/b> (.*)<\/p><div class='Sep1'>Description", text)
        if result is not None:
            data = {
                "_id" : x,
                "name": result.group(1),
                "level": int(result.group(2)),
                "components": re.findall("[VMS]", result.group(3)),
            }
            if result_resistance is not None:
                data.update({"spell_resistance": bool(english_to_boolean(result_resistance.group(1)))})
            else:
                data.update({"spell_resistance":  None })
            print(json.dumps(data))
            spell_list.append(data)
            x+=1
    else:
        i = -1
    i += 1

# Spells SQLite inserter
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

fo = open("spells.db", "wb")
fo.close()

connexion = create_connection("spells.db")
blank = connexion.cursor()
blank.execute("""
CREATE TABLE IF NOT EXISTS spells (
_id                 INTEGER PRIMARY KEY,
name                TEXT,
level               INTEGER,
components          TEXT,
spell_resistance    TEXT
);""")

for spell in spell_list:
    components=""
    for c in spell["components"]:
        components+=c+','
    components = components[:-1]
    spell_resitance=""
    if(spell["spell_resistance"]!=None):
        spell_resitance=boolean_to_english(spell["spell_resistance"])
    connexion.execute('INSERT INTO spells(_id,name,level,components,spell_resistance) VALUES("'+str(spell["_id"])+'","'+spell["name"]+'","'+str(spell["level"])+'","'+components+'","'+spell_resitance+'")')

connexion.commit()
connexion.close()