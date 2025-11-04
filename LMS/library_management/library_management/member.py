from .book import Book


class Member:
    """
    Represents a Member in the library.

    Attributes:
        member_id (int): Unique identifier for the book.
        name (str): name of the member.
        email (str): email of the member.
        borrowed_books (bool): A list to track books borrowed by the member
    """

    def __init__(
        self, member_id: int, name: str, email: str, borrowed_books: list
    ) -> None:
        """
        Initializes a member instance.

        Args:
            member_id (int): Unique identifier for the member.
            name (str): name of the member.
            email (str): email of the member.
            borrowed_books (bool, optional): borrowed books. Defaults to True.
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        """
                Allows a member to borrow a book if it is available.

        Args:
            book (Book): The book object to borrow.

        Returns:
            str: Confirmation message if the book is borrowed, or a message if not available.

        Example:
            >>> member.borrow_book(book)
            'Book borrowed successfully'
        """
        if book.is_available():
            book.mark_borrowed()
            self.borrowed_books.append(book)
            return "Book borrowed successfully"

    def return_book(self, book: Book):
        """
                Allows the member to return a borrowed book.

        Args:
            book (Book): The book object to return.

        Returns:
            str: Confirmation message if the book is returned, or a message if the member didn't borrow it.

        Example:
            >>> member.return_book(book)
            " Vaishnavi returned 'Python Basics' successfully."
        """
        if book in self.borrowed_books:
            book.mark_returned()
            self.borrowed_books.remove(book)
            return f"{self.name} returned '{book.title}' successfully."
        else:
            return f"{self.name} did not borrow '{book.title}'."
