# HTTP Methods in APIs

## Introduction to HTTP Methods

HTTP methods are standardized ways to interact with resources through an API. They define the type of action you want to perform on a resource.

## The Main HTTP Methods

### GET

- Used to **retrieve** information
- Does not modify any data
- Safe and idempotent (multiple identical requests should have the same result)
- Example: `GET /api/books/1` retrieves book with ID 1

### POST

- Used to **create** new resources
- Modifies data on the server
- Not idempotent (multiple identical requests create multiple resources)
- Example: `POST /api/books` creates a new book

### PUT

- Used to **update** existing resources
- Replaces the entire resource
- Idempotent (multiple identical requests have same result)
- Example: `PUT /api/books/1` updates book with ID 1

### PATCH

- Used to make **partial updates** to resources
- Only modifies specified fields
- Example: `PATCH /api/books/1` updates specific fields of book 1

### DELETE

- Used to **remove** resources
- Idempotent (deleting same resource multiple times has same effect)
- Example: `DELETE /api/books/1` removes book with ID 1

## Understanding Idempotency

An operation is idempotent if making the same request multiple times has the same effect as making it once:

- ✅ GET: Reading same data multiple times
- ❌ POST: Creating new resource each time
- ✅ PUT: Updating with same data
- ✅ DELETE: Removing same resource

## Status Codes

Common HTTP status codes you'll encounter:

### Success Codes (2xx)

- 200: OK (Success)
- 201: Created (Successfully created resource)
- 204: No Content (Success but no content to return)

### Client Error Codes (4xx)

- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 405: Method Not Allowed

### Server Error Codes (5xx)

- 500: Internal Server Error
- 503: Service Unavailable

## Practical Examples

### Book API Example

```python
# GET /api/books/1
def get_book(book_id):
    return {"id": 1, "title": "API Basics"}

# POST /api/books
def create_book(data):
    return {"status": "created", "id": 2}

# PUT /api/books/1
def update_book(book_id, data):
    return {"status": "updated"}

# DELETE /api/books/1
def delete_book(book_id):
    return {"status": "deleted"}
```

## Best Practices

1. Use appropriate HTTP methods for operations
2. Return correct status codes
3. Make endpoints noun-based (`/books` not `/getBooks`)
4. Keep endpoints consistent
5. Use plural nouns for collections

## Exercise

Try implementing these methods in the `basic-dictionary-api.py` example!
