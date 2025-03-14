from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Define the base class
Base = declarative_base()

# Database setup
engine = create_engine("sqlite:///books.db")  # SQLite database
Session = sessionmaker(bind=engine)
session = Session()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        if len(name) < 6:
            raise ValueError("Name must be at least 6 characters long")
        self.name = name

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    pages = Column(Integer, nullable=True)
    read_status = Column(String, nullable=True)  
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", backref="books")

    def get_all(self):
        return session.query(self).all()

    @classmethod
    def find_by_id(cls, book_id):
        return session.query(cls).filter_by(id=book_id).first()

    @classmethod
    def create(cls, title, author_name, genre="", pages=0, read_status="Not Started"):
        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            session.add(author)
            session.commit()

        new_book = cls(title=title, author=author, genre=genre, pages=pages, read_status=read_status)
        session.add(new_book)
        session.commit()
        return new_book

    @classmethod
    def update_details(cls, book_id, title=None, author_name=None, genre=None, pages=None, read_status=None):
        book = cls.find_by_id(book_id)
        if book:
            if title:
                book.title = title
            if author_name:
                author = session.query(Author).filter_by(name=author_name).first()
                if not author:
                    author = Author(name=author_name)
                    session.add(author)
                book.author = author
            if genre:
                book.genre = genre
            if pages is not None:
                book.pages = pages
            if read_status:
                book.read_status = read_status
            session.commit()

    @classmethod
    def delete_by_id(self):
        book = self.find_by_id(self.id)
        if book:
            session.delete(book)
            session.commit()

# Create tables
Base.metadata.create_all(engine)
