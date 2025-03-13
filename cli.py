import click
from models import session, Book

@click.group()
def cli():
    """Novel Reader App"""
    pass

@cli.command()
@click.option("--title", prompt="Book Title", help="Enter the book title")
@click.option("--author", prompt="Author", help="Enter the author's name")
@click.option("--genre", default="", help="Enter the book genre")
@click.option("--pages", type=int, default=0, help="Number of pages")
def add_book(title, author, genre, pages):
    book = Book.create(title, author, genre, pages)
    click.echo(f"Book '{book.title}' added successfully!")

@cli.command()
@click.argument("keyword")
def search_book(keyword):
    books = Book.search(keyword)
    if books:
        for book in books:
            click.echo(f"{book.id}: {book.title} by {book.author}")
    else:
        click.echo("No books found.")

@cli.command()
@click.argument("book_id")
@click.argument("status")
def mark_read(book_id, status):
    Book.update_read_status(book_id, status)

@cli.command()
@click.option("--book-id", prompt="Book ID", help="Enter the ID of the book to update")
@click.option("--new-title", prompt="New Title", help="Enter the new title")
@click.option("--new-author", prompt="New Author", help="Enter the new author name")
@click.option("--new-genre", prompt="New Genre", help="Enter the new genre")
@click.option("--new-pages", prompt="New Pages", type=int, help="Enter the new number of pages")
def update_book(book_id, new_title, new_author, new_genre, new_pages):
    Book.update_details(book_id, new_title, new_author, new_genre, new_pages)

# @cli.command()
# @click.option("--book_id", type=int, prompt="BookID", help="Enter book ID to update status")
# @click.option("--status", type=bool, prompt="Mark as Read(True/False)")
# def mark_read(book_id,status):
#     Book.update_read_status(book_id, status)

@cli.command()
@click.option("--order_by", default="title", help="Sort by 'title', 'author', or 'genre'")
def sort_books(order_by):
    books = Book.sort_books(order_by)
    for book in books:
        click.echo(f"{book.id}: {book.title} by {book.author}")

@cli.command()
@click.argument("book_id", type=int)
def delete_book(book_id):
    Book.delete_by_id(book_id)


if __name__ == "__main__":
    cli()