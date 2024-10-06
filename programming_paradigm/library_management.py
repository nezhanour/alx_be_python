class Book:
    def __init__(self, title, author):
        self._is_checked_out = True
        self.title = title
        self.author = author

    def checkout_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"{self.title} by {self.author} has been borrowed"
        else:
            return f"sorry {self.title} by {self.author} is not available"
        
    def return_book(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"Thank you for returning {self.title} by {self.author}"
        else:
            return f"{self.title} by {self.author} is already available"
        
    


class Library():
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.checkout_book()

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()