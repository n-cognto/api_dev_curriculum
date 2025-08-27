# Exercise 1: Building Your First API

## Objective
Create a simple contact list API using Python dictionaries to understand basic CRUD operations (Create, Read, Update, Delete).

## Requirements

Create a Python script that implements a contact list with the following features:

1. Store contacts with:
   - Name
   - Email
   - Phone number
   - Address (optional)

2. Implement these operations:
   - Add a new contact
   - Get all contacts
   - Get a specific contact by name
   - Update a contact's information
   - Delete a contact

## Starting Template

```python
# Your contact database (dictionary)
contacts = {}

def add_contact(name, email, phone, address=None):
    """
    Add a new contact to the database
    Return: Success/failure message
    """
    # Your code here
    pass

def get_all_contacts():
    """
    Return all contacts in the database
    """
    # Your code here
    pass

def get_contact(name):
    """
    Get a specific contact by name
    Return: Contact information or error message
    """
    # Your code here
    pass

def update_contact(name, email=None, phone=None, address=None):
    """
    Update an existing contact's information
    Return: Success/failure message
    """
    # Your code here
    pass

def delete_contact(name):
    """
    Delete a contact from the database
    Return: Success/failure message
    """
    # Your code here
    pass

# Test your implementation
if __name__ == "__main__":
    # Add some test cases here
    pass
```

## Tasks

1. Implement the `add_contact` function:
   - Check if contact already exists
   - Add contact if it doesn't exist
   - Return appropriate success/error message

2. Implement the `get_all_contacts` function:
   - Return all contacts in a readable format
   - Handle empty contact list case

3. Implement the `get_contact` function:
   - Find contact by exact name match
   - Return contact info if found
   - Return error message if not found

4. Implement the `update_contact` function:
   - Check if contact exists
   - Update only provided fields
   - Keep existing data for non-provided fields
   - Return success/error message

5. Implement the `delete_contact` function:
   - Check if contact exists
   - Remove contact if found
   - Return appropriate message

## Testing Your Implementation

Add these test cases to your script:

```python
if __name__ == "__main__":
    # Test adding contacts
    print("\nAdding contacts:")
    print(add_contact("John Doe", "john@example.com", "123-456-7890"))
    print(add_contact("Jane Smith", "jane@example.com", "098-765-4321", "123 Main St"))
    
    # Test getting all contacts
    print("\nAll contacts:")
    print(get_all_contacts())
    
    # Test getting specific contact
    print("\nGetting John's contact:")
    print(get_contact("John Doe"))
    
    # Test updating contact
    print("\nUpdating John's contact:")
    print(update_contact("John Doe", phone="111-222-3333"))
    
    # Test deleting contact
    print("\nDeleting Jane's contact:")
    print(delete_contact("Jane Smith"))
    
    # Verify deletion
    print("\nAll contacts after deletion:")
    print(get_all_contacts())
```

## Expected Output Format

Your implementation should produce output similar to this:

```
Adding contacts:
Contact added successfully

All contacts:
Name: John Doe
Email: john@example.com
Phone: 123-456-7890

Name: Jane Smith
Email: jane@example.com
Phone: 098-765-4321
Address: 123 Main St

Getting John's contact:
Name: John Doe
Email: john@example.com
Phone: 123-456-7890

Updating John's contact:
Contact updated successfully

Deleting Jane's contact:
Contact deleted successfully

All contacts after deletion:
Name: John Doe
Email: john@example.com
Phone: 111-222-3333
```

## Bonus Challenges

1. Add input validation:
   - Validate email format
   - Validate phone number format
   - Ensure required fields are not empty

2. Add search functionality:
   - Search contacts by partial name match
   - Search by email domain
   - Search by phone number pattern

3. Add contact categories:
   - Add categories (work, family, friends)
   - Filter contacts by category
   - Allow multiple categories per contact

## Submission

Save your solution as `contact_list_api.py` and make sure all test cases pass successfully.
