try:
    number=int(input("Enter Value"))
    print("The number enetered is: ",number)
except ValueError as Ex:
    print("Excpetion",Ex)