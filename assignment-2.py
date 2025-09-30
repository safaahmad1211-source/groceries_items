groceries = {"apple":2, "banana":1, "milk":3, "bread":2}
shopping_cart = []
while True:
    item = input("Input what you want to buy: ")
    if item == "done":
        break
    if item in groceries:
        shopping_cart.append(item)
    else:
        print("Sorry, we dont have that item.")

print(f"You bought:{shopping_cart}")
total = 0
for item in shopping_cart: 
    total=total+groceries[item]
print(f"total= ${total}")
if total>10:
    print("You spent alot!")

else:
    print("You spent a little")

       
