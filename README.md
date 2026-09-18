# Library Management System

A simple Python application for managing library books and members.

---

##  Whats in this project ?

This is a library management system that helps library staff:
1. Add new books to the library
2. Register new members
3. Let members borrow books
4. Accept returned books
5. Keep records of all activities
6. Save all data to files so it's never lost

---

## Learning Concepts

This project teaches these important programming concepts:

1. **Classes and Objects** (Book, Member, Transaction, Library classes)
2. **Methods** (functions inside classes)
3. **Control Structures** (if-else statements and loops)
4. **File Input/Output** (saving and loading CSV files)
5. **Exception Handling** (handling errors properly)
6. **Modules** (program split into multiple Python files)
7. **PEP 8 Code Style** (proper formatting and naming)


---

##  Example:- How to use

### Example 1:- Add a Book
```
Choose an option (1-7): 1

--- Add New Book ---
Enter book ISBN (unique ID): ISBN-025
Enter book title (name): Python Basics
Enter author name: Rajesh Kumar
SUCCESS: Book 'Python Basics' added successfully!
```

### Example 2: Register a Member
```
Choose an option (1-7): 2

--- Register New Member ---
Enter member ID (example: M001): M021
Enter member's full name: Aisha Patel
Enter member's email: aisha.patel@email.com
SUCCESS: Member 'Aisha Patel' registered successfully!
```

### Example 3: Borrow a Book
```
Choose an option (1-7): 3

--- Borrow a Book ---
Enter the book's ISBN: ISBN-003
Enter member ID: M001
SUCCESS: Book borrowed successfully!
```

### Example 4: Return a Book
```
Choose an option (1-7): 4

--- Return a Book ---
Enter the book's ISBN: ISBN-003
Enter member ID: M001
SUCCESS: Book returned successfully!
```

---

##  File Descriptions

| File | Purpose |
|------|---------|
| **main.py** | The main program - shows menu and handles user input |
| **book.py** | Defines the Book class |
| **member.py** | Defines the Member class |
| **transaction.py** | Defines the Transaction class (records when books are borrowed/returned) |
| **library.py** | Defines the Library class - manages everything |
| **books.csv** | Stores all book data (books.csv) |
| **members.csv** | Stores all member data (members.csv) |
| **transactions.csv** | Stores record of all borrows/returns (created automatically) |

---

##  Class Structure

### Book Class
Represents one book in the library.
- **Attributes:** isbn, title, author, is_borrowed
- **Methods:** 
  - `display_info()` - Shows book details
  - `mark_as_borrowed()` - Mark as borrowed
  - `mark_as_returned()` - Mark as available
  - `to_csv_row()` - Convert to CSV format

### Member Class
Represents one library member.
- **Attributes:** member_id, name, email, borrowed_books
- **Methods:**
  - `display_info()` - Shows member details
  - `borrow_book()` - Add book to borrowed list
  - `return_book()` - Remove book from borrowed list
  - `has_borrowed()` - Check if they have a book

### Transaction Class
Records when a book is borrowed or returned.
- **Attributes:** member_id, isbn, action, date
- **Methods:**
  - `display_info()` - Shows transaction details
  - `to_csv_row()` - Convert to CSV format
  - `from_csv_row()` - Create from CSV data

### Library Class
Manages the entire library system.
- **Attributes:** books, members, transactions
- **Methods:**
  - `add_book()` - Add a new book
  - `find_book()` - Search for a book
  - `register_member()` - Register a new member
  - `find_member()` - Search for a member
  - `issue_book()` - Borrow a book
  - `return_book()` - Return a book
  - `display_all_books()` - Show all books
  - `display_all_members()` - Show all members
  - `save_books_to_file()` - Save books
  - `load_books_from_file()` - Load books
  - And more file operations...

---


### books.csv
Stores information about all books:
```
isbn,title,author,is_borrowed
ISBN-001,Malgudi Days,R.K. Narayan,False
ISBN-002,Python Basics,Rajesh Kumar,True
```

### members.csv
Stores information about all members:
```
member_id,name,email,borrowed_books
M001,Rajesh Kumar,rajesh@email.com,ISBN-002
M002,Priya Sharma,priya@email.com,
```





---

##  Author

Anjali.

---

