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
    

    @classmethod
    

    @classmethod
    

    @classmethod


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')

engine = create_engine("sqlite:///library.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()