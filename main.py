from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# modern declarative base (SQLAlchemy 2.0)
class Base(DeclarativeBase):
    """Base class for all models."""
    pass
app = Flask(__name__) # create an instance of the Flask class

# configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db" # set the database URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # disable tracking modifications

db = SQLAlchemy(model_class=Base) # initialize the SQLAlchemy object
db.init_app(app) # initialize the database

# define the Book model (books table in the database)
class Book(Base):
    """Book model."""
    __tablename__ = "books" # set the table name

    id: Mapped[int] = mapped_column(Integer, primary_key=True) # primary key column
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True) # title column
    author: Mapped[str] = mapped_column(String(250), nullable=False) # author column
    rating: Mapped[float] = mapped_column(Float, nullable=False) # rating column

# create a table (only if it doesn't exist')
with app.app_context():
    db.create_all() # create the books table

@app.route('/')
def home():
    """Home page."""
    q = request.args.get("q", "") # get the query parameter from the URL
    sort = request.args.get("sort", "") # get the sort parameter from the URL

    query = db.select(Book) # select all books from the database

    if q: # if the query parameter is not empty
        query = query.where(Book.title.ilike(f"%{q}%") | Book.author.ilike(f"%{q}%")) # filter the books by title or author

    if sort == "title": # if the sort parameter is "title"
        query = query.order_by(Book.title.asc()) # order the books by title in ascending order
    elif sort == "rating": # if the sort parameter is "rating"
        query = query.order_by(Book.rating.desc()) # order the books by rating in descending order

    books = db.session.execute(query).scalars().all() # execute the query and get the books

    return render_template("index.html", books=books) # render the index.html template

@app.route("/add", methods=["GET", "POST"])
def add():
    """Add a new book."""
    if request.method == "POST": # if the form is submitted
        title = request.form.get("title") # get the value of the input
        author = request.form.get("author") # get the value of the input
        rating = request.form.get("rating") # get the value of the input

        if title and author and rating: # if the inputs are not empty
            new_book = Book(title=title, author=author, rating=float(rating)) # add the book to the list
            db.session.add(new_book) # add the book to the database
            db.session.commit() # commit the changes

        return redirect(url_for("home")) # redirect to the home page
    return render_template("add.html") # render the add.html template

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book, book_id) # get the book by its ID

    if request.method == "POST": # if the form is submitted
        book.title = request.form.get("title") # update the book's title
        book.author = request.form.get("author") # update the book's author
        book.rating = float(request.form.get("rating")) # update the book's rating
        db.session.commit() # commit the changes
        return redirect(url_for("home")) # redirect to the home page
    return render_template("edit.html", book=book) # render the edit.html template


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = db.get_or_404(Book, book_id) # get the book by its ID
    db.session.delete(book) # delete the book from the database
    db.session.commit() # commit the changes
    return redirect(url_for("home")) # redirect to the home page


if __name__ == "__main__":
    app.run(debug=True)

