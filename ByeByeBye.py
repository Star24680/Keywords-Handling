Valid=False
while not Valid:
    try:
        X=int(input("Enter a number"))
        while X%2==0:
            print("Bye")
        Valid=True
    except ValueError:
        print("Invalid")
        