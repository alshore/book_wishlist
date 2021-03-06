import datetime
import os
from book import Book

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0


def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    try:
        with open(BOOKS_FILE_NAME) as f:
            data = f.read()
            make_book_list(data)
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass


    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        f.write(output_data)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [book for book in book_list if book.read == kwargs['read']]
        return read_books



def add_book(book):
    ''' Add to db, set id value, return Book'''
    global book_list

    book.id = generate_id()
    book_list.append(book)

def delete_book(book):
    global book_list
    book_list.remove(book)

def check_book_list(book_title):

    global book_list

    for book in book_list:

        if book.title == book_title:
            return True
        else:
            return False


def generate_id():
    global counter
    counter += 1
    return counter


def edit_entry(book_id):

    global book_list

    for book in book_list:

        if book.id == book_id:
            edit = input("Do you want to change the author? (y for yes): ")
            if edit == 'y':
                book.set_author(input("Enter the name of the author: "))
            else:
                edit = input("Do you want to change the title? (y for yes): ")
                if edit == 'y':
                    book.set_title(input("Enter the name of the title: "))
            return True

        else:
            raise ValueError("Didn't find that book ID.")


def find_entry(book_search):

    global book_list

    for book in book_list:

        if book.title == book_search or book.author == book_search:
            return book


def set_read(book_id, read):
    """Update book with given book_id to read. Return True if \
    book is found in DB and update is made, False otherwise."""

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.date_read = datetime.date.today()
            book.read = True
            return True

    return False # return False if book id is not found

def set_rating(book_id, rating):
    global book_list
    for book in book_list:
        if book.id == book_id:
            book.rating = rating
            return True
    return False

def make_book_list(string_from_file):
    ''' turn the string from the file into a list of Book objects'''

    global book_list

    books_str = string_from_file.split('\n')

    for book_str in books_str:
        data = book_str.split(separator)
        book = Book(data[0], data[1], data[2] == 'True', data[3], int(data[4]), int(data[5]))
        book_list.append(book)


def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    for book in book_list:
        output = [ book.title, book.author, str(book.read), str(book.date_read), str(book.id), str(book.rating) ]
        output_str = separator.join(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string
