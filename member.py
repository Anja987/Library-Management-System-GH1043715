"""Member module - represents a library member"""


class Member:
    """Represents a library member"""

    def __init__(self, member_id, name, email):
        """Create a new member
        
        Args:
            member_id (str): Member ID
            name (str): Member's name
            email (str): Member's email
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def display_info(self):
        """Show member details"""
        book_count = len(self.borrowed_books)
        print(f"ID: {self.member_id} | Name: {self.name} | "
              f"Email: {self.email} | Books Borrowed: {book_count}")

    def borrow_book(self, isbn):
        """Add book to borrowed list"""
        self.borrowed_books.append(isbn)

    def return_book(self, isbn):
        """Remove book from borrowed list"""
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def has_borrowed(self, isbn):
        """Check if member has this book"""
        return isbn in self.borrowed_books