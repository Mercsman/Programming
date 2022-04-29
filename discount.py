# discount tracker
from datetime import datetime
# subtotal

subtotal = 0
price = 1

while price != 0:
    price = float(input("Enter the Price: "))
    if price != 0:
        quantity = float(input("How many articles are you buying: "))
        subtotal += (price * quantity)
    
day = datetime.now()
today = day.weekday()
discount = 0

if today == 1 or 2:
    if subtotal >= 50:
        discount = subtotal * 0.1
taxes = subtotal * 0.06
total = subtotal + taxes - discount

if discount > 0:
    print(f"Your discount is ${discount:.2f}")
    
if today == 1 or today == 2:
    if subtotal < 50:
            print(f"You need to spend ${50-subtotal} to have a discount")
            
print(f"Taxes: ${taxes:.2f}")
print(f"Total: ${total:.2f}")