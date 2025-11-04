from .book import Book
from .member import Member


class Library:
    """
    Manages the members and books in a library.

    Attributes:
        books (list): List of Book objects in the library.
        members (list): List of Member objects in the library.
    """

    def __init__(self, books: list = None, members: list = None) -> None:
        """
        Initializes a Library instance.

        Args:
            books (list, optional): List of Book objects. Defaults to empty list.
            members (list, optional): List of Member objects. Defaults to empty list.
        """
        self.books = books if books is not None else []
        self.members = members if members is not None else []

    def add_book(self, book: Book):
        """
            Adds a Book object to the library's collection.

        Args:
            book (Book): The book object to be added to the library.

        Returns:
            str: Confirmation message indicating the book has been successfully added.

        Example:
            >>> book = Book(1, "Python Basics", "Naveen")
            >>> library.add_book(book)
            "Book 'Python Basics' added successfully."
        """
        self.books.append(book)
        return f"{book.title} appended successfully"

    def add_member(self, member: Member):
        """
            Adds a Member object to the library's member list.

        Args:
            member (Member): The member object to be added to the library.

        Returns:
            str: Confirmation message indicating the member has been successfully added.

        Example:
            >>> member = Member(101, "Vaishnavi", "vaishnavi@example.com")
            >>> library.add_member(member)
            "Member 'Vaishnavi' added successfully."
        """
        self.members.append(member)
        return f"{member.name} added successfully"

    def find_book_by_id(self, book_id: int):
        """
             Finds and returns a Book object from the library by its ID.

        Args:
            book_id (int): The ID of the book to search for.

        Returns:
            Book: The book object with the matching ID, or None if not found.

        Example:
            >>> library.find_book_by_id(1)
            <Book object at 0x...>
        """

        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member_by_id(self, member_id: int):
        """
        Finds and returns a Member object from the library by its ID.

        Args:
            member_id (int): The ID of the member to search for.

        Returns:
            Member: The member object with the matching ID, or None if not found.

        Example:
            >>> member = library.find_member_by_id(101)
            >>> print(member.name)
            "Vaishnavi"
        """
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_all_books(self):
        """
             Displays the details of all books in the library.

        For each book in the library, this method prints a string containing:
        - Book ID
        - Title
        - Author
        - Availability status

        Example:
            >>> library.display_all_books()
            Book ID: 1, Title: Python Basics, Author: Naveen, Available: True
            Book ID: 2, Title: Data Science, Author: Aisha, Available: False
        """
        for book in self.books:
            print(book.display_info())

    def display_all_members(self):
        """
        Displays the details of all members in the library.

        For each member in the library, this method prints a string containing:
        - Member ID
        - Name
        - Email
        - Number of books currently borrowed

        Example:
            >>> library.display_all_members()
            Member ID: 101, Name: Vaishnavi, Email: vaishnavi@example.com, Borrowed Books: 2
            Member ID: 102, Name: Megha, Email: megha@example.com, Borrowed Books: 0
        """
        for member in self.members:
            print(
                f"Member ID: {member.member_id}, Name: {member.name}, Email: {member.email}, Borrowed Books: {len(member.borrowed_books)}"
            )

    def borrow_book(self, member_id: int, book_id: int):
        """
        Allows a member to borrow a book from the library.

        This method checks if the member and book exist in the library and whether
        the book is available. If all conditions are met, it marks the book as borrowed
        and adds it to the member's borrowed books list.

        Args:
            member_id (int): The unique ID of the member borrowing the book.
            book_id (int): The unique ID of the book to be borrowed.

        Returns:
            str: A message indicating the result of the borrow operation.
                - "Member not found." if the member doesn't exist.
                - "Book not found." if the book doesn't exist.
                - "'<book_title>' is already borrowed." if the book is not available.
                - "Member <member_name> borrowed '<book_title>' successfully." if borrowed successfully.

        Example:
            >>> library.borrow_book(101, 1)
            "Member Vaishnavi borrowed 'Python Basics' successfully."
        """
        member = self.find_member_by_id(member_id)
        if not member:
            return "Member not found."

        book = self.find_book_by_id(book_id)
        if not book:
            return "Book not found."

        if not book.is_available():
            return f"'{book.title}' is already borrowed."

        member.borrow_book(book)
        return f"Member {member.name} borrowed '{book.title}' successfully."

    def return_book(self, member_id: int, book_id: int):
        """
                Allows a member to return a borrowed book to the library.

        This method verifies that both the member and the book exist in the library system.
        If the member has borrowed the specified book, it processes the return by
        calling the member's `return_book` method and updates the book's availability status.

        Args:
            member_id (int): Unique ID of the member returning the book.
            book_id (int): Unique ID of the book being returned.

        Returns:
            str: A message indicating the outcome of the return process.
                - "Member not found." if the member does not exist.
                - "Book not found." if the book does not exist.
                - "Member did not borrow this book." if the member hasn’t borrowed the book.
                - "Member <member_name> returned '<book_title>' successfully." if the return is successful.

        Example:
            >>> library.return_book(101, 1)
            "Member Vaishnavi returned 'Python Basics' successfully."

        """

        member = self.find_member_by_id(member_id)
        if not member:
            return "Member not found."
        
        book = self.find_book_by_id(book_id)
        if not book:
            return "Book not found."
        
        result = member.return_book(book)
        return result
        # return f"Member {member.name} returned '{book.title}' successfully."


