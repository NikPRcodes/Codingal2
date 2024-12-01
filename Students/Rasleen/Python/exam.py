working = int(input("Enter the total number of working days: "))
absent = int(input("Enter the total number of days for absent: "))

present = working - absent

print("That means you were presnt on the following number of days out of the total working days, that is ", present)

Percentage = (present/working)*100

print("Your Percentage of class attented is " , Percentage)

if Percentage < 75:
    print("Sorry, you will not be able to sit in the exam")
else:
    print("Congratulations, you will be able to sit in the exam")