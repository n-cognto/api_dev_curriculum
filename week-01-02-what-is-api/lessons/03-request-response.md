# Understanding HTTP Requests and Responses

## Introduction

Every API interaction consists of two main parts:
1. The Request (what you ask for)
2. The Response (what you get back)

## HTTP Requests

### Anatomy of a Request

A complete HTTP request contains:

1. **HTTP Method**
   - GET, POST, PUT, DELETE, etc.
   - Tells the server what action to perform

2. **URL (Endpoint)**
   - The address where the resource is located
   - Example: `https://api.example.com/books/123`

3. **Headers**
   - Metadata about the request
   - Common headers:
     - Content-Type: Type of data being sent
     - Authorization: Authentication credentials
     - Accept: Type of response expected

4. **Body** (optional)
   - Data sent with the request
   - Common in POST/PUT requests
   - Usually in JSON format

### Example Request

```http
POST /api/books HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer abc123token

{
    "title": "API Design Patterns",
    "author": "John Smith",
    "year": 2025
}
```

## HTTP Responses

### Anatomy of a Response

A complete HTTP response contains:

1. **Status Code**
   - 3-digit number indicating request result
   - Categories:
     - 2xx: Success
     - 3xx: Redirection
     - 4xx: Client Error
     - 5xx: Server Error

2. **Headers**
   - Metadata about the response
   - Common headers:
     - Content-Type: Type of data being returned
     - Content-Length: Size of response
     - Cache-Control: Caching instructions

3. **Body**
   - The actual data being returned
   - Format specified in Content-Type header
   - Common formats: JSON, XML, HTML

### Example Response

```http
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 157

{
    "id": 456,
    "title": "API Design Patterns",
    "author": "John Smith",
    "year": 2025,
    "created_at": "2025-08-27T12:00:00Z"
}
```

## Common Response Status Codes

### Success (2xx)

- **200 OK**
  - Request succeeded
  - Used for successful GET requests

- **201 Created**
  - Resource created successfully
  - Used for successful POST requests

- **204 No Content**
  - Request succeeded, no content to return
  - Common for DELETE operations

### Client Errors (4xx)

- **400 Bad Request**
  - Invalid request syntax
  - Missing required fields

- **401 Unauthorized**
  - Authentication required
  - Invalid credentials

- **403 Forbidden**
  - Authentication succeeded
  - But user lacks permissions

- **404 Not Found**
  - Requested resource doesn't exist

### Server Errors (5xx)

- **500 Internal Server Error**
  - Something went wrong on the server

- **503 Service Unavailable**
  - Server temporarily unavailable
  - Often during maintenance

## Request-Response Flow Example

### Scenario: Creating a New Book

1. **Client Sends Request:**
```http
POST /api/books HTTP/1.1
Content-Type: application/json

{
    "title": "Python API Design",
    "author": "Jane Doe"
}
```

2. **Server Processes Request:**
   - Validates data
   - Creates new record
   - Generates response

3. **Server Sends Response:**
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 789,
    "title": "Python API Design",
    "author": "Jane Doe",
    "created_at": "2025-08-27T14:30:00Z"
}
```

## Best Practices

1. **Always Check Status Codes**
   - Don't assume request succeeded
   - Handle errors appropriately

2. **Set Proper Content-Type**
   - Tell server what you're sending
   - Tell client what to expect

3. **Handle Errors Gracefully**
   - Provide meaningful error messages
   - Include error details when appropriate

4. **Validate Request Data**
   - Check required fields
   - Validate data types
   - Sanitize input

5. **Use Standard Status Codes**
   - Don't invent new codes
   - Use most specific code available

## Practical Exercise

Try using the requests library in Python to:
1. Make GET requests to public APIs
2. Examine response status codes
3. Parse JSON responses
4. Handle different status codes

## Additional Resources

- [MDN HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [HTTP Status Codes](https://httpstatuses.com/)
- [Python Requests Library](https://requests.readthedocs.io/)
