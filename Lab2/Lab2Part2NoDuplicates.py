"""
Justin Third 2905, Lab 2 Q 2 8/29/2023
create an author class to build a list of published books that are not duplicated
"""


class Author:
    def __init__(self, name):  # I tried Books = [] here and the pycharm ide commented on using a "mutable" object
        self.name = name
        # use a set as the object that books are added too, this does not allow duplicates
        self.books = set()

    def __str__(self):
        book_list = ", ".join(self.books) or 'No Books'
        return f'Author: {self.name}. Books: {book_list}.'

    def publish(self, book):
        # If the book is in the set
        if book in self.books:
            # Display an error message
            print(f'{book} is already in the system.')
        else:
            # Everything else is correct
            self.books.add(book)
            print(f'{book} added to Author')

        # my original method included a check system to find the book. classmates in breakout showed me the simpler way
        # # Utilize a list comprehension to find any matching titles of the book being added
        # book_in_set = [title for title in self.books if book in title]
        # # If the book is in the set
        # if book_in_set:
        #     # Display an error message
        #     print(f'{book} is already in the system.')
        # else:
        #     # Everything else is correct
        #     self.books.add(book)
        #     print(f'{book} added to Author')

        # originally I had kept the list and converted it to a set upon each publication,
        # this probably had a vulnerability somewhere
        # self.books = list(set(self.books))


def main():
    author1 = Author('James')
    print(author1)
    author1.publish('Ring Leader')
    author1.publish('Got Game')

    # add a bunch of duplicates
    author1.publish('Ring Leader')
    author1.publish('Got Game')
    author1.publish('Ring Leader')
    author1.publish('Got Game')
    author1.publish('Ring Leader')
    print(author1)

    # add two more books
    author1.publish('Programming Guide')
    author1.publish('I think I\'m ALL THAT')
    print(author1)


if __name__ == '__main__':
    main()
