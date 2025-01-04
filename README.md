# Alchemist-Remix
A powerful platform for remixing and managing your digital content. Alchemist Remix lets you craft compelling creatives, manage schedules, and transform your social media accounts into high-performance assets.


# **API Documentation**

This document provides details on all the API endpoints available in the application.

## **User Routes**

### **GET /api/users**
- **Description**: Retrieve all users.
- **Parameters**: None
- **Response**:
  ```json
  {
    "users": [
      {
        "id": 1,
        "username": "Demo",
        "email": "demo@aa.io"
      }
    ]
  }
  ```

---

### **GET /api/users/{id}**
- **Description**: Retrieve a user by their ID.
- **Parameters**:
  - `id` (integer, required): ID of the user.
- **Response**:
  ```json
  {
    "id": 1,
    "username": "Demo",
    "email": "demo@aa.io"
  }
  ```

---

## **Auth Routes**

### **POST /api/auth/login**
- **Description**: Log in a user.
- **Request Body**:
  ```json
  {
    "email": "demo@aa.io",
    "password": "password"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Successfully logged in.",
    "user": {
      "id": 1,
      "username": "Demo",
      "email": "demo@aa.io"
    }
  }
  ```

---

### **POST /api/auth/logout**
- **Description**: Log out the current user.
- **Response**:
  ```json
  {
    "message": "Successfully logged out."
  }
  ```

---

## **Content Source Routes**

### **GET /api/content_sources**
- **Description**: Retrieve all content sources.
- **Parameters**:
  - `page` (integer, optional): Page number (default: 1).
  - `each_page` (integer, optional): Items per page (default: 10).
- **Response**:
  ```json
  {
    "sources": [
      {
        "id": 1,
        "name": "The New York Times",
        "source_type": "Newspaper",
        "url": "https://www.nytimes.com/"
      }
    ],
    "total_pages": 1,
    "page": 1,
    "each_page": 10
  }
  ```

---

### **GET /api/content_sources/{id}**
- **Description**: Retrieve a specific content source by ID.
- **Parameters**:
  - `id` (integer, required): ID of the content source.
- **Response**:
  ```json
  {
    "id": 1,
    "name": "The New York Times",
    "source_type": "Newspaper",
    "url": "https://www.nytimes.com/"
  }
  ```

---

### **POST /api/content_sources**
- **Description**: Create a new content source.
- **Request Body**:
  ```json
  {
    "name": "Example Source",
    "source_type": "Blog",
    "url": "https://example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 4,
    "name": "Example Source",
    "source_type": "Blog",
    "url": "https://example.com"
  }
  ```

---

## **Alchemy Routes**

### **GET /api/alchemy/fusions**
- **Description**: Retrieve all alchemy fusions.
- **Response**:
  ```json
  {
    "fusions": [
      {
        "id": 1,
        "name": "Fusion Example",
        "source_type": "Alchemy Fusion"
      }
    ],
    "total": 1
  }
  ```

---

### **POST /api/alchemy/fusions**
- **Description**: Combine multiple content sources into a new fusion.
- **Request Body**:
  ```json
  {
    "source_ids": [1, 2]
  }
  ```
- **Response**:
  ```json
  {
    "id": 3,
    "name": "Source 1 + Source 2",
    "source_type": "Alchemy Fusion"
  }
  ```

---

## **Reflection Routes**

### **GET /api/reflections/{id}**
- **Description**: Retrieve reflections for a specific content source.
- **Parameters**:
  - `id` (integer, required): ID of the content source.
- **Response**:
  ```json
  {
    "reflections": [
      {
        "id": 1,
        "content": "This source is fantastic for beginners.",
        "user_id": 1
      }
    ]
  }
  ```

---

## **Comment Routes**

### **GET /api/comments/{id}**
- **Description**: Retrieve comments for a specific content source.
- **Parameters**:
  - `id` (integer, required): ID of the content source.
- **Response**:
  ```json
  {
    "comments": [
      {
        "id": 1,
        "content": "Great article!",
        "user_id": 2
      }
    ]
  }
  ```

