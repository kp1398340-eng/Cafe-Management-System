import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to handle login process
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Connect to MySQL Database
    conn = mysql.connector.connect(host="localhost", user="root", password="your_password", database="food_cafe")
    cursor = conn.cursor()

    # Check if the entered credentials match the admin record
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        # If credentials are correct, open the dashboard
        messagebox.showinfo("Login Success", "Welcome to the Admin Panel!")
        root.destroy()
        open_dashboard()
    else:
        # If credentials are incorrect, show error message
        messagebox.showerror("Login Failed", "Invalid Username or Password.")
    
    cursor.close()
    conn.close()

# Function to open the Dashboard (this can be extended later)
def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Admin Dashboard")
    dashboard.geometry("800x600")
    
    # Add a simple label to the dashboard as an example
    dashboard_label = tk.Label(dashboard, text="Welcome to the Admin Dashboard", font=("Arial", 20))
    dashboard_label.pack(pady=20)
    
    # Main loop for the dashboard window
    dashboard.mainloop()

# Create the main login window
root = tk.Tk()
root.title("Admin Login")
root.geometry("400x300")

# Username Label and Entry
tk.Label(root, text="Username:").pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password Label and Entry
tk.Label(root, text="Password:").pack(pady=10)
password_entry = tk.Entry(root, show="*")  # Hide the password input
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Main loop for the login window
root.mainloop()
