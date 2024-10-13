import sqlite3

def main():
    db = sqlite3.connect("books-collection.db")
    cursor = db.cursor()
    try:
        cursor.execute("CREATE TABLE books ( \
                        id INTEGER PRIMARY KEY, \
                        title varchar(250) NOT NULL UNIQUE, \
                        author varchar(250) NOT NULL, \
                        rating FLOAT NOT NULL \
                       )")
    except sqlite3.OperationalError:
        pass
    
    try:
        cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
        db.commit()
    except sqlite3.IntegrityError:
        print("Book already exists.")
    
    db.close()

if __name__ == "__main__":
    main()
