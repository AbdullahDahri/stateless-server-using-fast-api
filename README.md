# Project 1: REST API Fundamentals

## Overview

This project is a REST API built using FastAPI in Python. The API demonstrates the fundamentals of web server development, HTTP methods, routing, and JSON data handling.

The server manages user information and supports CRUD (Create, Read, Update, Delete) operations through RESTful endpoints.

## Objectives

* Build a local web server using Python and FastAPI
* Implement API routing
* Handle HTTP requests and responses
* Return structured JSON data
* Understand REST API fundamentals

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

## Features

* Retrieve all users
* Retrieve a user by ID
* Create a new user
* Update a user completely using PUT
* Update specific user fields using PATCH
* Delete a user
* Input validation using Pydantic models

## API Endpoints

### GET /

Returns API status information.

### GET /users/

Returns all users.

### GET /users/{user_id}

Returns a specific user by ID.

### POST /users/

Creates a new user.

### PUT /users/{user_id}

Updates all user information.

### PATCH /user/{user_id}

Updates selected user fields.

### DELETE /users/{user_id}

Deletes a user.

## Example POST Request

```json
{
  "name": "Ahmed",
  "email": "ahmed@gmail.com",
  "age": 22
}
```

## Example Response

```json
{
  "response": "User added successfully",
  "user": {
    "id": 3,
    "name": "Ahmed",
    "email": "ahmed@gmail.com",
    "age": 22
  }
}
```

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn statelessserver:app --reload
```

### Access the API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

This opens FastAPI's automatically generated Swagger API documentation where all endpoints can be tested.

## Notes

* This project stores data in an in-memory Python list.
* Data is not persistent and will reset whenever the server restarts.
* The API follows REST principles and demonstrates the use of HTTP methods such as GET, POST, PUT, PATCH, and DELETE.

## Author

Abdullah Dahri
