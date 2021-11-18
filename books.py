import sqlite3
import os.path as p

def create_tables(con):

    con.execute(
        '''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            p_office TEXT,
            year INTEGER,
            annotation TEXT,
            cover TEXT,
            series TEXT,
            part INTEGER,
            film_adapt TEXT
        )
        '''
    )
    con.commit()

def add_entry(con, cur, values):
    columns = ("name", "author", "p_office", "year", "annotation", "cover", "series", "part", "film_adapt")
    columns = (',').join(columns)
    values = ('","').join(values)
    query = f'INSERT INTO books ({columns}) VALUES ("{values}")'
    try:
        print(query)
        cur.execute(query)
    except sqlite3.Error as e:
        print(f'Ошибка добавления: {e}\n')
    else:
        print('Запись успешно добавлена\n')
        con.commit()

def change_entry(con, cur, columns, values, key):
    columns = (',').join(columns)
    values = ('","').join(values)
    query = f'UPDATE books SET ({columns}) = ("{values}") WHERE id = {key}'
    try:
        print(query)
        cur.execute(query)
    except sqlite3.Error as e:
        print(f'Ошибка изменения: {e}\n')
    else:
        print('Запись успешно изменена\n')
        con.commit()

def delete_entry(con, cur, key):
    query = f'DELETE FROM books WHERE id = {key}'
    try:
        print(query)
        cur.execute(query)
    except sqlite3.Error as e:
        print(f'Ошибка удаления: {e}\n')
    else:
        print('Запись успешно удалена\n')
        con.commit()

def select_entry(con, cur, col, key):
    query = f'SELECT * FROM books WHERE {col} = {key}'
    try:
        print(query)
        res = cur.execute(query).fetchall()
    except sqlite3.Error as e:
        print(f'Ошибка поиска: {e}\n')
    else:
        con.commit()
        return res

def select_column(con, cur, col):
    query = f'SELECT {col} FROM books'
    try:
        print(query)
        res = cur.execute(query).fetchall()
    except sqlite3.Error as e:
        print(f'Ошибка поиска: {e}\n')
    else:
        con.commit()
        return res

def select_all(con, cur):
    try:
        res = cur.execute('SELECT * FROM books').fetchall()
    except sqlite3.Error as e:
        print(f'Ошибка поиска: {e}\n')
    else:
        con.commit()
        return res

def connecting():
    try:
        con = sqlite3.connect(p.join(p.abspath(p.dirname(__file__)), 'books.db'))
        cur = con.cursor()
        return con, cur
    except sqlite3.Error as e:
        print(f'Ошибка: {e}')
        return

if __name__ == "__main__":
    con, cur = connecting()
    # create_tables(con)
    print(select_all(con, cur))
    con.close()