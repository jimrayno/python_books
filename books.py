#book functions together here

import sqlite3

# Function to create a table in the database to store book information.
def make_book_tab(database):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        # SQL command to create a table named 'books' with four columns: id, title, author, and status.
        # 'id' is set as the primary key.
        cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, status TEXT)')
        # The following are examples of other SQL operations you might perform, currently commented out.
        # Insert example data into the books table.
        # cursor.execute('INSERT INTO books (title, author, status) VALUES (?, ?, ?)', ('Propast casu', 'Bures', 'reading'))
        # Update operation example for a table named 'students'.
        # cursor.execute("UPDATE students SET age = ? WHERE name = ?", (100, 'Bob'))

# Function to insert a new book record into the books table.
def insert_book(database, name, author, status):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        # SQL command to insert the provided book details into the books table.
        cursor.execute('INSERT INTO books (title, author, status) VALUES (?, ?, ?)', (name, author, status))

# Function to retrieve and display all book records from the books table.
def retrieve_book(database):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        # SQL command to select all records from the books table.
        cursor.execute('SELECT * FROM books')
        # Fetches all the rows from the query result and prints them.
        for row in cursor.fetchall():
            print(row)

# Function to delete a book record from the books table based on its ID.
def delete_book(database, book_id):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        # SQL command to delete the book record whose ID matches the provided book_id.
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        # Confirmation message after deleting the book.
        print(f"Book with id {book_id} has been deleted.")

# Function to search for books in the books table based on a search term.
def search_books(database, search_term):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        # SQL query to find books where the author, title, or status matches the search term.
        query = 'SELECT * FROM books WHERE author = ? OR title = ? OR status = ?'
        cursor.execute(query, (search_term, search_term, search_term))
        result = cursor.fetchall()
        # Check if the search returned any results.
        if not result:
            return 'Nothing found'
        else:
            return result

#calling the functions above all together here
# Define a function called choice_menu that takes an option as an argument
def choice_menu(option):
    # Print the menu options
    print('1 for creating a database')
    print('2 for showing all')
    print('3 for full-text search')
    print('4 for deleting a record')
    print('5 for creating a record')

    # Set the database filename
    database = 'books.db'

    try:
        # Use a "match" statement to handle different options
        match int(option):
            case 1:
                # Call a function to create a book table in the database
                make_book_tab(database)
                print("Database created.")
            case 2:
                # Call a function to retrieve and display all books from the database
                retrieve_book(database)  # reads book database
            case 3:
                # Ask the user for a search term and call a function to search for books
                search_term = input('Enter search term: ')
                results = search_books(database, search_term)
                if results:
                    for book in results:
                        print(book)
                else:
                    print("No books found.")
            case 4:
                # Ask the user for the ID of the book to delete and call a function to delete it
                deleted_row = int(input('Enter the ID of the book to delete: '))
                delete_book(database, deleted_row)
            case 5:
                # Ask the user for book details and call a function to insert the book into the database
                name, author, status = input('Enter title, author, status separated by commas: ').split(',')
                insert_book(database, name.strip(), author.strip(), status.strip())
                print("Book record created.")
            case _:
                # Handle an invalid choice
                print("Invalid choice.")
    except ValueError:
        # Handle the case where the user enters an invalid number
        print("Please enter a valid number.")

# Example usage
# Ask the user for an option and call the choice_menu function with the chosen option
user_option = input("Select an option: ")
choice_menu(user_option)
