print("--- Exercise 1 ---")



print("--- Exercise 2 ---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer[email]

print(customer)

print(customer.get("email", "Email not found"))

print("--- Exercise 3 ---")

print(customer.get("email", "no email on file"))

# try:
#     print(customer["email"])
# except KeyError as error:
#     print(f"KeyError Caught: {error}")

print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)

print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0,
                  "silver": .05,
                  "gold": .10,
                  "platinum": .15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate}")
print(f"Final Price: {final_price}")
