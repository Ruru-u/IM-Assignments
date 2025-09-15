print("Currency Converter Program")
print("Enter dollar amounts(* to exit)")

while True:
    user_input = input("\nEnter dollar ($) (* to exit): ").strip()
    
    if user_input == "*":
        print("Bye")
        break
    
    dollar_amounts = user_input.split('@')
    
    valid_amounts = []
    for amount in dollar_amounts:
        try:
            dollar_value = float(amount)
            if dollar_value >= 0:
                valid_amounts.append(dollar_value)
        except ValueError:
            continue
    
    if not valid_amounts:
        print("No valid dollar amounts entered. Please try again.")
        continue
    
    print("\nDollar ($)\tIndian Rupee (R)  \tBritish (Pound)   \tChina (Y)")
    
    for dollar in valid_amounts:
        rupee_rate = 83.50
        pound_rate = 0.79
        yuan_rate = 7.25
        
        rupees = dollar * rupee_rate
        pounds = dollar * pound_rate
        yuan = dollar * yuan_rate
        
        print(f"{dollar}\t\t{rupees}\t        \t{pounds}\t        \t{yuan}")