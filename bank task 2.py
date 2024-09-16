a=['keerthi','abi','sumai','swetha','priya']
b=[500,700,400,1000,300]
j=0
sender=input("enter the sender name:")
receiver=input("enter the receiver name:")
amount=int(input("enter the amount:"))

for i in a:
    if(i==sender):
     print("Sender bal amount",b[j]-amount)
     
    elif(i==receiver):
     print("Receiver add amount",b[j]+amount)
     
    j+=1
