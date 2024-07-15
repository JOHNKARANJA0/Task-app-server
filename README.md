# Task Management App Backend 

## Overview

Task Management App is a web application designed to help users manage their tasks and assignments. The application provides functionalities for user authentication, task management, and assignment tracking. It is built with Flask for the backend and integrates with a React frontend.

## Features

- User authentication (login, logout, session management)
- User registration
- Task management (create, read, update, delete tasks)
- Assignment management (create, read assignments)
- Protected routes for authenticated users

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-Session
- Flask-CORS
- Flask-RESTful
- Postgrsql

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/john7319/Task-app-server.git
    cd task-app-server
    ```

2. **Create and activate a virtual environment:**

    ```sh
    pipenv --python /usr/bin/python
    pipenv install
    pipenv shell
    ```

3. **Install the dependencies:**

    ```sh
    pipenv install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root and add your database URI:

    ```sh
    DATABASE_URI=sqlite:///app.db
    ```

5. **Initialize the database:**

    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

## Running the Application

1. **Start the Flask development server:**

    ```sh
    flask run or python3 app.py
    ```

    The application will be available at `http://localhost:5000`.

## API Endpoints

### Authentication

- **POST /login**

    Request:

    ```json
    {
        "email": "user@example.com",
        "password": "password"
    }
    ```

    Response:

    ```json
    {
        "id": 1,
        "name": "User Name",
        "email": "user@example.com"
    }
    ```

- **DELETE /logout**

    Response: `204 {}`

- **GET /check_session**

    Response:

    ```json
    {
        "id": 1,
        "name": "User Name",
        "email": "user@example.com"
    }
    ```

### Users

- **GET /users**

    Response:

    ```json
    [
        {
            "id": 1,
            "name": "User Name",
            "email": "user@example.com"
        }
    ]
    ```

- **POST /users**

    Request:

    ```json
    {
        "name": "New User",
        "email": "newuser@example.com"
    }
    ```

    Response:

    ```json
    {
        "id": 2,
        "name": "New User",
        "email": "newuser@example.com"
    }
    ```

- **GET /users/<id>**

    Response:

    ```json
    {
        "id": 1,
        "name": "User Name",
        "email": "user@example.com"
    }
    ```

- **DELETE /users/<id>**

    Response: `204 ''`

### Tasks

- **GET /tasks**

    Response:

    ```json
    [
        {
            "id": 1,
            "title": "Task Title",
            "description": "Task Description",
            "due_date": "2023-07-14",
            "user_id": 1
        }
    ]
    ```

- **POST /tasks**

    Request:

    ```json
    {
        "title": "New Task",
        "description": "Task Description",
        "due_date": "2023-07-14",
        "user_id": 1
    }
    ```

    Response:

    ```json
    {
        "id": 2,
        "title": "New Task",
        "description": "Task Description",
        "due_date": "2023-07-14",
        "user_id": 1
    }
    ```

- **GET /tasks/<id>**

    Response:

    ```json
    {
        "id": 1,
        "title": "Task Title",
        "description": "Task Description",
        "due_date": "2023-07-14",
        "user_id": 1
    }
    ```

- **PATCH /tasks/<id>**

    Request:

    ```json
    {
        "title": "Updated Task Title",
        "description": "Updated Task Description",
        "due_date": "2023-07-15"
    }
    ```

    Response:

    ```json
    {
        "id": 1,
        "title": "Updated Task Title",
        "description": "Updated Task Description",
        "due_date": "2023-07-15",
        "user_id": 1
    }
    ```

- **DELETE /tasks/<id>**

    Response: `204 ''`

### Assignments

- **GET /assignments**

    Response:

    ```json
    [
        {
            "id": 1,
            "task_id": 1,
            "user_id": 1,
            "status": "Incomplete"
        }
    ]
    ```

- **POST /assignments**

    Request:

    ```json
    {
        "task_id": 1,
        "user_id": 1,
        "status": "Incomplete"
    }
    ```

    Response:

    ```json
    {
        "id": 2,
        "task_id": 1,
        "user_id": 1,
        "status": "Incomplete"
    }
    ```

## Database Models

### User

- `id`: Integer, primary key
- `name`: String, not nullable
- `email`: String, unique, not nullable
- `password_hash`: String, not nullable

### Task

- `id`: Integer, primary key
- `title`: String, not nullable
- `description`: Text, not nullable
- `due_date`: Date, not nullable
- `user_id`: Integer, foreign key, not nullable

### Assignment

- `id`: Integer, primary key
- `task_id`: Integer, foreign key, not nullable
- `user_id`: Integer, foreign key, not nullable
- `status`: String, not nullable
