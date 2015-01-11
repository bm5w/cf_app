#! /usr/bin/env python
"""Use object-oriented Python to model a public library (w/ three classes: 
    Library, Shelf, & Book). *  
The library should be aware of a number of shelves. Each shelf should know what
books it contains. Make the book object have "enshelf" and "unshelf" methods
that control what shelf the book is sitting on. The library should have a
method to report all books it contains. Note: this should *not* be a
Django (or any other) app - just a single file with three classes (plus 
commands at the bottom showing it works) is all that is needed. In addition to
pushing this python file to your Github account, please also setup a
http://repl.it/languages/Python (so it runs there) and enter the saved URL here.
"""

class Library(object):
    """The Library class is made up of shelves."""
    def __init__(self):
        self.shelves = []

    def report(self):
        """Report all books Library contains."""
        print 'This Library contains the following books:\nAuthor\t\tTitle\t\t\
        ISBN\t\tShelf'
        for shelf in self.shelves:
            for book in shelf:
                print book.output() + '\t\t{shelf}'.format(shelf=shelf)


class Shelf(object):
    """The Shelf class is made up of books."""
    def __init__(self, name, library):
        library.shelves.append(name)
        self.books = []


class Book(object):
    """A class defining each book in the library"""

    def __init__(self, author, title, ISBN):
        """Initialize a book, with Author Name, Title and ISBN"""
        self.data = {author, title, ISBN}      # A set to define the book

    def enshelf(self, shelf):
        """Add book to a particular shelf."""
        shelf.books.append(self.Book)

    def unshelf(self, shelf):
        """Remove book from shelf."""
        shelf.books.pop(self.Book)

    def output(self):
        """Return string representation of book"""
        return '{author},       {title},        {ISBN}\n'.\
            format(author=self.data[0], title=self.data[1], ISBN=self.data[2])

if __name__ == '__main__':
    """Test classes on execution."""
    a = Library()   # Create library
    shelf1 = Shelf('1', a)  # Add shelves to library
    shelf2 = Shelf('2', a)
    author_list = ['Mark Saiget', 'Joe Smith', 'Michael Creighton',
                   'Salman Rushdie', 'William Faulkner']
    title_list = ['Python', 'The Life of Nexus', 'Jurassic Park',
                  'Midnight\'s Children', 'As I Lay Dying']
    isbn_list = [1234567890, 1234567899, 1234567888,
                 1234567777, 1234566666, 1234555555]
    shelf_list = [shelf1, shelf2, shelf1, shelf2, shelf1, shelf2]
    for author, title, isbn, shelf in zip(author_list, title_list, isbn_list, shelf_list):
        Book(author, title, isbn, shelf)
