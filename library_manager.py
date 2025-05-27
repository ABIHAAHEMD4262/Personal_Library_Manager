import json
import csv

class Book:
    def __init__(self, title, author, year, genre, read):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read = read

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "read": self.read
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data['title'],
            data['author'],
            data['year'],
            data['genre'],
            data['read']
        )


class LibraryManager:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read = input("Have you read this book? (yes/no): ").lower() == 'yes'
        self.books.append(Book(title, author, year, genre, read))
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found.")

    def search_book(self):
        print("Search by:\n1. Title\n2. Author")
        choice = input("Enter your choice: ")
        keyword = input("Enter the search keyword: ").lower()
        matches = []
        if choice == '1':
            matches = [book for book in self.books if keyword in book.title.lower()]
        elif choice == '2':
            matches = [book for book in self.books if keyword in book.author.lower()]
        else:
            print("Invalid choice.")
            return

        if matches:
            for i, book in enumerate(matches, 1):
                self.display_book(i, book)
        else:
            print("No matching books found.")

    def display_all_books(self):
        if not self.books:
            print("Library is empty.")
            return
        for i, book in enumerate(self.books, 1):
            self.display_book(i, book)

    def display_statistics(self):
        total = len(self.books)
        read = sum(book.read for book in self.books)
        percent = (read / total * 100) if total else 0
        print(f"Total books: {total}")
        print(f"Percentage read: {percent:.1f}%")

    def filter_books(self):
        print("Filter by:\n1. Genre\n2. Year")
        choice = input("Enter your choice: ")
        if choice == '1':
            genre = input("Enter genre: ").lower()
            filtered = [b for b in self.books if b.genre.lower() == genre]
        elif choice == '2':
            year = int(input("Enter year: "))
            filtered = [b for b in self.books if b.year == year]
        else:
            print("Invalid choice.")
            return
        if filtered:
            for i, book in enumerate(filtered, 1):
                self.display_book(i, book)
        else:
            print("No books match the filter.")

    def export_to_csv(self):
        with open("books.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "author", "year", "genre", "read"])
            writer.writeheader()
            for book in self.books:
                writer.writerow(book.to_dict())
        print("Books exported to books.csv")

    def save_books(self):
        with open("library.json", "w") as f:
            json.dump([book.to_dict() for book in self.books], f)

    def load_books(self):
        try:
            with open("library.json", "r") as f:
                self.books = [Book.from_dict(b) for b in json.load(f)]
        except FileNotFoundError:
            self.books = []

    def display_book(self, index, book):
        status = "Read" if book.read else "Unread"
        print(f"{index}. {book.title} by {book.author} ({book.year}) - {book.genre} - {status}")

    def menu(self):
        while True:
            print("\nMenu")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Filter books")
            print("7. Export to CSV")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_all_books()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                self.filter_books()
            elif choice == '7':
                self.export_to_csv()
            elif choice == '8':
                self.save_books()
                print("Library saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = LibraryManager()
    manager.menu()
