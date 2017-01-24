# Main program

import ui
from book_wishlist import datastore
from book_wishlist import input_output
from book_wishlist import book


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        edit_entry()

    elif choice == '6':
        find_entry()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def edit_entry():
    book_id = ui.ask_for_book_id()
    if datastore.edit_entry(book_id):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    already_read = datastore.check_book_list(new_book.title)
    if already_read:
        ui.message('Book already read. ')
        add_anyway = ui.add_or_skip()
        if add_anyway:
            datastore.add_book(new_book)
            ui.message('Book added: ' + str(new_book))
        else:
            print('Entry Canceled')
    else:
        datastore.add_book(new_book)
        ui.message('Book added: ' + str(new_book))


def find_entry():
    '''Get info from user, find existing book'''
    book_search = ui.get_search_info()
    if datastore.find_entry(book_search):
        book = datastore.find_entry(book_search)
        ui.message('Here are the results: ')
        ui.print_results(book)
    else:
        ui.message('No results found.')


def quit():
    '''Perform shutdown tasks'''
    input_output.shutdown()
    ui.message('Bye!')


def main():

    input_output.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
