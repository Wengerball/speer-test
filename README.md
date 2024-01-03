# speer-test

Building a secure and scalable RESTful API that allows users to create, read, update, and delete notes

## Framework and database

- This API is built using Django Rest Framework (DRF), a powerful and flexible toolkit for building Web APIs in Django.

- PostgreSQL is used as the database for storing notes and user data.

## Authentication and Rate Limiting

- Authentication is implemented using JSON Web Tokens (JWT) for secure user authentication and authorization.

- Simple rate limiting and request throttling mechanisms are in place to handle high traffic and prevent abuse of the API.

## Search Functionality

- Text indexing is implemented for high-performance note searching based on keywords.

## Unit and Integration Testing

- The API includes comprehensive unit and integration tests to ensure correctness and reliability of endpoints.

## Getting Started

To run this project locally, follow these steps:

1. Setup Environment variable:

    ```bash
    virtualenv django-env
    source /django-env/bin/activate

2. Clone the repository and install dependencies:

    ```bash
    git clone <repository_url>
    cd assessment
    pip install -r requirements.txt

3. Postgres configurations:

    ```bash
    # kindly update these configurations according to your feasibility
    /assessment/settings.py 
   
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'speer',
        'USER': 'shashwat',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }

4. Apply Migrations and Runserver:

    ```bash
    python manage.py makemigrations
    python manage.py migrate

    python manage.py runserver 8008

5. Running unit and integration tests:

    ```bash
    python manage.py test notes.tests

## APIs and cURL Requests

### Authentication Endpoints

1. Create a new user account

    ```bash
    curl -X POST http:/localhost:8008/api/auth/signup \
     -H "Content-Type: application/json" \
     -d '{"username": "newuser", "password": "strongpassword123"}'

2. Log in to an existing user account and receive an access token

    ```bash
    curl -X POST http:/localhost:8008/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"username": "newuser", "password": "strongpassword123"}'

### Note Endpoints

1. Get a list of all notes for the authenticated user

    ```bash
    curl -X GET http://localhost:8008/api/notes/ \
    -H "Authorization: Bearer Access-Token"

2. Get a note by ID for the authenticated user

    ```bash
    curl -X GET http://localhost:8008/api/notes/:id \
    -H "Authorization: Bearer Access-Token"

3. Create a new note for the authenticated user

    ```bash
    curl -X POST http://localhost:8008/api/notes/ \
    -H "Authorization: Bearer Access-Token" \
    -H "Content-Type: application/json" \
    -d '{"title": "New Note", "content": "This is the content of the new note."}'

4. Update an existing note by ID for the authenticated user

    ```bash
    curl -X PUT http://localhost:8008/api/notes/:id \
    -H "Authorization: Bearer Access-Token" \
    -H "Content-Type: application/json" \
    -d '{"title": "Updated Note", "content": "This is the updated content."}'

5. Delete a note by ID for the authenticated user

    ```bash
    curl -X DELETE http://localhost:8008/api/notes/:id \
    -H "Authorization: Bearer Access-Token"

6. Share a note with another user for the authenticated user

    ```bash
    curl -X POST http://localhost:8008/api/notes/:id/share/ \
    -H "Authorization: Bearer Access-Token" \
    -H "Content-Type: application/json" \
    -d '{"shared_with": "shash"}'

7. Search for notes based on keywords for the authenticated user

    ```bash
    curl -X GET http://localhost:8008/api/search/?q=:query \
    -H "Authorization: Bearer Access-Token"
