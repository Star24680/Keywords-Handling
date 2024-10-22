try:
    num1,num2=eval(input("Enter 2 numbers,seperated by a comma "))
    Result=num1/num2
    print("Result is: ",Result)
except ZeroDivisionError:
    print("DIVISION BY 0 IS ERROR")
except SyntaxError:
    print("Comma is missssiiinnng, Enter sperated by commmmmmmmmaaaa")
except:
    print("Wrooooong input")
else:
    print("NO EXCEPTION")
finally:
    print("This will execute no matter what")