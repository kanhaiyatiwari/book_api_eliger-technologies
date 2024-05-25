# Book API

## Introduction
This project involves creating a RESTful API for managing a simple book database using Python, Flask, SQLAlchemy, and MySQL. The API supports Create, Read, Update, and Delete (CRUD) operations on book records.

Each book record contains the following fields:
- Title
- Author
- ISBN
- Publication Date

## Prerequisites
Before you begin, ensure you have the following installed:

1. **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2. **MySQL**: [Download MySQL](https://dev.mysql.com/downloads/mysql/)
3. **MySQL Connector for Python**: Install via pip using `pip install mysql-connector-python`
4. **Visual Studio Code or PyCharm**: For editing the code

## Project Setup

### 1. Install Python and MySQL
- **Python**: Follow the installation instructions on the [Python website](https://www.python.org/downloads/).
- **MySQL**: Follow the installation instructions on the [MySQL website](https://dev.mysql.com/downloads/mysql/).

### 2. Download and Unzip the Project
- Download the `book_api.zip` file.
- Unzip the file to a desired location using any unzipping tool (e.g., WinRAR, 7-Zip, or the built-in unzip tool on your operating system).

### 3. Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
