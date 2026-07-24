from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector  
from index import index_win
from register import Register_win
from forget import forget_win

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Load and resize image
        self.bg_image = Image.open("images/cafe7.png")
        self.bg_resized = self.bg_image.resize((1550, 800), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_resized)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white", bd=2)
        frame.place(x=510, y=170, width=340, height=450)

        img1 = Image.open(r"images/pro2.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbimg1 = Label(self.root, image=self.photoimage1, bg="#664229", borderwidth=0)
        lbimg1.place(x=630, y=180, width=100, height=90)

        get_str = Label(frame, text="WELCOME", font=("Bradley Hand ITC", 23, "bold"), fg="gold", bg="white")
        get_str.place(x=95, y=90)

        username_lbl = Label(frame, text="USERNAME", font=("Times New Roman", 15, "bold"), fg="#563D2D", bg="white")
        username_lbl.place(x=40, y=155)

        self.txtuser = ttk.Entry(frame, font=("Times New Roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="PASSWORD", font=("Times New Roman", 15, "bold"), fg="#563D2D", bg="white")
        password_lbl.place(x=40, y=225)

        self.txtpass = ttk.Entry(frame, font=("Times New Roman", 15, "bold"), show='*')
        self.txtpass.place(x=40, y=250, width=270)

        # Login Button
        loginbtn = Button(frame, text="Login", command=self.login, font=("Times New Roman", 15, "bold"), bd=3, relief=RIDGE, bg="#452711", fg="gold", activebackground="white", activeforeground="blue")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Forgot Password Button
        forgetbtn = Button(frame, text="FORGET PASSWORD", command=self.forget_detail, font=("Times New Roman", 10, "bold"), borderwidth=0, fg="#563D2D", bg="white", activebackground="black", activeforeground="white")
        forgetbtn.place(x=22, y=370, width=130)

        # Register Button
        registerbtn = Button(frame, text="NEW USER REGISTER", command=self.register_detail, font=("Times New Roman", 10, "bold"), borderwidth=0, fg="#563D2D", bg="white", activebackground="black", activeforeground="white")
        registerbtn.place(x=10, y=400, width=160)

    # 🔹 **Updated Login Function with MySQL Authentication**
    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cafe_food"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM user_details WHERE name = %s AND password = %s", (username, password))
            row = cursor.fetchone()

            if row:
                messagebox.showinfo("Success", f"Welcome, {username}!")
                self.root.destroy()
                from index import index_win
                new_root = Tk()
                index_win(new_root)
                new_root.mainloop()
            else:
                messagebox.showerror("Invalid", "Invalid username or password")

            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")

    def index_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = index_win(self.new_window)

    def register_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_win(self.new_window)

    def forget_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = forget_win(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
