import math

def trig_values():
    
    angle = float(input("Enter the angle in degrees: "))

    sin = math.sin(angle)
    cos = math.cos(angle)
    tan = math.tan(angle)

    choice = input("which value would u like to obtain? (sin/cos/tan) : ")

    if choice == "sin":
        print("the value is", sin)
    elif choice == "cos":
        print("the value is", cos)
    elif choice == "tan":
        print("the value is", tan)
    
trig_values()