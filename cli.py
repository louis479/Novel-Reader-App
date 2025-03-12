import click
from models import session, Book

@click.group()
def cli():
    """Novel Reader App"""
    pass

@cli.command()
@click.option("", prompt="Book Title", help="Enter the book title")
@click.option("", prompt="Author", help="Enter the author's name")
@click.option("", default="", help="Enter the book genre")
@click.option("", type=int, default=0, help="Number of pages")
def add_book(title, author, genre, pages):
    """Add a new book"""
    book = Book.create(title, author, genre, pages)
    click.echo(f"Book '{book.title}' added successfully!")