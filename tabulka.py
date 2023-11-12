import sqlite3
import random
import pandas as pd

# Pripojenie k databáze
conn = sqlite3.connect('moja_prva.sql')
c = conn.cursor()

num = 1000

def random_mena():
    spol = "qwrtzpsdfghjklxcvbnm"
    sam = "euioay"
    n = random.randrange(6,13)
    name = ""
    ch = ""
    for i in range(n):
        if i == 0:
            ch = random.choice(spol)
            name += ch.upper()
        else:
            if ch in spol:
                ch = random.choice(sam)
                name += ch
            else:
                ch = random.choice(spol)
                name += ch
    return name

# Načítanie tabuľky farieb očí
df_eyes = pd.read_sql_query("SELECT * FROM eyes", conn)

# Vytvorenie mapovania farieb na ich indexy
colour_to_index = df_eyes.reset_index().set_index('eyecolour')['index'].to_dict()

# Vloženie náhodných mien, priezvisk, veľkostí nôh a indexov farieb očí do tabuľky 'student'
for i in range(num):
    meno = random_mena()
    priezvisko = random_mena()
    noha = random.randrange(39,52)
    eyecolour = random.choice(list(colour_to_index.values()))
    c.execute("INSERT INTO student (name, surname, footsize, eyecolour) VALUES (?, ?, ?, ?)", (meno, priezvisko, noha, eyecolour))

# Uloženie zmien a zatvorenie spojenia
conn.commit()
conn.close()
