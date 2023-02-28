from turtle import title
from flask import Flask, render_template, request, redirect, url_for
from pprint import pprint
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float(), nullable=False)

db.create_all()

""" new_book =  Book(id= 1, title= "Harry Potter", author= "J. K. Rowling", rating= 9.3)

db.session.add(new_book)
db.session.commit() """


all_books = db.session.query(Book).all()


""" db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit() """



@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', bookdata= all_books)


@app.route("/add", methods= ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    elif request.method == "POST":
        """ book_data = {
            "title": request.form['book'],
            "author": request.form['author'],
            "rating": request.form['rating']
        } """

        book_data = Book(title= request.form['book'], author= request.form['author'], rating= request.form['rating'])

        """ all_books.append(book_data) """
        db.session.add(book_data)
        db.session.commit()

        pprint(all_books)
        
        return redirect( url_for('home') )


@app.route("/edit/<id>", methods= ["GET", "POST"])
def edit(id):
    if request.method == "GET":
        selected_book = Book.query.get(id)

        return render_template('edit.html', book = selected_book)
    elif request.method == "POST":
        book_to_update = Book.query.filter_by(id= id).first()
        book_to_update.rating = request.form['new_rating']
        db.session.commit() 
        

        return redirect( url_for('home'))

@app.route("/delete/<id>")
def delete(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect( url_for('home') )




if __name__ == "__main__":
    app.run(debug=True)

