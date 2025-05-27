import json
import os

LIBRARY_FILE = 'library.txt'


class Book:
    def __init__(self, title, author, year, genre, read):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read = read

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'read': self.read
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            genre=data['genre'],
            read=data['read']
        )


class LibraryManager:
    def __init__(self):
        self.library = self.load_library()

    def load_library(self):
        if os.path.exists(LIBRARY_FILE):
            with open(LIBRARY_FILE, 'r') as f:
                data = json.load(f)
                return [Book.from_dict(book) for book in data]
        return []

    def save_library(self):
        with open(LIBRARY_FILE, 'w') as f:
            json.dump([book.to_dict() for book in self.library], f)

    def add_book(self):
        title = input("Enter the book title: ").strip()
        author = input("Enter the author: ").strip()
        year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ").strip()
        read_input = input("Have you read this book? (yes/no): ").strip().lower()
        read = read_input == 'yes'
        book = Book(title, author, year, genre, read)
        self.library.append(book)
        print("Book added successfully!\n")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ").strip().lower()
        for book in self.library:
            if book.title.lower() == title:
                self.library.remove(book)
                print("Book removed successfully!\n")
                return
        print("Book not found.\n")

    def search_books(self):
        print("Search by:\n1. Title\n2. Author")
        choice = input("Enter your choice: ").strip()
        keyword = input("Enter the keyword: ").strip().lower()
        found = []

        if choice == '1':
            found = [book for book in self.library if keyword in book.title.lower()]
        elif choice == '2':
            found = [book for book in self.library if keyword in book.author.lower()]
        else:
            print("Invalid choice.\n")
            return

        if found:
            print("\nMatching Books:")
            for i, book in enumerate(found, 1):
                status = 'Read' if book.read else 'Unread'
                print(f"{i}. {book.title} by {book.author} ({book.year}) - {book.genre} - {status}")
        else:
            print("No matching books found.")
        print()

    def display_all_books(self):
        if not self.library:
            print("Your library is empty.\n")
            return

        print("\nYour Library:")
        for i, book in enumerate(self.library, 1):
            status = 'Read' if book.read else 'Unread'
            print(f"{i}. {book.title} by {book.author} ({book.year}) - {book.genre} - {status}")
        print()

    def display_statistics(self):
        total = len(self.library)
        if total == 0:
            print("Your library is empty.\n")
            return

        read_books = sum(1 for book in self.library if book.read)
        percentage = (read_books / total) * 100
        print(f"Total books: {total}")
        print(f"Percentage read: {percentage:.1f}%\n")

    def menu(self):
        print("Welcome to your Personal Library Manager!")

        while True:
            print("Menu:")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_books()
            elif choice == '4':
                self.display_all_books()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                self.save_library()
                print("Library saved to file. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == '__main__':
    manager = LibraryManager()
    manager.menu()
