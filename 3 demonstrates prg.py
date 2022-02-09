try:
    print("try block")
    x = int(input('Enter a Number:'))
    y = int(input('Enter Another Number:'))
    z = x/y
except ZeroDivisionError:
        print("except ZeroDivisionError block")
        print("Division by 0 not accepted")
else:
    print("else block")
    print("Division =",z)
finally:
    print("Finally block")
    x=0
    y=0
    print("Out of try,except,else and finally blocks.")
