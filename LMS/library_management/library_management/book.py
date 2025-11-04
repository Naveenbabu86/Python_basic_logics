class Book:
    """
    Represents a book in the library.

    Attributes:
        book_id (int): Unique identifier for the book.
        title (str): Title of the book.
        author (str): Author of the book.
        available (bool): Availability status of the book. True if the book is available, False if borrowed.
    """

    def __init__(
        self, book_id: int, title: str, author: str, available: bool = True
    ) -> None:
        """
        Initializes a new Book instance.

        Args:
            book_id (int): Unique identifier for the book.
            title (str): Title of the book.
            author (str): Author of the book.
            available (bool, optional): Availability status of the book. Defaults to True.
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        """
        Returns a string representation of the book's details.

        Returns:
            str: A formatted string containing the book's ID, title, author, and availability status.

        Example:
            >>> book.display_info()
            'Book ID: 1, Title: Python Basics, Author: Naveen, Available: True'
        """
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}"

    def mark_borrowed(self):
        """
        Marks the book as borrowed by setting its availability to False.

        Returns:
            str: Confirmation message that the book has been borrowed.

        Example:
            >>> book.mark_borrowed()
            'Book borrowed successfully.'
        """
        self.available = False
        return "Book borrowed successfully"

    def mark_returned(self):
        """
                Marks the book as returned by setting its availability to True.

        Returns:
            str: Confirmation message that the book has been returned.

        Example:
            >>> book.mark_returned()
            'Book returned successfully.'
        """
        self.available = True
        return "Book returned successfully."
    
    def is_available(self):
        """
        Checks whether the book is currently available.

        Returns:
            bool: True if the book is available, False if borrowed.

        Example:
            >>> book.is_available()
            True
        """
        return self.available
