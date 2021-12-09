# Created by Cyclops!
def menu ():
    print ("\n1. Decimal")
    print ("2. Binary")
    print ("3. Octal")
    print ("4. Hexadecimal")
    print ("5. Exit")
    pick = int(input("Please enter an option: "))
    return pick

def toBinary (b):
    return bin(b)

def toDecimal (d):
    return int(d)

def toOctal (o):
    return oct(o)

def toHexadecimal (h):
    return hex(h)


def main():
    choice=menu()
    while choice !=5:
        if choice == 1:
            
            d = eval(input("What is your Decimal Value?: "))
            print(int(toDecimal (d)))

        elif choice == 2:
            
            b = eval(input("What is your Binary Value?: "))
            print(str(toBinary (b)))

        elif choice == 3:
            
            o = eval(input("What is your Octal Value?: "))
            print(str(toOctal (o)))

        elif choice == 4:
            
            h = eval(input("What is your Hexadecimal Value?: "))
            print(str(toHexadecimal (h)))

        else:
            print ("Whoops!!! Invalid Entry")

main()
