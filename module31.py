# charge for the food from customer
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip (18% of the food charge)
tip_percent = 0.18
tip_amount = food_charge * tip_percent

# Calculate the sales tax (7% of the food charge)
tax_percent = 0.07
tax_amount = food_charge * tax_percent

# Calculate the total price (food charge + tip + tax)
total_price = food_charge + tip_amount + tax_amount

# Display each of these amounts and the total price
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip_amount:.2f}")
print(f"Sales Tax (7%): ${tax_amount:.2f}")
print(f"Total Price: ${total_price:.2f}")
