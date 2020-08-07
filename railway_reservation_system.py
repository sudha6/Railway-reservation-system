def reserve(n,m):
    if n==1 and m==1:
         print("\t\t\tJOURNEY RESERVATION DETAILS")
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         x=int(input("TRAIN NUMBER:\t"))
         y=str(input("TRAIN NAME:\t"))
         z=input("DATE OF JOURNEY:\t")
         a=str(input("CLASS:\t"))
         b=int(input("NUMBER OF BERTHS:\t"))
         c=str(input("STATION FROM ......TO........\t"))
         d=str(input("BOARDING AT:\t"))
         return x,y,z,a,b,c,d
    elif n==1 and m==2:
         print("\t\t\tJOURNEY RESERVATION DETAILS")
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         x=int(input("TRAIN NUMBER:\t"))
         y=str(input("TRAIN NAME:\t"))
         z=input("DATE OF JOURNEY:\t")
         a=str(input("CLASS:\t"))
         b=int(input("NUMBER OF BERTHS:\t"))
         c=str(input("STATION FROM ......TO........:\t"))
         d=str(input("BOARDING AT:\t"))
         return x,y,z,a,b,c,d
    else:
        print("\t\t\tCANCELLATION FORM")
        print("~~~~~~~~~~~~~~~~~")
        x=int(input("TRAIN NUMBER:\t"))
        y=str(input("TRAIN NAME:\t"))
        z=input("DATE OF JOURNEY:\t")
        a=str(input("CLASS:\t"))
        b=int(input("NUMBER OF BERTHS:\t"))
        c=str(input("STATION FROM ......TO........:\t"))
        d=str(input("BOARDING AT:\t"))
        return x,y,z,a,b,c,d
def passenger_input(b):
         name=list()
         age=list()
         gen=list()
         choice=list()
         for i in range (b): 
          name.append(str(input("NAME IN BLOCK LETTERS:")))
          age.append(int(input("AGE:")))
          gen.append(str(input("GENDER:")))
          choice.append(str(input("CHOICE WITH ANY..........LOWER BERTH/UPPER BERTH WITH REASON:")))
         return name,age,gen,choice
def return_details(n):
    if n!=2:
         print("\t\t\tRETURN JOURNEY DETAILS ")
         x1=int(input("TRAIN NUMBER:\t"))
         y1=str(input("TRAIN NAME:\t"))
         z1=input("DATE OF JOURNEY:\t")
         a1=str(input("CLASS:\t"))
         b1=str(input("STATION FROM ......TO........:\t"))
         c1=str(input("BOARDING AT:\t"))
         name1=str(input("NAME OF THE APPLICANT:\t"))
         add=str(input("ADDRESS: "))
         mobile=input("MOBILE NUMBER: ")
         return x1,y1,z1,a1,b1,c1,name1,add,mobile
    else:
         print("\t\t\tRETURN JOURNEY DETAILS ")
         x1=int(input("TRAIN NUMBER:\t"))
         y1=str(input("TRAIN NAME:\t"))
         z1=input("DATE OF JOURNEY:\t")
         a1=str(input("CLASS:\t"))
         b1=str(input("STATION FROM ......TO........\t"))
         c1=str(input("BOARDING AT:\t"))
         name1=str(input("NAME OF THE APPLICANT:"))
         add=str(input("ADDRESS: "))
         mobile=input("MOBILE NUMBER: ")
         return x1,y1,z1,a1,b1,c1,name1,add,mobile
def ticket_price(n,m,o):
    if (n==1 and m==1):
        return(350*o)   
    elif (n==1 and m==2):
        return(600*o)
    else:
        return("YOUR TICKET HAS BEEN CANCELLED AND THE AMOUNT IS PAID BACK")
def print_ticket(x,y,z,a,b,c,d,name,age,gen,x1,y1,z1,a1,b1,c1,name1,add,mobile,price):
    print("RAILWAY RESERVATION OR CANCELLATION TICKET")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("TRAIN NUMBER:\t",x)
    print("TRAIN NAME:\t",y)
    print("DATE OF JOURNEY:\t",z)
    print("CLASS:\t",a)
    print("NUMBER OF BERTHS:\t",b)
    print("STATION FROM ......TO........\t",c)
    print("BOARDING AT:\t",d)
    for i in range (b): 
          print("NAME IN BLOCK LETTERS:\t",name[i])
          print("AGE:\t",age[i])
          print("GENDER:\t",gen[i])
    print("\t\t\tRETURN JOURNEY DETAILS ")
    print("TRAIN NUMBER:\t",x1)
    print("TRAIN NAME:\t",y1)
    print("DATE OF JOURNEY:\t",z1)
    print("CLASS:\t",a1)
    print("STATION FROM ......TO........\t",b1)
    print("BOARDING AT:\t",c1)
    print("NAME OF THE APPLICANT:\t",name1)
    print("ADDRESS:\t",add)
    print("MOBILE NUMBER:\t",mobile)  
    print("TICKET AMOUNT:\t",price)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t\t\tWELCOME TO SOUTHERN RAILWAY RESERVATION")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
p=int(input("RESERVATION/CANCELLATION"))
q=int(input("ORDINARY/TATKAL"))
x,y,z,a,b,c,d=reserve(p,q)
name,age,gen,choice=passenger_input(b)
x1,y1,z1,a1,b1,c1,name1,add,mobile=return_details(p)
price=ticket_price(p,q,b)
print_ticket(x,y,z,a,b,c,d,name,age,gen,x1,y1,z1,a1,b1,c1,name1,add,mobile,price)


    
        
        
