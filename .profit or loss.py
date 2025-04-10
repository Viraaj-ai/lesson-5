cost_price=float(input("Enter your products cost:"))
selling_price=float(input("Enter your products selling price"))
if selling_price>cost_price:
    amount=selling_price-cost_price
    print("your proft gained is",amount)
else:
    print("you had a loss")