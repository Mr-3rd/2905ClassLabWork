"""
Justin Third 2905, Lab 2 Q 1 8/29/2023
create an author class to build a list of published books
"""


# Create the Author class
class Author:
    def __init__(self, name):
        # create the self objects hat will hold the data
        self.name = name
        self.books = []  # blank list

    # uae the STR method to create an object that returns strings
    def __str__(self):
        # use a conditional expression to create a joined list or no books string
        book_list = ", ".join(self.books) or 'No Books'
        # provide this format string with book name and clean list of books
        return f'author: {self.name}. Books: {book_list}.'

    # create a method that will add a book a book to an author
    def publish(self, book):
        self.books.append(book)


# create a main program with sample date to test class output
def main():
    author1 = Author('James')
    print(author1)
    author1.publish('Ring Leader')
    author1.publish('Got Game')
    print(author1)


main()
