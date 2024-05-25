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
```
Change username and password in `config.py`. Replace `your_username` and `your_password` with your MySQL credentials.









