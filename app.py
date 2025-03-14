from flask import Flask, request, jsonify
from models import session, Book, Author, b
#it helps in defining the below
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Novel Reader API!'}), 200

@app.route('/books', methods=['GET'])
def get_books():
    # i am using b as a substitute for book here
    books = b.get_all()
    return jsonify([{
        'id': b.id,
        'title': b.title,
        'author': b.author.name,
        'genre':b.genre,
        'pages': b.pages,
        'read_status': b.read_status
    } for b in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.find_by_id(book_id)
    if book:
        return jsonify({
            'id': book.id,
            'title': book.title,
            'author': book.author.name,
            'genre': book.genre,
            'pages': book.pages,
            'read_status': book.read_status
        }), 200
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Title and author are required'}), 400

    try:
        book = Book.create(
            title=data['title'],
            author_name=data['author'],
            genre=data.get('genre', ''),
            pages=data.get('pages', 0),
            read_status=data.get('read_status', 'Not Started')
        )
        return jsonify({'message': f"'{book.title}' added successfully!"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/books/<int:book_id>', methods=['PUT'])
#b_id will act as a substitution for book_id
def update_book(b_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Data not provided'}), 400
    try:
        Book.update_details(
            b_id,
            data.get('title'),
            data.get('author'),
            data.get('genre'),
            data.get('pages'),
            data.get('read_status')
        )
        return jsonify({'message': 'Book updated successfully!'}), 200
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        Book.delete_by_id(book_id)
        return jsonify({'message': 'Book deleted successfully!'}), 200
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
