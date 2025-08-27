# Exercise 2: Restaurant Order System API

## Objective

Build a more complex API system using the restaurant metaphor to deepen your understanding of API concepts and HTTP methods.

## Background

You'll create a restaurant order management system that demonstrates how real-world processes map to API operations.

## Requirements

Create a Python script that implements a restaurant system with:

1. Menu management
2. Order processing
3. Kitchen operations
4. Status tracking

## Starting Template

```python
class MenuItem:
    def __init__(self, name, price, preparation_time):
        self.name = name
        self.price = price
        self.preparation_time = preparation_time

class Order:
    def __init__(self, order_id, items, table_number):
        self.order_id = order_id
        self.items = items
        self.table_number = table_number
        self.status = "pending"
        self.timestamp = None

class Restaurant:
    def __init__(self):
        self.menu = {}
        self.orders = {}
        self.order_counter = 1

    def add_menu_item(self, name, price, preparation_time):
        """
        Add a new item to the menu
        Similar to: POST /api/menu
        """
        # Your code here
        pass

    def get_menu(self):
        """
        Return the current menu
        Similar to: GET /api/menu
        """
        # Your code here
        pass

    def place_order(self, items, table_number):
        """
        Create a new order
        Similar to: POST /api/orders
        """
        # Your code here
        pass

    def get_order_status(self, order_id):
        """
        Check status of an order
        Similar to: GET /api/orders/{order_id}
        """
        # Your code here
        pass

    def update_order_status(self, order_id, new_status):
        """
        Update the status of an order
        Similar to: PUT /api/orders/{order_id}
        """
        # Your code here
        pass

    def cancel_order(self, order_id):
        """
        Cancel an order
        Similar to: DELETE /api/orders/{order_id}
        """
        # Your code here
        pass

# Test your implementation
if __name__ == "__main__":
    # Add test cases here
    pass
```

## Tasks

1. Implement Menu Management:
   - Add new menu items
   - Get the current menu
   - Update menu item details
   - Remove menu items

2. Implement Order Processing:
   - Create new orders
   - Validate order items against menu
   - Calculate total price
   - Generate unique order ID

3. Implement Status Management:
   - Track order status (pending, preparing, ready, served)
   - Update order status
   - Get current status of any order

4. Implement Order Operations:
   - Cancel orders
   - Modify existing orders
   - Handle invalid orders

## Test Cases

Add these test cases to your script:

```python
if __name__ == "__main__":
    # Create restaurant instance
    restaurant = Restaurant()

    # Add menu items
    print("\nAdding menu items:")
    restaurant.add_menu_item("Pizza", 12.99, "20 min")
    restaurant.add_menu_item("Burger", 8.99, "15 min")
    restaurant.add_menu_item("Salad", 6.99, "10 min")

    # Display menu
    print("\nCurrent Menu:")
    print(restaurant.get_menu())

    # Place orders
    print("\nPlacing orders:")
    order1 = restaurant.place_order(["Pizza", "Salad"], 5)
    print(f"Order 1 status: {restaurant.get_order_status(order1)}")

    order2 = restaurant.place_order(["Burger"], 3)
    print(f"Order 2 status: {restaurant.get_order_status(order2)}")

    # Update order status
    print("\nUpdating order status:")
    restaurant.update_order_status(order1, "preparing")
    print(f"Order 1 updated status: {restaurant.get_order_status(order1)}")

    # Cancel order
    print("\nCancelling order:")
    restaurant.cancel_order(order2)
    print(f"Trying to get cancelled order: {restaurant.get_order_status(order2)}")
```

## Expected Output

Your implementation should produce output similar to this:

```
Adding menu items:
Pizza added to menu
Burger added to menu
Salad added to menu

Current Menu:
Pizza: $12.99 (20 min)
Burger: $8.99 (15 min)
Salad: $6.99 (10 min)

Placing orders:
Order #1 placed successfully
Order 1 status: pending
Order #2 placed successfully
Order 2 status: pending

Updating order status:
Order 1 updated status: preparing

Cancelling order:
Order #2 cancelled successfully
Trying to get cancelled order: Order not found
```

## Bonus Challenges

1. Add Time Management:
   - Track order preparation time
   - Estimate delivery time
   - Handle kitchen capacity

2. Add Table Management:
   - Track table status
   - Handle multiple orders per table
   - Calculate table bills

3. Add Special Requests:
   - Handle dietary restrictions
   - Customize menu items
   - Add special instructions

4. Add Error Handling:
   - Handle invalid menu items
   - Handle unavailable items
   - Handle invalid table numbers

## Submission

Save your solution as `restaurant_api.py` and ensure all test cases pass successfully.

## Learning Objectives

This exercise helps you understand:
1. How real-world processes map to API operations
2. CRUD operations in a practical context
3. State management in APIs
4. Error handling and validation
5. Complex data relationships
