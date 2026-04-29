# Coffee Shop SQL Web App

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
- `base.html` - Shared layout template
- `index.html` - Homepage
- `menu.html` - Menu page
- `list.html` - List or data display page

## Main Application Features

The Flask app includes routes for:

- Homepage
- Menu page
- Database connection test
- Product listing and search
- Creating new products
- Editing existing products
- Deleting products
- Inventory analytics

## Database

The app connects to a MySQL database named `campuscoffee`. Product data is pulled from a `Product` table and used throughout the web app for product listings, search, updates, and inventory analytics.

## Security Note

This project uses environment variables for database credentials and secret keys. Real passwords are not included in this repository. Placeholder values in `app.py` are for local demo and development use only.

## How to Use

1. Clone or download the repository.
2. Install the required Python packages.
3. Set up a local MySQL database.
4. Update the environment variables for the database connection.
5. Run the Flask app.
6. Open the local server in a web browser.

## Example Environment Variables

```env
SECRET_KEY=your_secret_key_here
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3309
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=campuscoffee
