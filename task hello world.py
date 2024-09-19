string=input("Enter The String")
length=len(string)
for i in range(string):
    for j in range(i+1):
        print(string[j],end=" ")
    print()
