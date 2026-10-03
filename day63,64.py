class Library:

    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("Books available:")
        for book in self.books:
            print(book)

    def add_book(self, book):
        self.books.append(book)
        print(book, "has been added.")


books = ["Python", "Java", "C++"]

library = Library(books)

library.display_books()

library.add_book("SQL")

library.display_books()