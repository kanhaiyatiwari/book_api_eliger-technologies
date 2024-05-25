# app.py

from flask import Flask, request, jsonify
from config import Config
from models import db, Book
from datetime import datetime
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    isbn = data.get('isbn')
    publication_date = data.get('publication_date')

    if not all([title, author, isbn, publication_date]):
        return jsonify({'error': 'Missing data'}), 400

    new_book = Book(
        title=title,
        author=author,
        isbn=isbn,
        publication_date=datetime.strptime(publication_date, '%Y-%m-%d').date()
    )

    try:
        db.session.add(new_book)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Book with this ISBN already exists'}), 409

    return jsonify({'message': 'Book created successfully', 'book': new_book.to_dict()}), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    title = data.get('title')
    author = data.get('author')
    isbn = data.get('isbn')
    publication_date = data.get('publication_date')

    if not all([title, author, isbn, publication_date]):
        return jsonify({'error': 'Missing data'}), 400

    book = Book.query.get(book_id)
    if book:
        book.title = title
        book.author = author
        book.isbn = isbn
        book.publication_date = datetime.strptime(publication_date, '%Y-%m-%d').date()

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Book with this ISBN already exists'}), 409

        return jsonify({'message': 'Book updated successfully', 'book': book.to_dict()}), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
