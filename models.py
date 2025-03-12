from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship('Book', back_populates='author', cascade="all, delete")

    @classmethod
    def create(cls, name):
        author = cls(name=name)
        session.add(author)
        session.commit()
        return author

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, author_id):
        return session.query(cls).filter_by(id=author_id).first()  

    @classmethod
    def delete_by_id(cls, author_id):
        author = session.query(cls).filter_by(id=author_id).first()
        if author:
            session.delete(author)
            session.commit()
            print("Author deleted")
        else:
            print("Author not found.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 5:
            raise ValueError("Name must be at least 5 characters long")
        self._name = new_name

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre = Column(String, nullable=True)
    pages = Column(Integer, nullable=True)
    read_status = Column(Boolean, default=False)

    @classmethod
    def create(cls, title, author, genre=None, pages=None):
        book = cls(title=title, author=author, genre=genre, pages=pages)
        session.add(book)
        session.commit()
        return book
    
    @classmethod
    def search(cls, keyword):
        return session.query(cls).filter(
            (cls.title.ilike(f"%{keyword}%")) | (cls.author.ilike(f"%{keyword}%"))
        ).all()
    
    @classmethod
    def update_read_status(cls, book, id, status):
        book = session.query(cls).filter_by(id=book_id).first()
        if book:
            book.read_status = status
            session.commit()
            print(f"Book '{book.title}' marked as {'Read' if status else 'Unread'}.")
        else:
            print("Book not found.")

    @classmethod
    def update_details(cls, book_id, new_title=None, new_author=None, new_genre=None, new_pages=None):
        book = session.query(cls).filter_by(id=book_id).first()
        if book:
            if new_title:
                book.title = new_title
            if new_author:
                book.author = new_author
            if new_genre:
                book.genre = new_genre
            if new_pages:
                book.pages = new_pages
            session.commit()
            print(f"Book '{book.id}' update succesfully.")
        else:
            print("Book not found.")

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    author = relationship('Author', back_populates='books')

engine = create_engine("sqlite:///library.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()