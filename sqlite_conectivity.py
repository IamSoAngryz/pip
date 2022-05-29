"""
Set up a conection to SQLite database
(conectivitatea la oa baza de date SQLite)
https://sqlite.org/index.html
SQLite - librarie in C care implementeaza un sistem de gestiune a bazelor de
date light-weight (SQL engine disk-stored - salveaza pe disc baza de date)
    - baza de date este stocata pe disc (alternativ se poate stoca in memorie)
    - nu necesita un server care sa execute / proceseze interogarile
sqlite3
"""
import sqlite3

# seta o conecxiune la baza de date
con = sqlite3.connect('curs.db')

# executa queries (interogari ale bazei de date)
c = con.cursor()

# inchide o conexiune la o baza de date
con.close()