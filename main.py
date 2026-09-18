"""Main module - the main program"""

from library import Library
from book import Book
from member import Member


def print_menu():
    """Show the menu"""
    print("\n" + "="*50)
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add a new book")
    print("2. Register a new member")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Show all books")
    print("6. Show all members")
    print("7. Save and Exit")
    print("="*50)


def add_book(lib):
    """Add a new book"""
    print("\n--- Add New Book ---")
    isbn = input("Enter ISBN: ").strip()
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()

    if lib.find_book(isbn) is not None:
        print("ERROR: Book already exists!")
        return

    book = Book(isbn, title, author)
    lib.add_book(book)
    print(f"SUCCESS: Book '{title}' added!")


def register_member(lib):
    """Register a new member"""
    print("\n--- Register New Member ---")
    member_id = input("Enter member ID: ").strip()
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    if lib.find_member(member_id) is not None:
        print("ERROR: Member already exists!")
        return

    member = Member(member_id, name, email)
    lib.register_member(member)
    print(f"SUCCESS: Member '{name}' registered!")


def borrow_book(lib):
    """Borrow a book"""
    print("\n--- Borrow Book ---")
    isbn = input("Enter ISBN: ").strip()
    member_id = input("Enter member ID: ").strip()

    try:
        lib.issue_book(isbn, member_id)
        print("SUCCESS: Book borrowed!")
    except ValueError as e:
        print(f"ERROR: {e}")


def return_book(lib):
    """Return a book"""
    print("\n--- Return Book ---")
    isbn = input("Enter ISBN: ").strip()
    member_id = input("Enter member ID: ").strip()

    try:
        lib.return_book(isbn, member_id)
        print("SUCCESS: Book returned!")
    except ValueError as e:
        print(f"ERROR: {e}")


def main():
    """Main program loop"""
    lib = Library()
    lib.load_books_from_file()
    lib.load_members_from_file()

    running = True
    while running:
        print_menu()
        choice = input("Choose option (1-7): ").strip()

        try:
            choice = int(choice)
        except ValueError:
            print("ERROR: Enter a number between 1-7")
            continue

        if choice == 1:
            add_book(lib)
        elif choice == 2:
            register_member(lib)
        elif choice == 3:
            borrow_book(lib)
        elif choice == 4:
            return_book(lib)
        elif choice == 5:
            print("\n--- All Books ---")
            lib.display_all_books()
        elif choice == 6:
            print("\n--- All Members ---")
            lib.display_all_members()
        elif choice == 7:
            lib.save_books_to_file()
            lib.save_members_to_file()
            lib.save_transactions_to_file()
            print("\nDATA SAVED! Goodbye!")
            running = False
        else:
            print("ERROR: Choose 1-7")


if __name__ == "__main__":
    main()