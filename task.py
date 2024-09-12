
a=['keerthi','abi','sumai','swetha','priya']
b=[500,700,400,1000,300]

sender=input("enter the sender name:")
receiver=input("enter the receiver name:")
amount=int(input("enter the amount:"))

for i in a:
    if(i==sender):
        print("sender is available")
        s=(a.index(i))
        print("bal amount",b[s]-amount)
    elif(i==receiver):
        print("receiver is available")
        p=(a.index(i))
        print("add amount",b[p]+amount)
