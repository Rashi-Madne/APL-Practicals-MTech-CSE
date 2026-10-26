n=int (input("Enter number of items bought : "))
items=[]
subtotal=0

for i in range(n):
    print(f"enter details of the item {i+1}")

    item_name=input("Enter item name : ")
    quantity=float(input(f"Enter quantity of item {i+1} :"))
    price=float(input("Enter price per unit :"))
    total=quantity*price
    subtotal=subtotal+total

    items.append([item_name,quantity,price,total])

if subtotal>1000:
    discount_percent=10
elif subtotal>500:
    discount_percent=5
else:
    discount_percent=0

discount=subtotal*discount_percent/100
discounted_price=subtotal-discount
gst=discounted_price*12/100
total_bill=discounted_price+gst

print("==============================")
print("        SHOPPING BILL         ")
print("==============================")
print(f"{"Item":<12}{"Qty":<6}{"Price":<8}{"Total":<8}")
for item in items:
    print(f"{item[0]:<12}{item[1]:<6}{item[2]:<8.2f}{item[3]:<8.2f}")
print("-------------------------------")
print(f"Subtotal:                    {subtotal:.2f}")
print(f"Discount {discount_percent}:                 -Rs.{discount:.2f}  ")  
print(f"GST(12%)                     +{gst:.2f}")  
print("--------------------------------")
print(f"Total Amount To Pay :       Rs.{total_bill:.2f}")
print("=================================")
print("     Thank you! Visit again!     ")
print("=================================")