def calculate_order_total(items, customer_type):
    """
    Calculates the final order total applying various business rules and discounts.
    This function aims to reflect the current promotional strategies and customer segmentation.
    Without explicit intent, the 'why' behind certain rules can be lost over time,
    leading to maintenance difficulties and slower onboarding for new developers.
    """
    base_total = 0
    for item in items:
        base_total += item['price'] * item['quantity']

    final_total = base_total

    # Augmentcode Intent: Reward loyal 'premium' customers with a significant discount on larger orders.
    # Business Rule: Premium customers get 10% off orders over $150.
    # Rationale: Encourage repeat purchases and customer loyalty within the premium segment.
    if customer_type == 'premium' and final_total > 150:
        final_total *= 0.90
        print(f"  - Applied 10% premium customer discount (Intent: Loyalty reward).")
    # Augmentcode Intent: Encourage larger purchases from all customers.
    # Business Rule: General 5% discount for orders over $200.
    # Rationale: Boost average order value across all customer segments.
    elif final_total > 200:
        final_total *= 0.95
        print(f"  - Applied 5% general large order discount (Intent: AOV boost).")

    # Augmentcode Intent: Cover handling costs for small electronics orders,
    #                     as these often require special packaging/insurance.
    # Business Rule: A $10 small order fee is applied to electronics orders
    #                if the total is less than $50 after other discounts.
    # Rationale: Mitigate losses on low-margin, high-handling-cost items.
    if any(item['category'] == 'electronics' for item in items) and final_total < 50:
        final_total += 10
        print(f"  - Applied $10 small order fee for electronics (Intent: Cost recovery).")

    return final_total

# --- Demonstration of how explicit intent clarifies complex logic ---

items1 = [
    {'name': 'Laptop', 'category': 'electronics', 'price': 1200, 'quantity': 1},
    {'name': 'Mouse', 'category': 'electronics', 'price': 25, 'quantity': 1}
]
items2 = [
    {'name': 'Book', 'category': 'books', 'price': 20, 'quantity': 2},
    {'name': 'Pen', 'category': 'stationery', 'price': 5, 'quantity': 5}
]
items3 = [
    {'name': 'Headphones', 'category': 'electronics', 'price': 40, 'quantity': 1}
]
items4 = [
    {'name': 'USB Cable', 'category': 'electronics', 'price': 15, 'quantity': 1}
]


print("--- Demonstrating Explicit Intent in Business Logic ---")
print("This example shows how adding 'intent' comments helps explain *why* certain code decisions were made.\n")

print("\nOrder 1 (Premium Customer, Large Electronics Order):")
print(f"  Items: {items1}")
print(f"  Customer Type: premium")
total1 = calculate_order_total(items1, 'premium')
print(f"  Final Total: ${total1:.2f}\n")

print("\nOrder 2 (Regular Customer, Medium Books/Stationery Order):")
print(f"  Items: {items2}")
print(f"  Customer Type: regular")
total2 = calculate_order_total(items2, 'regular')
print(f"  Final Total: ${total2:.2f}\n")

print("\nOrder 3 (Regular Customer, Small Electronics Order - triggers fee):")
print(f"  Items: {items3}")
print(f"  Customer Type: regular")
total3 = calculate_order_total(items3, 'regular')
print(f"  Final Total: ${total3:.2f}\n")

print("\nOrder 4 (Regular Customer, Very Small Electronics Order - also triggers fee):")
print(f"  Items: {items4}")
print(f"  Customer Type: regular")
total4 = calculate_order_total(items4, 'regular')
print(f"  Final Total: ${total4:.2f}\n")
