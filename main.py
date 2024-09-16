
print("  ____    _    _     ____ _   _ _        _  _____ ___  ____  ")
print(" / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ ")
print("| |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |")
print("| |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ <")
print(" \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_\ ")

print(" ")

while True:
    no1 = float(input("Input number #1: "))
    no2 = float(input("Input number #2: "))



    operation= str(input("Enter operation performed:"))

    if not operation == "/":
        no1 = int(no1)
        no2 = int(no2)


    if operation == "+":
        output = no1 + no2
        print(no1,"+", no2, "=" ,round(output) )
    elif operation == "-":
        output = no1 - no2
        print(no1,"-", no2, "=" ,round(output) )
    elif operation == "*":
        output = no1 * no2
        print(no1,"*", no2, "=" ,round(output) )
    elif operation == "/" and no2 == 0:
        print("Error 02:  Divide by Zero error. Please try again.")
    elif operation == "/":
        output = no1 / no2
        print(no1,"/", no2, "=" ,round(output,2) )
    elif operation == "^" or operation == "**":
        output = no1 ** no2
        print(no1,"^", no2, "=" ,round(output) )
    else:
        print("Error 01: Please input an operation (+, -, *, /, ^, **)")
        
        
