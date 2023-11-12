import sqlite3
import pandas as pd

# Pripojenie k databáze
conn = sqlite3.connect('moja_prva.sql')

# Načítanie tabuľky do DataFrame
df = pd.read_sql_query("SELECT * from student", conn)
# Resetovanie indexu
df.reset_index(inplace=True)

# Zmena názvu stĺpca 'index' na 'id'
df.rename(columns={'index': 'id'}, inplace=True)
df = df.drop('id', axis=1)


# Zobrazenie tabuľky
print(df)

# Zatvorenie spojenia
conn.close()
