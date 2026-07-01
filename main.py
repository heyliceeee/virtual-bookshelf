from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

all_books = [] # list to store all the books

db = sqlite3.connect("books-collection.db") # connect to the database
cursor = db.cursor() # create a cursor object
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)") # create a table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', 9.3)") # insert a book into the table
db.commit() # commit the changes to the database

@app.route('/')
def home():
    return render_template("index.html", books=all_books) # books is a variable

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST": # if the form is submitted
        title = request.form.get("title") # get the value of the input
        author = request.form.get("author") # get the value of the input
        rating = request.form.get("rating") # get the value of the input

        if title and author and rating: # if the inputs are not empty
            all_books.append({
                "title": title,
                "author": author,
                "rating": rating
            }) # add the book to the list

        return redirect(url_for("home")) # redirect to the home page
    return render_template("add.html") # render the add.html template


if __name__ == "__main__":
    app.run(debug=True)

