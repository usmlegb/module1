class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price:.2f}")

if __name__ == "__main__":
    # Prompt the user for item 1
    print("Item 1")
    item_name1 = input("Enter the name of the item: ")
    item_price1 = float(input("Enter the price of the item: "))
    item_quantity1 = int(input("Enter the quantity: "))

    # Prompt the user for item 2
    print("\nItem 2")
    item_name2 = input("Enter the name of the item: ")
    item_price2 = float(input("Enter the price of the item: "))
    item_quantity2 = int(input("Enter the quantity: "))

    # Create two objects of the ItemToPurchase class
    item1 = ItemToPurchase(item_name1, item_price1, item_quantity1)
    item2 = ItemToPurchase(item_name2, item_price2, item_quantity2)

    # Calculate and print the total cost
    total_cost = (item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)
    print("\nTotal cost: ${:.2f}".format(total_cost))
