"""Book module - represents a book in the library"""


class Book:
    """Represents a single book"""

    def __init__(self, isbn, title, author, is_borrowed=False):
        """Create a new book
        
        Args:
            isbn (str): Book ID number
            title (str): Book name
            author (str): Who wrote it
            is_borrowed (bool): Is it borrowed? (default: False)
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def display_info(self):
        """Show book details"""
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ISBN: {self.isbn} | Title: {self.title} | "
              f"Author: {self.author} | Status: {status}")

    def mark_as_borrowed(self):
        """Mark as borrowed"""
        self.is_borrowed = True

    def mark_as_returned(self):
        """Mark as available"""
        self.is_borrowed = False

    def to_csv_row(self):
        """Convert to CSV format"""
        return [self.isbn, self.title, self.author, str(self.is_borrowed)]