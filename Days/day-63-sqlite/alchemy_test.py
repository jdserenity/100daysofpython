from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase): pass

db = SQLAlchemy(model_class=Base)

# create the app, configure the SQLite database, relative to the app instance folder
app = Flask(__name__); app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

# delete entire database
def delete_db():
    db.drop_all()

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

def create_db():
    db.create_all()

def add_book(title, author, rating):
    new_book = Books(id=1, title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()

def read_all_books():
    for book in db.session.query(Books).all():
        print(f"{book.title} by {book.author}, rating: {book.rating}")

def query_books_by_title(title):
    return db.session.execute(db.select(Books).where(Books.title == title)).scalar()

def query_books_by_author(author):
    return db.session.execute(db.select(Books).where(Books.author == author)).scalar()

def query_books_by_rating(rating):
    return db.session.execute(db.select(Books).where(Books.rating == rating)).scalar()

def main():
    with app.app_context():
        # read_all_books()
        print(query_books_by_author("J. K. Rowling"))
        
if __name__ == "__main__":
    main()