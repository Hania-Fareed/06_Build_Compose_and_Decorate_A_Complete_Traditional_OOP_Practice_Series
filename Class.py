class Book:
    total_books = 0  # Class variable to track the number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment count when a new book is added

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_book_count(cls):
        print(f"Total books: {cls.total_books}")

# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")

Book.display_book_count()  # Output: Total books: 2
