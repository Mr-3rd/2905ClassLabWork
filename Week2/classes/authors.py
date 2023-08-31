class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        book_list = ", ".join(self.books) or 'No Books'
        return f'author: {self.name}. Books: {book_list}.'

    def publish(self, book):
        self.books.append(book)


def main():
    author1 = Author('James')
    print(author1)
    author1.publish('Ring Leader')
    author1.publish('Got Game')
    print(author1)


main()