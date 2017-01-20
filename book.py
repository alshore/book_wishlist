import datetime

class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1

    def __init__(self, title, author, read=False, dateread='', id=NO_ID):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.read = read
        self.dateread = dateread
        self.id=id


    def set_id(self, id):
        self.id = id


    def __str__(self):
        read_str = 'no'
        read_date = ''
        if self.read:
            read_str = 'yes'
            read_date = datetime.date.today()

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'id: {} Title: {} Author: {} Read: {} Date: {}'
        return template.format(id_str, self.title, self.author, read_str, read_date)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.dateread == other.dateread and self.id==other.id
