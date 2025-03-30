def calculate_discount(price,discount_percent):
   
    if discount_percent>=20:
        final_Price=price - (price*(discount_percentage/100))
        print(f"Final Price: {final_Price:.2f}")
    else:
        print(f"Price: {price:.2f}")
original_price=float(input("Enter the Original Price: "))
discount_percentage=float(input("Enter the discount percentage: "))

calculate_discount(original_price,discount_percentage)
      