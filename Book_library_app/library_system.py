class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def addBooks(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def viewBooks(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_books(self, query):
        query = query.lower()
        found_books = [
            book
            for book in self.books
            if query in book.title.lower() or query in book.author.lower() or query in book.isbn
        ]
        if not found_books:
            print("No books found.")
        else:
            for book in found_books:
                print(book)


def main():
    library = Library()
    while True:
        print("\nLibrary Menu")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search for a book")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1, 2, 3, 4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.addBooks(book)

        elif choice == 2:
            library.viewBooks()

        elif choice == 3:
            query = input("Enter your query (title, author, or ISBN): ")
            library.search_books(query)

        elif choice == 4:
            print("Exiting the library...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
