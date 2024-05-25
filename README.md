<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book API Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1, h2, h3 {
            color: #333;
        }
        p {
            color: #555;
        }
        code {
            background-color: #f0f0f0;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 90%;
        }
        pre {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        pre code {
            display: block;
        }
        .section {
            margin-bottom: 30px;
        }
        .endpoint {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
        }
        .highlight {
            background-color: #ffffcc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Book API Documentation</h1>
        
        <div class="section">
            <h2>Introduction</h2>
            <p>This project involves creating a RESTful API for managing a simple book database using Python, Flask, SQLAlchemy, and MySQL. The API supports Create, Read, Update, and Delete (CRUD) operations on book records.</p>
        </div>
        
        <div class="section">
            <h2>Prerequisites</h2>
            <ul>
                <li>Python 3.8+</li>
                <li>MySQL</li>
                <li>MySQL Connector for Python</li>
                <li>Visual Studio Code or PyCharm</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>Project Setup</h2>
            <ol>
                <li>Install Python and MySQL.</li>
                <li>Download and Unzip the Project.</li>
                <li>Set Up a Virtual Environment.</li>
                <li>Install Required Packages.</li>
                <li>Create the MySQL Database.</li>
            </ol>
        </div>
        
        <div class="section">
            <h2>Project Structure</h2>
            <pre><code class="language-txt">book_api/
├── app.py
├── config.py
├── models.py
└── doc.txt</code></pre>
        </div>
        
        <div class="section">
            <h2>Configuration</h2>
            <p>Change username and password in <code>config.py</code>. Replace <code>your_username</code> and <code>your_password</code> with your MySQL credentials.</p>
        </div>
        
        <div class="section">
            <h2>Validation</h2>
            <p>To ensure data integrity and correctness, validation is performed on the incoming data. This includes:</p>
            <ol>
                <li>Presence Check: Ensure all fields (title, author, isbn, publication_date) are present.</li>
                <li>Unique Constraint: Ensure the ISBN is unique for each book.</li>
                <li>Data Type Check: Ensure the publication date is in the correct date format.</li>
            </ol>
        </div>
        
        <div class="section">
            <h2>Testing the API</h2>
            <p>You can use tools like Postman or cURL to test the API endpoints.</p>
            <div class="endpoint">
                <p><strong>POST /books</strong></p>
                <p>URL: <code>http://127.0.0.1:5000/books</code></p>
                <div class="highlight">
                    <pre><code class="language-json">{
  "title": "Book Title",
  "author": "Author Name",
  "isbn": "1234567890123",
  "publication_date": "2023-05-01"
}</code></pre>
                </div>
            </div>
            <div class="endpoint">
                <p><strong>GET /books/&lt;book_id&gt;</strong></p>
                <p>URL: <code>http://127.0.0.1:5000/books/8</code></p>
            </div>
            <div class="endpoint">
                <p><strong>PUT /books/&lt;book_id&gt;</strong></p>
                <p>URL: <code>http://127.0.0.1:5000/books/8</code></p>
                <div class="highlight">
                    <pre><code class="language-json">{
  "title": "Updated Book Title",
  "author": "Updated Author Name",
  "isbn": "1234567890123",
  "publication_date": "2023-05-01"
}</code></pre>
                </div>
            </div>
            <div class="endpoint">
                <p><strong>DELETE /books/&lt;book_id&gt;</strong></p>
                <p>URL: <code>http://127.0.0.1:5000/books/8</code></p>
            </div>
        </div>
        
        <div class="section">
            <h2>Features</h2>
            <ol>
                <li>CRUD Operations: Create, Read, Update, and Delete book records.</li>
                <li>Validation: Ensures data integrity and correctness.</li>
                <li>Error Handling: Handles missing data, duplicate entries, and not found errors gracefully.</li>
                <li>Data Model: Uses SQLAlchemy ORM for defining data models and interacting with the MySQL database.</li>
            </ol>
        </div>
    </div>
</body>
</html>
