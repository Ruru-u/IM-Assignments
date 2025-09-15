while True:
    x = input("Welcome! Press any to continue or / to exit: ")
    if x == '/':
        print("Exit")
        break

    print("Enter row: ")
    num = int(input())
    
    print("Enter col: ")
    num2 = int(input())

    print("Search: ")
    num3 = int(input())

    for i in range(1, num+1):
        for j in range(1, num2+1):
            result = i * j
            if num3 == result:
                print(f"\033[93m\033[1m{result:4}\033[0m", end=" ")   
            else:
                print(f"{result:4}", end=" ")    
        print()