from models import session, Book, Author

#INPUTTING FUNCTIONS FOR NOVEL_READER_APP BELOW:

def list_books():
    books = session.query(Book).all()

    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"{book.id}. {book.title} by {book.author.name} | Genre: {book.genre} | Pages: {book.pages} | Status: {book.read_status}")

def get_book():
    book_id = input("Enter book ID: ").strip()

    if not book_id.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

    book = Book.find_by_id(int(book_id)) # HELPS IN LOCATING BOOKS
    if book:
        print(f"ID: {book.id}\nTitle: {book.title}\nAuthor: {book.author.name}\nGenre: {book.genre}\nPages: {book.pages}\nRead Status: {book.read_status}")
    else:
        print("Book not found.")

def add_book():
    title = input("Enter book title: ").strip()
    author_name = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()
    pages = input("Enter number of pages: ").strip()
    read_status = input("Enter read status (Not Started/In Progress/Completed): ").strip()

    if not title or not author_name:
        print("Error: Title and author name are required.")
        return
    
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    # DETAILS OF THE BOOK YOU ARE ADDING 
    new_book = Book(title=title, author=author, genre=genre, pages=int(pages) if pages.isdigit() else 0, read_status=read_status)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' added successfully!")

def update_book():
    book_id = input("Enter book ID to update: ").strip()
    if not book_id.isdigit():
        print("Invalid input. Please enter the ID of the book.")
        return

    book = Book.find_by_id(int(book_id))
    if not book:
        print("ERROR: Book not found.")
        return
    # THE CODES THAT EDIT THE DETAILS OF THE CURRENT BOOK SHOWN BELOW:
    new_title = input(f"Enter new title (Current: {book.title}): ").strip() or book.title
    new_author_name = input(f"Enter new author name (Current: {book.author.name}): ").strip() or book.author.name
    new_genre = input(f"Enter new genre (Current: {book.genre}): ").strip() or book.genre
    new_pages = input(f"Enter new page count (Current: {book.pages}): ").strip() or str(book.pages)
    new_read_status = input(f"Enter new read status (Current: {book.read_status}): ").strip() or book.read_status

    author = session.query(Author).filter_by(name=new_author_name).first()
    if not author:
        author = Author(name=new_author_name)
        session.add(author)
        session.commit()

    book.title = new_title
    book.author = author
    book.genre = new_genre
    book.pages = int(new_pages) if new_pages.isdigit() else book.pages
    book.read_status = new_read_status
    session.commit()

    print(f"Book '{book.title}' updated successfully!")

def delete_book():
    book_id = input("Enter book ID to delete: ").strip()
    if not book_id.isdigit():
        print("Invalid input. Please enter a number.")
        return

    book = Book.find_by_id(int(book_id))
    if not book:
        print("Book not found.")
        return

    session.delete(book)
    session.commit()
    print(f"Book '{book.title}' deleted successfully!")

# THIS WILL help the app.py in choosing IN YOUR TERMINAL WHEN TYPING 'python app.py'
def main():
    while True:
        print("\nNovel Reader App CLI")
        print("1. List Books")
        print("2. Get Book Details")
        print("3. Add a Book")
        print("4. Update a Book")
        print("5. Delete a Book")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_books()
        elif choice == "2":
            get_book()
        elif choice == "3":
            add_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__': # you can now directly execute the script directly in your terminal
    main()
