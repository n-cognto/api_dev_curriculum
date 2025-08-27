"""
Restaurant API Metaphor
----------------------
This example explains APIs using a restaurant analogy:
- Customer = Client
- Waiter = API
- Kitchen = Server
- Menu = API Documentation
- Order = Request
- Served Food = Response
"""

class Kitchen:
    def __init__(self):
        self.menu = {
            "pizza": {"price": 12.99, "prep_time": "15 min"},
            "burger": {"price": 8.99, "prep_time": "10 min"},
            "salad": {"price": 7.99, "prep_time": "5 min"}
        }
        self.orders = {}
        self.order_counter = 1

    def prepare_order(self, items):
        """Kitchen prepares the ordered items"""
        available_items = []
        unavailable_items = []
        total = 0

        for item in items:
            if item in self.menu:
                available_items.append(item)
                total += self.menu[item]["price"]
            else:
                unavailable_items.append(item)

        return {
            "available": available_items,
            "unavailable": unavailable_items,
            "total": total
        }

class Waiter:
    def __init__(self, kitchen):
        self.kitchen = kitchen

    def take_order(self, items):
        """
        POST request - Taking a new order
        Similar to creating a new resource
        """
        order_result = self.kitchen.prepare_order(items)
        
        if not order_result["available"]:
            return {
                "status": "error",
                "message": "None of the ordered items are available",
                "unavailable_items": order_result["unavailable"]
            }

        order_id = self.kitchen.order_counter
        self.kitchen.orders[order_id] = order_result
        self.kitchen.order_counter += 1

        return {
            "status": "success",
            "order_id": order_id,
            "available_items": order_result["available"],
            "unavailable_items": order_result["unavailable"],
            "total": order_result["total"]
        }

    def check_menu(self):
        """
        GET request - Retrieving the menu
        Similar to reading a resource
        """
        return {
            "status": "success",
            "menu": self.kitchen.menu
        }

    def check_order_status(self, order_id):
        """
        GET request - Checking specific order
        Similar to reading a specific resource
        """
        if order_id in self.kitchen.orders:
            return {
                "status": "success",
                "order": self.kitchen.orders[order_id]
            }
        return {
            "status": "error",
            "message": "Order not found"
        }

# Example usage
if __name__ == "__main__":
    # Initialize our restaurant
    kitchen = Kitchen()
    waiter = Waiter(kitchen)

    # Customer checks the menu (GET request)
    print("\nCustomer checks menu:")
    print(waiter.check_menu())

    # Customer places an order (POST request)
    print("\nCustomer orders food:")
    order = waiter.take_order(["pizza", "burger", "sushi"])
    print(order)

    # Customer checks order status (GET request)
    print("\nCustomer checks order status:")
    print(waiter.check_order_status(1))

    # Customer checks non-existent order (GET request with error)
    print("\nCustomer checks invalid order:")
    print(waiter.check_order_status(999))
