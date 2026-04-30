# Django Blogging Website

A full-stack blogging web application built using Django.
The backend logic and core functionality are developed manually, while the frontend templates were created with the assistance of AI tools.

## Features

* User authentication (Register, Login, Logout)
* Create, update, and delete blog posts
* User profile management
* Search functionality
* Responsive UI using Django templates

## Tech Stack

* Backend: Django
* Database: PostgreSQL
* Frontend: HTML, CSS (Django Templates)
* Environment Management: `.env` configuration

## Project Structure

```
blog/
├── blog/        # Main project settings
├── feed/        # Blog post app
├── user/        # User authentication app
├── manage.py
├── .env         # Environment variables (not included in repo)
```

## Setup Instructions

1. Clone the repository:

```
git clone https://github.com/Credence1289/Blogging--website-Django-core.git
cd Blogging--website-Django-core
```

2. Create a virtual environment:

```
python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add:

```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

5. Apply migrations:

```
python manage.py migrate
```

6. Run the server:

```
python manage.py runserver
```

## Notes

* The `.env` file is not included for security reasons.
* Ensure PostgreSQL is installed and running before setup.
* Do not use `DEBUG=True` in production.

## Author

Backend developed by Vinayak Dewoolkar
Frontend templates generated with AI assistance
