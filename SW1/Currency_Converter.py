def convert_usd(amount_usd):
    rate_inr = 88.09
    rate_gbp = 0.73346
    rate_cny = 7.11545
    inr = amount_usd * rate_inr
    gbp = amount_usd * rate_gbp
    cny = amount_usd * rate_cny
    return inr, gbp, cny

def main():
    while True:
        s = input("Enter dollar ($) (* to exit): ")
        if s.strip() == '*':
            print("Bye")
            break
        parts = s.split('@')
        dollars = []
        for p in parts:
            try:
                d = float(p)
                dollars.append(d)
            except ValueError:
                continue
        print("{:<15} {:<20} {:<20} {:<15}".format("Dollar ($)","Indian Rupee (INR)","British Pound (GBP)","Chinese Yuan (CNY)"))
        for d in dollars:
            inr, gbp, cny = convert_usd(d)
            print("{:<15} {:<20.2f} {:<20.2f} {:<15.2f}".format(d, inr, gbp, cny))

if __name__ == "__main__":
    main()
