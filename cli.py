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

    if len(author_name) < 6:
        print("Error: Author name must be at least 6 characters long.")
        return

    # Check if the author exists, if not, create a new one
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    # Create and add book
    new_book = Book(title=title, author_id=author.id)
    session.add(new_book)
    session.commit()

    print(f"Book '{title}' by {author_name} added successfully!")

@click.command()
def list_books():
    """List all books in the database."""
    books = session.query(Book).all()
    if not books:
        print("No books found.")
    else:
        for book in books:
            output = f"{book.id}. {book.title} by {book.author.name}"
            print(output)

@click.command
def get_book_by_id(book_id):
    return session.query(Book).filter_by(id=book_id).first()

@click.command()
@click.argument("book_id", type=int)
def delete_book(book_id):
    """Delete a book by its ID."""
    book = get_book_by_id(book_id)
    if not book:
        print(f"Book with ID {book_id} not found.")
        return

    session.delete(book)
    session.commit()
    print(f"Deleted book: {book.title}")

@click.command()
@click.argument("book_id", type=int)
@click.option("--title", help="New title for the book")
@click.option("--author", help="New author name for the book")
def update_book(book_id, title, author):
    """Update book details by ID."""
    book = get_book_by_id(book_id)
    if not book:
        print(f"Book with ID {book_id} not found.")
        return

    if title:
        book.title = title
    if author:
        if len(author) < 6:
            print("Error: Author name must be at least 6 characters long.")
            return

        author_obj = session.query(Author).filter_by(name=author).first()
        if not author_obj:
            author_obj = Author(name=author)
            session.add(author_obj)
            session.commit()

        book.author_id = author_obj.id

    session.commit()
    print(f"Updated book ID {book_id}: {book.title} by {book.author.name}")

cli.add_command(add_book)
cli.add_command(list_books)
cli.add_command(delete_book)
cli.add_command(update_book)

if __name__ == "__main__":
    cli()
