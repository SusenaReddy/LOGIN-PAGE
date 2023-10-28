import tkinter as tk
from tkinter import messagebox
user_data = {}
def check_login(username, password):
    return username in user_data and user_data[username] == password
def login():
    username = username_entry.get()
    password = password_entry.get()
    if check_login(username, password):
        open_welcome_page(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
def open_welcome_page(username):
    login_window.destroy()
    welcome_window = tk.Tk()
    welcome_window.title("Welcome")
    welcome_label = tk.Label(welcome_window, text=f"Welcome, {username}! Have a good day!")
    welcome_label.pack(padx=20, pady=20)
    welcome_window.mainloop()
def register():
    registration_window = tk.Tk()
    registration_window.title("Registration")
    def register_user():
        new_username = register_username_entry.get()
        new_password = register_password_entry.get()
        if new_username and new_password:
            if new_username not in user_data:
                user_data[new_username] = new_password
                messagebox.showinfo("Registration Successful", "User registered successfully!")
                registration_window.destroy()
            else:
                messagebox.showerror("Registration Failed", "Username already exists.")
        else:
            messagebox.showerror("Registration Failed", "Please enter both username and password.")
    register_username_label = tk.Label(registration_window, text="New Username:")
    register_username_label.pack(pady=5)
    register_username_entry = tk.Entry(registration_window)
    register_username_entry.pack(pady=5)
    register_password_label = tk.Label(registration_window, text="New Password:")
    register_password_label.pack(pady=5)
    register_password_entry = tk.Entry(registration_window, show="*")
    register_password_entry.pack(pady=5)

    # Register Button in registration window
    register_button = tk.Button(registration_window, text="Register", command=register_user)
    register_button.pack(pady=10)

    # Run the registration window
    registration_window.mainloop()

# Create the main window
login_window = tk.Tk()
login_window.title("Login")

# Username Label and Entry for login
username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=10)

# Password Label and Entry for login
password_label = tk.Label(login_window, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=10)

# Login Button
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

# Register Button
register_button = tk.Button(login_window, text="Register", command=register)
register_button.pack(pady=10)

# Run the main window
login_window.mainloop()
