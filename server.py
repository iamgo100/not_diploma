#!/usr/bin/python
# -*- coding: utf8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash
import helpfunc as hf
import books as db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ffcbb1af81d63144389a5d6e'

@app.route('/')
def main():
    con, cur = db.connecting()
    books = db.select_all(con, cur)
    con.close()
    return render_template('index.html', books=books)

@app.route('/book<int:id>')
def book(id):
    con, cur = db.connecting()
    entry = db.select_entry(con, cur, 'id', id)
    con.close()
    return render_template('book.html', entry=entry[0])

@app.route('/book/create', methods=('GET','POST'))
def book_create():
    if request.method == "POST":
        req = request.form
        error = False
        if not req['name']:
            error = True
            flash('name', category='error')
        else:
            flash('name', category='success')
        author = hf.checking_select(req, 'author')
        if not author:
            error = True
            flash('author', category='error')
        else:
            flash('author', category='success')
        if not error:
            series = hf.checking_select(req, 'series')
            p_office = hf.checking_select(req, 'p_office')
            annotation = req['annotation'].replace('\r\n', '<br>')
            film_adapt = req['film-adapt'].replace('\r\n', '<br>')
            entry = (req['name'], author, p_office, req['year'], annotation, req['cover'], series, req['part'], film_adapt)
            con, cur = db.connecting()
            db.add_entry(con, cur, entry)
            con.close()
            return redirect(url_for('main'))
    title = 'Запись книги'
    con, cur = db.connecting()
    authors = ['Выберите автора', 'Новый автор', 'Автор неизвестен']
    p_offices = ['Выберите издательство', 'Новое издательство', 'Самиздат']
    series = ['Выберите серию', 'Нет серии', 'Новая серия']
    hf.add_options(authors, con, cur, 'author')
    hf.add_options(p_offices, con, cur, 'p_office')
    hf.add_options(series, con, cur, 'series')
    con.close()
    return render_template('createbook.html', title=title, authors=authors, p_offices=p_offices, series=series)

if __name__ == "__main__":
    app.run(
        host='localhost', 
        port=8000
    )