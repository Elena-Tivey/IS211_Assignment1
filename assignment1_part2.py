class Book:
    """Represents a book with an author and a title."""
    author = ""
    title = ""

    def __init__(self, author, title):
        """
        Initialize a Book object with the given author and title.
        """
        self.author = author
        self.title = title
    
    def display(self):
        """
        Print a string for book in the following form: "title, written by author"
        """
        print(f"{self.title}, written by {self.author}")

if __name__ == "__main__":
    book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe: A Romance")

    books = [book1, book2]

    for book in books:
        book.display()
