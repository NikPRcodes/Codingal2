import tkinter as tk

# Function to check password strength
def check_password_strength():
    password = entry.get()  # Get the password from the entry widget
    length = len(password)
    
    
    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "lightgreen"
    else:
        strength = "Very Strong"
        color = "darkgreen"
    
    # Update the label with strength and color
    strength_label.config(text=strength, fg=color)

# Create the main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

# Create a Label for the Password Entry
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=10)

# Create an Entry widget for password input
entry = tk.Entry(root, show="*")
entry.pack(pady=10)

# Create a Button to check the password strength
check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=20)

# Create a Label to display the password strength
strength_label = tk.Label(root, text="", font=("Arial", 14))
strength_label.pack(pady=20)

# Run the application
root.mainloop()