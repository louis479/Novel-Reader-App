import click
from models import Book, Author, session

@click.group()
def cli():
    """Command-line interface for managing books."""
    pass

@click.command()
def add_book():
    """Add a new book."""
    title = input("Book Title: ").strip()
    author_name = input("Author: ").strip()
    genre = input("Genre (optional): ").strip()
    pages = input("Number of pages (optional): ").strip()
    read_status = input("Read status (default 'Not Started'): ").strip()

    if not pages.isdigit() and pages:
        print("Error: Pages must be a number.")
        return

    book = Book.create(title=title, author_name=author_name, genre=genre or None, pages=int(pages) if pages else None, read_status=read_status or "Not Started")
    print(f"Book '{book.title}' by {book.author.name} added successfully!")

# use of click commands to give emphasis on the function
@click.command()
def list_books():
    """List all books in the database."""
    books = Book.get_all()
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"{book.id}. {book.title} by {book.author.name}")

@click.command()
@click.argument("book_id", type=int)
def get_book_by_id(book_id):
    """Get book details by ID."""
    book = Book.find_by_id(book_id)
    if book:
        print(f"Title: {book.title}\nAuthor: {book.author.name}\nGenre: {book.genre or 'N/A'}\nPages: {book.pages or 'N/A'}\nStatus: {book.read_status}")
    else:
        print("Book not found.")

@click.command()
@click.argument("book_id", type=int)
@click.option("--title", help="New title for the book")
@click.option("--author", help="New author name for the book")
@click.option("--genre", help="New genre")
@click.option("--pages", type=int, help="New page count")
@click.option("--status", help="New read status")
def update_book(book_id, title, author, genre, pages, status):
    """Update book details by ID."""
    updated_book = Book.update_details(book_id, title=title, author_name=author, genre=genre, pages=pages, read_status=status)
    if updated_book:
        print(f"Updated book ID {book_id}: {updated_book.title} by {updated_book.author.name}")
    else:
        print(f"Book with ID {book_id} not found.")

@click.command()
@click.argument("book_id", type=int)
def delete_book(book_id): # Delete a book by its ID.
    success = Book.delete_by_id(book_id)
    if success:
        print(f"Deleted book with ID {book_id}")
    else:
        print(f"Book with ID {book_id} not found.")

# create commands for various functions
cli.add_command(add_book)
cli.add_command(list_books)
cli.add_command(get_book_by_id)
cli.add_command(update_book)
cli.add_command(delete_book)

if __name__ == "__main__":  # you can now directly execute the script directly in your terminal
    cli()
