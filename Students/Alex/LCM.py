numberLargest=int(input("Enter Largest number:"))
numberSmallest=int(input("Enter Smallest number:"))

numberStore= numberSmallest
numbersmallest = numberLargest % numberSmallest
numberLargest= numberStore
print("LCM is:",numberSmallest)