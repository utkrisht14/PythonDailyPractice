class Book:
    def __init__(self, title: str, author: str, is_available: bool = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        availability = "Yes" if self.is_available else "No"
        return f"Title: {self.title}, Author: {self.author}, Available: {availability}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        for existing_book in self.books:
            if existing_book.title.lower() == book.title.lower():
                print("Book already exists")
                return

        self.books.append(book)
        print("Book added successfully")

    def view_books(self):
        if not self.books:
            print("No books available")
            return

        for book in self.books:
            print(book)

    def borrow_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print("Book borrowed successfully")
                else:
                    print("Book is already borrowed")
                return  # correct place

        print("Book not found")

    def return_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully")
                else:
                    print("Book was not borrowed")
                return  # correct place

        print("Book not found")