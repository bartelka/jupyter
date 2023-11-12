import sqlite3

# Pripojenie k databáze
conn = sqlite3.connect('moja_prva.sql')
c = conn.cursor()

# Vymazanie všetkých riadkov z tabuľky
c.execute("DELETE FROM student")

# Uloženie zmien a zatvorenie spojenia
conn.commit()
conn.close()
