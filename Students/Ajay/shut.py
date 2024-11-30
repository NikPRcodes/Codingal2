word = input("would u like to shut down? (yes/no): ")
while True:
    if word.lower() == "yes":
        break
    elif word.lower() == "no": 
        print("abort shutdown") 
        break
    else: 
        print("sorry")
        break