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
    """Add a new book"""
    book = Book.create(title, author, genre, pages)
    click.echo(f"Book '{book.title}' added successfully!")

@cli.command()
@click.option("--keyword", prompt="Search Keyword", help="Enter name of title or author")
def search_book(keyword):
    """search for a book with title or author"""
    book = Book.search(keyword)
    if books:
        for book in books:
            click.echo(f"{book.id}: {book.title} by {book.author}")
    else:
        click.echo("No books found.")

if __name__ == "__main__":
    cli()