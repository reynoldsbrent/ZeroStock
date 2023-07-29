initial_stock = int(input("Please enter the an initial stock level: "))
plan = int(input("Please enter the number of months to plan: "))

produce = []
for i in range(0, plan):
    sales_quantity = int(input("Please enter the planned sales quantity: "))
    if sales_quantity <= initial_stock:
        to_produce = 0
    else:
        to_produce = sales_quantity - initial_stock
    produce.append(to_produce)
    initial_stock += to_produce
    initial_stock -= sales_quantity

print("The resulting production quantities are:")
for i in produce:
    print(f"Production quantity month {produce.index(i) + 1} - {i}")
