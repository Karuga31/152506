class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} doesn't have '{book.title}'")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print("No books borrowed.")


# Interactive test
book1 = Book("Python Basics", "John Doe")
book2 = Book("OOP in Python", "Jane Smith")
member = LibraryMember("Esther", "152506")

while True:
    print("\n1. Borrow Book\n2. Return Book\n3. List Books\n4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        title = input("Enter title: ")
        if title == book1.title:
            member.borrow_book(book1)
        elif title == book2.title:
            member.borrow_book(book2)
        else:
            print("Book not found.")
    elif choice == "2":
        title = input("Enter title to return: ")
        if title == book1.title:
            member.return_book(book1)
        elif title == book2.title:
            member.return_book(book2)
        else:
            print("Book not found.")
    elif choice == "3":
        member.list_borrowed_books()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
