# Novel-Reader-App

## Description

The **Novel Reader App** is a command-line application that allows users to manage and read novels easily. Users can add, list, update, Mark Read/Unread and delete books from the database, keeping track of authors and other details. The app leverages Python and SQLAlchemy for data management and uses Click for a user-friendly command-line interface.

---

## Features

These are the following features present in my project:

- **Add a New Book**: Users can add a book along with the author's name.
- **List All Books**: View all stored books with details.
- **Update Book Details**: Modify the book title or author.
- **Delete a Book**: Remove a book from the database.
- **Search Functionality**: Implement book search by title or author.
- **Mark Book as Read or Unread**: Can mark the book to match the book status as user.

---

## Technologies Used

Here are the following:

- **Python**
- **SQLAlchemy** (for database interactions)
- **Click** (for command-line interface)
- **SQLite** (default database, can be changed)

---

## Project Structure

This is my project structure for Novel Reader App

```

Novel-Reader-App/
│── venv             # virtual environment
│── models.py        # Defines the Book and Author models
│── cli.py           # Command-line interface for interacting with the app
│── books.py         # Handles database connections
│── app.py           # Handles Api Request
│── README.md        # Documentation
│── requirements.txt # Dependencies
```

---

## Installation & Setup

### 1. Clone the Repository

```sh
git clone FinalProject
cd Novel-Reader-App
```

### 2. Create a Virtual Environment

First ensure that you have activated your python environment

```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies

Then ensure to install the necessary dependencies

```sh
pip install -r requirements.txt
```

### 4. Initialize the Database

Then finally in your terminal type python and click enter. Then import the following below:

```sh
python
>>> from models import session
>>> session.commit()
>>> exit()
```

---

## How to Run the code

Here are the steps:

1. Run the App.py

First run the app.py to get the view of what the code does.

```sh
python app.py
```

### 2.Run the CLI

Then run the Cli to mange the books from the terminal

```sh
python cli.py --help
```

### 2.Add a Book

Use the cli to add books

```sh
python cli.py add-book
```

### 3.List All Books

Use the cli to list the books added

```sh
python cli.py list-books
```

### 4.Update a Book

Use the cli to update the books you selected

```sh
python cli.py update-book <book_id> --title "New Title" --author "New Author"
```

### 5.Delete a Book

Use the cli to delete the books you selected

```sh
python cli.py delete-book <book_id>
```

### 5.View the books

- To view the books added and its changes, check your browser in the link given in your terminal. It will give you

```sh
python flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

- It will give you a Welcome message.

```sh
{"message":"Welcome to the Novel Reader API!"}
```

- Then on the url page add ***/books***  in your <http://127.0.0.1:5000> to form <http://127.0.0.1:5000/books> to see the list

**Example:**

```sh
[{"author":"Danielle steel","genre":"Romance","id":1,"pages":567,"read_status":"Reading","title":"The House"},
{"author":"William robert","genre":"Fiction","id":2,"pages":1230,"read_status":"Reading","title":"Space Ranger"},
{"author":"Joestar Mary","genre":"Romance","id":3,"pages":340,"read_status":"Reading","title":"Melody"}]
```

---

## Conclusion

Thank you for taking your time in looking through this project.

Have a blessed Day.
