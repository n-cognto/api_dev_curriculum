"""
Basic Dictionary API Example
---------------------------
A simple API implementation using dictionaries to demonstrate basic CRUD operations.
This example shows how APIs work without the complexity of web frameworks.
"""

# Our "database" is just a dictionary in memory
books_db = {
    1: {"title": "The Python Way", "author": "John Smith", "year": 2025},
    2: {"title": "API First", "author": "Jane Doe", "year": 2024},
}

def get_book(book_id):
    """Simulate GET request to retrieve a book"""
    book_id = int(book_id)
    if book_id in books_db:
        return {"status": "success", "data": books_db[book_id]}
    return {"status": "error", "message": "Book not found"}

def create_book(book_data):
    """Simulate POST request to create a new book"""
    new_id = max(books_db.keys()) + 1
    books_db[new_id] = book_data
    return {"status": "success", "message": f"Book created with ID: {new_id}"}

def update_book(book_id, book_data):
    """Simulate PUT request to update a book"""
    book_id = int(book_id)
    if book_id in books_db:
        books_db[book_id].update(book_data)
        return {"status": "success", "message": "Book updated"}
    return {"status": "error", "message": "Book not found"}

def delete_book(book_id):
    """Simulate DELETE request to remove a book"""
    book_id = int(book_id)
    if book_id in books_db:
        del books_db[book_id]
        return {"status": "success", "message": "Book deleted"}
    return {"status": "error", "message": "Book not found"}

# Example usage
if __name__ == "__main__":
    # GET example
    print("\nGetting book 1:")
    print(get_book(1))

    # POST example
    new_book = {"title": "API Design Patterns", "author": "Alice Johnson", "year": 2023}
    print("\nCreating new book:")
    print(create_book(new_book))

    # PUT example
    print("\nUpdating book 2:")
    update_data = {"year": 2025}
    print(update_book(2, update_data))

    # DELETE example
    print("\nDeleting book 1:")
    print(delete_book(1))

    # Verify deletion
    print("\nTrying to get deleted book 1:")
    print(get_book(1))
