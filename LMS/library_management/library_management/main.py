from .library import Library
from .book import Book
from .member import Member


def main():
    library = Library()

    # Optional: Preload some books and members
    book1 = Book(1, "Python Basics", "Naveen")
    book2 = Book(2, "Data Science Essentials", "Aisha")
    book3 = Book(3, "AI Fundamentals", "Anjali")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    member1 = Member(member_id=101, name="Vaishnavi", email="vaishnavi@example.com", borrowed_books=[])
    member2 = Member(member_id=102, name="Megha", email="megha@example.com", borrowed_books=[])
    library.add_member(member1)
    library.add_member(member2)

    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Display All Members")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            book = Book(book_id, title, author)
            print(library.add_book(book))

        elif choice == "2":
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Member Name: ")
            email = input("Enter Member Email: ")
            member = Member(member_id, name, email, borrowed_books=[])
            print(library.add_member(member))

        elif choice == "3":
            member_id = int(input("Enter Member ID: "))
            book_id = int(input("Enter Book ID: "))
            print(library.borrow_book(member_id, book_id))

        elif choice == "4":
            member_id = int(input("Enter Member ID: "))
            book_id = int(input("Enter Book ID: "))
            print(library.return_book(member_id, book_id))

        elif choice == "5":
            library.display_all_books()

        elif choice == "6":
            library.display_all_members()

        elif choice == "7":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
