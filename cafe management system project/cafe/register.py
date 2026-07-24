from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Ensure Pillow is installed
import mysql.connector  # Import MySQL connector


class Register_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Page")
        self.root.geometry("1550x800+0+0")

        # Load the background image
        self.bg = ImageTk.PhotoImage(file=r"images/cafe7.png")  # Update the path
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for the registration form
        frame = Frame(self.root, bg="white", bd=10, relief=RIDGE)
        frame.place(x=450, y=60, width=600, height=600)

        # Heading label
        heading = Label(frame, text="REGISTER", font=("Arial", 24, "bold"), fg="brown", bg="white")
        heading.place(x=230, y=20)

        # Username label and entry
        username_lbl = Label(frame, text="Username", font=("Arial", 14), bg="white" , fg="brown")
        username_lbl.place(x=40, y=80)
        self.username_entry = Entry(frame, font=("Arial", 14), bd=2)
        self.username_entry.place(x=40, y=110, width=500)

        # Email label and entry
        email_lbl = Label(frame, text="Email", font=("Arial", 14), bg="white", fg="brown")
        email_lbl.place(x=40, y=160)
        self.email_entry = Entry(frame, font=("Arial", 14), bd=2)
        self.email_entry.place(x=40, y=190, width=500)

        # Phone label and entry
        phone_lbl = Label(frame, text="Phone Number", font=("Arial", 14), bg="white" , fg="brown")
        phone_lbl.place(x=40, y=240)
        self.phone_entry = Entry(frame, font=("Arial", 14), bd=2)
        self.phone_entry.place(x=40, y=270, width=500)

        # Password label and entry
        password_lbl = Label(frame, text="Password", font=("Arial", 14), bg="white", fg="brown")
        password_lbl.place(x=40, y=320)
        self.password_entry = Entry(frame, font=("Arial", 14), bd=2, show="*")
        self.password_entry.place(x=40, y=350, width=500)

        # Confirm Password label and entry
        confirm_password_lbl = Label(frame, text="Confirm Password", font=("Arial", 14), bg="white", fg="brown")
        confirm_password_lbl.place(x=40, y=400)
        self.confirm_password_entry = Entry(frame, font=("Arial", 14), bd=2, show="*")
        self.confirm_password_entry.place(x=40, y=430, width=500)

        # Terms and Conditions Checkbox
        self.terms_var = IntVar()
        terms_checkbox = Checkbutton(frame, text="I agree to the terms and conditions", variable=self.terms_var, font=("Arial", 12), bg="white", fg="brown")
        terms_checkbox.place(x=40, y=470)

        # Register button
        register_button = Button(frame, text="Register", font=("times new roman", 15, "bold"), bg="brown", fg="white", command=self.register)
        register_button.place(x=50, y=520, width=200)

        # Login button
        login_button = Button(frame, text="Login", font=("times new roman", 15, "bold"), bg="brown", fg="white", command=self.login)
        login_button.place(x=310, y=520, width=200)

    def register(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        terms_accepted = self.terms_var.get()

        if username == "" or email == "" or phone == "" or password == "" or confirm_password == "":
            messagebox.showerror("Error", "All fields are required")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        elif not terms_accepted:
            messagebox.showerror("Error", "You must accept the terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",  
                    user="root",  
                    password="",  
                    database="cafe_food"  
                )
                cursor = conn.cursor()
                
                # Check if email already exists
                cursor.execute("SELECT * FROM user_details WHERE email = %s", (email,))
                row = cursor.fetchone()
                if row:
                    messagebox.showerror("Error", "Email already registered")
                else:
                    cursor.execute(
                        "INSERT INTO user_details (name, email, phone, password) VALUES (%s, %s, %s, %s)",
                        (username, email, phone, password)
                    )
                    conn.commit()
                    messagebox.showinfo("Success", f"Registration successful for {username}")
                    self.clear_fields()

                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")

    def login(self):
        from login import Login_Window
        self.new_window = Toplevel(self.root)
        self.app = Login_Window(self.new_window)

    def clear_fields(self):
        self.username_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.confirm_password_entry.delete(0, END)
        self.terms_var.set(0)

if __name__ == "__main__":
    root = Tk()
    app = Register_win(root)
    root.mainloop()
