# Coffee Shop Flask MySQL App

This project is a Flask-based coffee shop web application with a MySQL database connection, HTML templates, product pages, and inventory analytics.

## Project Overview

The goal of this project was to build a small coffee shop web application that connects a Python Flask backend with HTML template pages and a MySQL database.

The app supports product listing, product searching, adding products, editing products, deleting products, and viewing inventory-related analytics. This project demonstrates how a simple business web app can connect front-end pages with back-end database operations.

## Built With

- Python
- Flask
- MySQL
- Flask-MySQLdb
- HTML
- CSS

## Key Features

- Flask web application structure
- MySQL database connection
- Product list and search page
- Add, edit, and delete product functionality
- Inventory analytics route
- HTML template pages
- SQL queries for product and inventory data
- Environment-based database configuration

## Skills Demonstrated

- Python web development
- Flask routing
- SQL database connection
- CRUD operations
- MySQL queries
- HTML template design
- Inventory reporting
- Web app organization
- Business data management

## Project Files

- `app.py` - Main Flask application file
- `requirements.txt` - Python package requirements
- `templates/` - HTML templates used by the Flask app, if included
- `static/` - CSS, images, and static files, if included
- `.env.example` - Example environment variable setup, if included

## Security Note

Database credentials and secret keys should be stored using environment variables. Real passwords are not included in this repository.

## Example Environment Variables

```env
SECRET_KEY=your_secret_key_here
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3309
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=campuscoffee
