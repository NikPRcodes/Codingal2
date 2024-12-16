import sys
def initial_phonebook():
    columns=5
    rows=int(input("Enter the number of contacts you wish to have"))
    phone_book = []

    for i in range(rows):
        print("Enter the details for contact #",i+1)
        print("NOTE: The asterisk(*) indicates mandatory fields.")
        temp = []
        for j in range(columns):
            if j==0:
                temp.append(input("Enter name*:"))
                if temp[j]=="" or temp[j]==" ":
                    sys.exit("This is a mandatory field. Process exiting")
            if j==1:
                temp.append(int(input("Enter phone number*:")))
            if j==2:
                temp.append(input("Enter the email address:"))
                if temp[j]=="" or temp[j]==" ":
                    temp[j]= None
            if j==3:
                temp.append(input("Enter date of birth (dd/mm/yy):"))
                if temp[j]=="" or temp[j]==" ":
                    temp[j]= None
            if j==4:
                temp.append(input("Enter category of contact(Work/Family/Friends/Others):"))
                if temp[j]=="" or temp[j]==" ":
                    temp[j]= None
        phone_book.append(temp)

    print(phone_book)
    return(phone_book)

def menu():
    print("*************************************************************************************");print("\t\t\tSMARTPHONE DIRECTORY", flush=False);
    print("*************************************************************************************");print("\tYou can now perform the following operations on this phonebook\n");
    print("1. Add a new contact");
    print("2. Remove an existing contact");
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    choice=int(input("Please enter your choice:" ))

    return choice

def add_contact(pb):
   dip=[]
   for i in range(5):
    if i==0:
        dip.append(str(input("Enter name:")))
    elif i==1:
        dip.append(int(input("Enter number:")))
    elif i==2:
        dip.append(str(input("Enter e-mail address:")))
    elif i==3:
        dip.append(str(input("Enter date of birth(dd/mm/yy):")))
    elif i==4:
        dip.append(str(input("Enter category(Family/Friends/Work/Others:)")))

    pb.append(dip)

    return pb 
def remove_existing(pb):
    query=input("Please enter the name of the contact you wish to remove:")
    temp=0
    for i in range(len(pb)):
        if query==pb[i][0]:
            temp+=1
            pb.pop(i)
            return pb

    if temp==0:
        print("Sorry, we could not find the contact you wished to remove.")
        return pb

def delete_all(pb):
    pb.clear()
    return pb

def search_contacts(pb):
    search_criteria= int(input("Please enter your search criteria: 1.Name 2. Phone No. 3. Email ID  4.Date of Birth 5. Category"))
    temp=-1
    matches=[]
    if search_criteria==1:
        query=input("Please enter the name of the contact you wish to locate:")
        for i in range(len(pb)):
            if query==pb[i][0]:
                print("We have found the contact you wish to locate.")
                temp=i
                matches.append(pb[i])
    elif search_criteria==2:
        query=int(input("Please enter the phone number of the contact you wish to locate:"))

        for i in range(len(pb)):
            if query==pb[i][1]:
                print("We have found the contact you wish to locate.")
                temp=i
                matches.append(pb[i])
    elif search_criteria==3:
        query=input("Please enter the email ID of the contact you wish to locate:")
        for i in range(len(pb)):
            if query==pb[i][2]:
                print("We have found the contact you wish to locate.")
                temp=i
                matches.append(pb[i])
    elif search_criteria==4:
        query=input("Please enter the date of birth of the contact you wish to locate:")
        for i in range(len(pb)):
            if query==pb[i][3]:
                print("We have found the contact you wish to locate.")
                temp=i
                matches.append(pb[i])
    elif search_criteria==5:
        query==input("Please enter the category of the contact you wish to locate (Work/Friends/Family/Others:)")
        for i in range(len(pb)):
            if query==pb[i][4]:
                print("We have found the contact you wish to locate.")
                temp=i
                matches.append(pb[i])
    else:
        sys.exit("Invalid Search Criteria. Exiting phonebook...")
    if temp==0:
        print("We did not find the contact you wish to locate.")
        return -1
    else:
        #display(matches)
        return temp
def display(pb):
    print(pb)
def exit_phonebook():
    sys.exit("Exiting phonebook...")

pb=initial_phonebook()
choice=menu()

if choice==1:
    pb=add_contact(pb)
elif choice==2:
    pb=remove_existing(pb)
elif choice==3:
    pb=delete_all(pb)
elif choice==4:
    lc=search_contacts(pb)
    print(lc)
elif choice==5:
    display(pb)
else:
    exit_phonebook()









    