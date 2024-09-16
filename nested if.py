a=input("A:")
b=input("B:")
c=input("C:")

if(a>b):
    print("A")
    if(a>c):
        print("A is big")
    else:
        print("A is small")
else:
    if(a<b):
        print("B is big")
        if(a<c):
            print("C is big")
        else:
             print("C is small")
    else:
         print("B is small")

