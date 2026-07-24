from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
import string
import re

class forget_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Forget Password")
        self.root.geometry("1550x800+0+0")

        # Database connection
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="cafe_food")
        self.cursor = self.conn.cursor()

        # Load the background image
        self.bg = ImageTk.PhotoImage(file=r"images/cafe7.png")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for input fields
        frame = Frame(self.root, bg="white", bd=3, relief=RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=400, height=500)

        # Title Label
        title_label = Label(frame, text="FORGET PASSWORD", font=("Arial", 20, "bold"), bg="white", pady=10 , fg="brown")
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username Input
        label_username = Label(frame, text="Username:", font=("Arial", 12), bg="white", fg="brown")
        label_username.grid(row=1, column=0, padx=20, pady=5, sticky=W)
        self.entry_username = Entry(frame, width=30)
        self.entry_username.grid(row=1, column=1, pady=5, padx=10)

        # Email Input
        label_email = Label(frame, text="Email:", font=("Arial", 12), bg="white", fg="brown")
        label_email.grid(row=2, column=0, padx=20, pady=5, sticky=W)
        self.entry_email = Entry(frame, width=30)
        self.entry_email.grid(row=2, column=1, pady=5, padx=10)

        # Security Question Input
        label_security_question = Label(frame, text="Security Question:", font=("Arial", 12), bg="white", fg="brown")
        label_security_question.grid(row=3, column=0, padx=20, pady=5, sticky=W)
        self.security_question = ttk.Combobox(frame, state="readonly", values=["Your pet's name?", "Your first school?", "Your favorite food?"], width=28)
        self.security_question.grid(row=3, column=1, pady=5, padx=10)

        label_answer = Label(frame, text="Answer:", font=("Arial", 12), bg="white", fg="brown")
        label_answer.grid(row=4, column=0, padx=20, pady=5, sticky=W)
        self.entry_answer = Entry(frame, width=30)
        self.entry_answer.grid(row=4, column=1, pady=5, padx=10)

        # New Password Input
        label_new_password = Label(frame, text="New Password:", font=("Arial", 12), bg="white", fg="brown")
        label_new_password.grid(row=5, column=0, padx=20, pady=5, sticky=W)
        self.entry_new_password = Entry(frame, show="*", width=30)
        self.entry_new_password.grid(row=5, column=1, pady=5, padx=10)

        # Confirm Password Input
        label_confirm_password = Label(frame, text="Confirm Password:", font=("Arial", 12), bg="white", fg="brown")
        label_confirm_password.grid(row=6, column=0, padx=20, pady=5, sticky=W)
        self.entry_confirm_password = Entry(frame, show="*", width=30)
        self.entry_confirm_password.grid(row=6, column=1, pady=5, padx=10)

        # Buttons
        button_reset_password = Button(frame, text="Reset Password", command=self.reset_password, bg="brown", fg="white")
        button_reset_password.grid(row=10, column=0, columnspan=2, pady=5, ipadx=5)

        button_generate_password = Button(frame, text="Generate Password", command=self.generate_password, bg="brown", fg="white")
        button_generate_password.grid(row=11, column=0, columnspan=2, pady=5, ipadx=5)

    def reset_password(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        security_q = self.security_question.get()
        security_ans = self.entry_answer.get()
        new_password = self.entry_new_password.get()
        confirm_password = self.entry_confirm_password.get()

        if not all([username, email, security_q, security_ans, new_password, confirm_password]):
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        if new_password != confirm_password:
            messagebox.showerror("Mismatch", "Passwords do not match.")
            return

        if len(new_password) < 8 or not re.search(r"[A-Z]", new_password) or not re.search(r"[a-z]", new_password) or not re.search(r"[0-9]", new_password) or not re.search(r"[!@#$%^&*]", new_password):
            messagebox.showerror("Weak Password", "Password must be at least 8 characters long and include upper/lower case letters, a number, and a special character.")
            return

        # Check if user exists
        query = "SELECT * FROM users WHERE username=%s AND email=%s AND security_question=%s AND security_answer=%s"
        self.cursor.execute(query, (username, email, security_q, security_ans))
        user = self.cursor.fetchone()

        if user:
            update_query = "UPDATE users SET password=%s WHERE username=%s"
            self.cursor.execute(update_query, (new_password, username))
            self.conn.commit()
            messagebox.showinfo("Success", "Your password has been updated.")
        else:
            messagebox.showerror("Error", "User details do not match. Please try again.")

    def generate_password(self):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        self.entry_new_password.delete(0, END)
        self.entry_new_password.insert(0, password)
        self.entry_confirm_password.delete(0, END)
        self.entry_confirm_password.insert(0, password)
        messagebox.showinfo("Generated Password", f"Generated strong password: {password}")

if __name__ == "__main__":
    root = Tk()
    app = forget_win(root)
    root.mainloop()
