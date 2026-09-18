"""Library module  manages everything"""

import csv
import os
from book import Book
from member import Member
from transaction import Transaction


class Library:
    """Manages the library system"""

    def __init__(self, books_file="books.csv", members_file="members.csv",
                 transactions_file="transactions.csv"):
        """Create a new library
        
        Args:
            books_file (str): File to store books
            members_file (str): File to store members
            transactions_file (str): File to store transactions
        """
        self.books = []
        self.members = []
        self.transactions = []
        self.books_file = books_file
        self.members_file = members_file
        self.transactions_file = transactions_file

    def add_book(self, book):
        """Add a book to library"""
        self.books.append(book)

    def find_book(self, isbn):
        """Find a book by ISBN"""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def register_member(self, member):
        """Register a new member"""
        self.members.append(member)

    def find_member(self, member_id):
        """Find a member by ID"""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def issue_book(self, isbn, member_id):
        """Borrow a book"""
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if book is None:
            raise ValueError(f"Book with ISBN {isbn} not found!")
        if member is None:
            raise ValueError(f"Member with ID {member_id} not found!")
        if book.is_borrowed:
            raise ValueError(f"Book '{book.title}' is already borrowed!")

        book.mark_as_borrowed()
        member.borrow_book(isbn)
        transaction = Transaction(member_id, isbn, "BORROW")
        self.transactions.append(transaction)

    def return_book(self, isbn, member_id):
        """Return a book"""
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if book is None:
            raise ValueError(f"Book with ISBN {isbn} not found!")
        if member is None:
            raise ValueError(f"Member with ID {member_id} not found!")
        if not member.has_borrowed(isbn):
            raise ValueError(f"Member {member_id} didn't borrow this book!")

        book.mark_as_returned()
        member.return_book(isbn)
        transaction = Transaction(member_id, isbn, "RETURN")
        self.transactions.append(transaction)

    def display_all_books(self):
        """Show all books"""
        if not self.books:
            print("No books in library yet.")
            return
        for book in self.books:
            book.display_info()

    def display_all_members(self):
        """Show all members"""
        if not self.members:
            print("No members registered yet.")
            return
        for member in self.members:
            member.display_info()

    def save_books_to_file(self):
        """Save books to CSV"""
        with open(self.books_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["isbn", "title", "author", "is_borrowed"])
            for book in self.books:
                writer.writerow(book.to_csv_row())

    def load_books_from_file(self):
        """Load books from CSV"""
        try:
            with open(self.books_file, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                self.books = []
                for row in reader:
                    if len(row) == 4:
                        isbn, title, author, is_borrowed = row
                        book = Book(isbn, title, author, is_borrowed == "True")
                        self.books.append(book)
        except FileNotFoundError:
            print(f"File '{self.books_file}' not found. Starting fresh.")
            self.books = []

    def save_members_to_file(self):
        """Save members to CSV"""
        with open(self.members_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["member_id", "name", "email", "borrowed_books"])
            for member in self.members:
                borrowed = ";".join(member.borrowed_books)
                writer.writerow(
                    [member.member_id, member.name, member.email, borrowed])

    def load_members_from_file(self):
        """Load members from CSV"""
        try:
            with open(self.members_file, "r", newline="",
                      encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                self.members = []
                for row in reader:
                    if len(row) == 4:
                        member_id, name, email, borrowed = row
                        member = Member(member_id, name, email)
                        if borrowed:
                            member.borrowed_books = borrowed.split(";")
                        self.members.append(member)
        except FileNotFoundError:
            print(f"File '{self.members_file}' not found. Starting fresh.")
            self.members = []

    def save_transactions_to_file(self):
        """Save transactions to CSV"""
        file_exists = os.path.isfile(self.transactions_file)
        with open(self.transactions_file, "a", newline="",
                  encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["member_id", "isbn", "action", "date"])
            for transaction in self.transactions:
                writer.writerow(transaction.to_csv_row())
        self.transactions = []