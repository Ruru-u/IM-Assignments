def display_dict(mydict):
    print("Displaying Values")
    print("Key      Value")
    for k, v in mydict.items():
        print(f"{k:<8} {v}")

def main():
    mydict = {}
    items = ["underwear", "tank top", "jacket"]
    for i, item in enumerate(items):
        mydict[i] = item

    print("You have 3 items in the cart")

    while True:
        action = input("\nWhat would you like to do [C]hange items [R]emove [D]isplay  S[earch] ? ").strip().lower()
        if action == 'd':
            display_dict(mydict)
        elif action == 's':
            search_type = input("\nSearch by [K]ey or [V]alue? ").strip().lower()
            if search_type == 'k':
                key = input("Enter key to search: ")
                try:
                    key = int(key)
                    value = mydict.get(key)
                    if value is not None:
                        print(f"Found {value} item")
                    else:
                        print("Im sorry, not in the cart")
                except ValueError:
                    print("Invalid key. Please enter an integer.")
            elif search_type == 'v':
                value = input("Enter item to search: ")
                found = False
                for v in mydict.values():
                    if v == value:
                        print(f"Found {value} item")
                        found = True
                        break
                if not found:
                    print("Im sorry, not in the cart")
            else:
                print("Invalid option.")
        elif action == 'r':
            key = input("Enter key to search: ")
            try:
                key_int = int(key)
                value = mydict.get(key_int)
                if value is not None:
                    del mydict[key_int]
                    print(f"The key {key_int} with value {value} has been deleted")
                else:
                    print("Key not found")
            except ValueError:
                print("Key not found")
        elif action == 'c':
            key = input("Enter key to search: ")
            try:
                key_int = int(key)
                value = mydict.get(key_int)
                if value is not None:
                    print(f"Found {value} item")
                    new_value = input("Enter value: ")
                    mydict[key_int] = new_value
                else:
                    print("Im sorry, not in the cart")
            except ValueError:
                print("Im sorry, not in the cart")
        elif action == '*':
            print("Bye")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()