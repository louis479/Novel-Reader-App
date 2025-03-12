import click
from models import session, Book

@click.group()
def cli():
    """Novel Reader App"""
    pass

