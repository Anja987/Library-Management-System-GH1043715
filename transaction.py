"""Transaction module - records borrow/return activities"""

from datetime import datetime


class Transaction:
    """Records a borrow or return event"""

    def __init__(self, member_id, isbn, action, date=None):
        """Create a transaction record
        
        Args:
            member_id (str): Who did it
            isbn (str): Which book
            action (str): BORROW or RETURN
            date (str): When (default: now)
        """
        self.member_id = member_id
        self.isbn = isbn
        self.action = action
        
        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        else:
            self.date = date

    def display_info(self):
        """Show transaction details"""
        print(f"[{self.date}] Member {self.member_id} {self.action} "
              f"book {self.isbn}")

    def to_csv_row(self):
        """Convert to CSV format"""
        return [self.member_id, self.isbn, self.action, self.date]