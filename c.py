def name(first, last):
    first=first.upper()
    last=last.upper()
    t = first+" "+last
    return t

print("Welcome to "+name("Sonu","c")+" World....")

while True:
    a=int(input("Enter the first number : "))
    b=int(input("enter the second number :"))
    def sum(a,b):
        c = a+b
        return c
    def sub(a,b):
        c = a-b
        return c
    def mul(a,b):
        c = a*b
        return c
    def div(a,b):
        c = a/b
        return c

    c = input("Enter the opertion : ").strip()

    if c == "+":
        print(sum(a,b))
    elif c == "-":
        print(sub(a,b))
    elif c == "*" :
        print(mul(a,b))
    elif c == "/":
        print(div(a,b))
    else:
        print("Not valid... ")

    ip = input("Do u want to continue : (yes/ no) : ").lower().strip()
    if ip == "no":
        break
    elif ip == "yes":
        continue
    else: break

