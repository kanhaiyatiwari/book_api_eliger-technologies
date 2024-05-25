# Book API Documentation

## Introduction
This project involves creating a RESTful API for managing a simple book database using Python, Flask, SQLAlchemy, and MySQL. The API supports Create, Read, Update, and Delete (CRUD) operations on book records.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8+
- MySQL
- MySQL Connector for Python
- Visual Studio Code or PyCharm

## Project Setup
1. **Install Python and MySQL:**
   - Python: Follow the installation instructions on the [Python website](https://www.python.org/downloads/).
   - MySQL: Follow the installation instructions on the [MySQL website](https://www.mysql.com/downloads/).

2. **Download and Unzip the Project:**
   - Download the `book_api.zip` file.
   - Unzip the file to a desired location using any unzipping tool (e.g., WinRAR, 7-Zip, or the built-in unzip tool on your operating system).

3. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
4. **Install Required Packages:**
  - Install the required packages using pip:
    ```bash
    pip install Flask Flask-SQLAlchemy mysql-connector-python`
 

5. **Create the MySQL Database:**
   Log in to your MySQL server and create a database:
   ```sql
   CREATE DATABASE db;

## Project Structure

book_api/
<br>
├── app.py<br>
├── config.py<br>
├── models.py<br>
└── doc.txt<br>


## Configuration

Change username and password in `config.py`. Replace `your_username` and `your_password` with your MySQL credentials.

 ## Run the Flask Application

- Run the Flask application:
  ```bash
     python app.py`
 

## Validation

To ensure data integrity and correctness, validation is performed on the incoming data. This includes:
1. **Presence Check:** Ensure all fields (title, author, isbn, publication_date) are present.
2. **Unique Constraint:** Ensure the ISBN is unique for each book.
3. **Data Type Check:** Ensure the publication date is in the correct date format.
py;
 ## Testing the API

You can use tools like Postman or cURL to test the API endpoints.

- **POST /books**
  - URL: `http://127.0.0.1:5000/books`
  - Example Body:
    ```json
    {
      "title": "Book Title",
      "author": "Author Name",
      "isbn": "1234567890123",
      "publication_date": "2023-05-01"
    }
    ```

- **GET /books/<book_id>**
  - URL: `http://127.0.0.1:5000/books/8`

- **PUT /books/<book_id>**
  - URL: `http://127.0.0.1:5000/books/8`
  - Example Body:
    ```json
    {
      "title": "Updated Book Title",
      "author": "Updated Author Name",
      "isbn": "1234567890123",
      "publication_date": "2023-05-01"
    }
    ```

- **DELETE /books/<book_id>**
  - URL: `http://127.0.0.1:5000/books/8`

 ## Features
- CRUD Operations: Create, Read, Update, and Delete book records.
- Validation: Ensures data integrity and correctness.
- Error Handling: Handles missing data, duplicate entries, and not found errors gracefully.
- Data Model: Uses SQLAlchemy ORM for defining data models and interacting with the MySQL database.






