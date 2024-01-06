# Flask Task Master

A task management web application built with Flask, SQLAlchemy, and SQLite.

## Technologies Used

- **Flask** 
- **SQLAlchemy**
- **SQLite**
- **HTML & CSS**
- **Jinja2**

## Features

- Create new tasks
- Update existing tasks
- Delete tasks

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/flask-task-master.git
    ```
2. Change into the directory:
    ```bash
    cd flask-task-master
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # Unix or MacOS
    venv\Scripts\activate  # Windows
    ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set the Flask application environment variable:
    ```bash
    export FLASK_APP=app  # Unix or MacOS
    set FLASK_APP=app  # Windows
    ```
2. Run the Flask application:
    ```bash
    flask run
    ```

Open your web browser and visit `http://localhost:5000` to use the application.

## Deployment

This application includes a `Procfile` for deployment to platforms like Heroku. The application uses Gunicorn as the WSGI HTTP server when deployed.
