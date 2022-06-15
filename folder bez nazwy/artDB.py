import os
import sqlite3


def create_database():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    # tworzenie tabeli
    cursor.execute("""CREATE TABLE kluby 

                          (nazwa text, trener text, kraj text, liczba_pilkarzy int, 
                          najlepszy_zawodnik text,sponsor_glowny text) 

                       """)
    # insert
    cursor.execute("INSERT INTO kluby VALUES "
                   "('Piast Czluchow', 'Roberto Babiaggio', 'Polska', 12, 'Robertinson', 'Robex')")
    # zapisanie danych do bazy
    conn.commit()


def select_all_albums(nazwa):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM kluby WHERE nazwa=?"
    cursor.execute(sql, [nazwa])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    if not os.path.exists("mydatabase.db"):
        create_database()
    print(select_all_albums('Piast Czluchow'))
