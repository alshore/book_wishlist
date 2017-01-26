from book import Book


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read + give it a rating
        4. Add book to wishlist
        5. Edit entry (author/title)
        6. Search for a book (read or unread)
        7. Delete a book from wishlist
        8. Add book rating
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    """Format and display a list of book objects"""

    if len(books) == 0:
        print ('* No books *')
        return

    for book in books:
        print(book)

    print('* {} book(s) *'.format(len(books)))

def sort_by_title(books):
    if len(books) == 0:
        print ('*No books *')
        return
    for book in books:
        booksort = books.title.sort()
        print(booksort)

def ask_for_book_id():

    ''' Ask user for book id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter book id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number: ')
        except ValueError:
            print('Please enter an integer number: ')

def ask_for_book_rating():
    rating = input('Please enter your book rating: ')
    return Book(rating)

def add_or_skip():

    add_anyway = input('Do you want to add the book anyway? (y for yes): ')

    if add_anyway == 'y':
        return True
    else:
        return False


def get_search_info():

    search = input("Enter an author or title to search for: ")
    return search


def print_results(book):

    print(book)


def get_new_book_info():

    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)

def edit(id):
    while True:
        try:
            edit = input("Do you want to change the author? (y for yes): ")
            if edit == 'y':
                book.set_author(input("Enter the name of the author: "))
                break
            else:
                edit = input("Do you want to change the title? (y for yes): ")
                if edit == 'y':
                    book.set_title(input("Enter the name of the title: "))
                    break
                else:
                    print("Sorry, I don't think you really want to change anything.")
                    break
        except ValueError:
                print("Please select which value you'd like to change using 'y'. ")


def message(msg):
    '''Display a message to the user'''
    print(msg)
