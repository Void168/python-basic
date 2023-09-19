class JustNotCoolError(Exception):
    pass


x = 2

try:
    raise JustNotCoolError("This just isn't cool, man.")
except NameError:
    print("NameError meas something is probably undefinded")
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(error)
else:
    print("no errors!")
finally:
    print("I'm going to print with or without an error.")
