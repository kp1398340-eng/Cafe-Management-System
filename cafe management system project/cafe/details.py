from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from order import order_win
import importlib
from tkinter import messagebox

class details_win :
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("1550x800+0+0")

        # ================== Image ==================
        img1 = Image.open(r"images/cafe0.png")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)
        
        # ================== Logo ==================
        img2 = Image.open(r"images/cafelogo3.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lblimg_logo = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg_logo.place(x=0, y=0, width=230, height=140)
        
        # ================== Title ==================
        lbl_title = Label(self.root, text="CAFE DETAILS", font=("Bradley Hand ITC", 35, "bold"),
                          bg="#452711", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)
        
        # ================== Main Frame ==================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ================== Sidebar Menu ==================
        lbl_menu = Label(main_frame, text="HOME", font=("Arial Unicode MS", 20, "bold"),
                         bg="#563D2D", fg="WHITE", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
        
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=46, width=228, height=300)
        
        buttons = ["CUSTOMER", "MENU", "BOOKING", "SERVICE", "FEEDBACK", "DETAILS", "ORDER", "LOGOUT"]
        commands = [self.cust_detail, self.menu_detail, self.booking_detail, self.service_detail,
                    self.feedback_detail, self.details_detail, self.order_detail, self.logout]
        
        for i, (btn_text, cmd) in enumerate(zip(buttons, commands)):
            Button(btn_frame, text=btn_text, command=cmd, width=22, font=("times new roman", 14, "bold"),
                   bg="#987554", fg="#664229", bd=0, cursor="hand2").grid(row=i, column=0, pady=1)
            

        # ================== DOWN image ==================
        img4 = Image.open(r"images/cafe8.png")
        img4 = img4.resize((230, 240), Image.Resampling.LANCZOS)  # Updated
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg14 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg14.place(x=0, y=340, width=230, height=240)

        
        # ================== Cafe Details Section ==================
        details_frame = Frame(self.root, bd=4, relief=RIDGE)
        details_frame.place(x=230, y=190, width=1130, height=500)
        
        cafe_name = "BREW UNIVERSE CAFE"
        description = "A cozy place serving fresh and tasty meals."
        experience_year = "10 Years"
        about_us = ("We are a passionate team dedicated to providing high-quality food and beverages.\n"
                    "Our journey started a decade ago, and we continue to serve our customers with love and dedication.\n"
                    "We source the finest ingredients, prepare each meal with care, and strive to create a warm and inviting \natmospherefor everyone.\n\n"
                    "Our commitment to excellence goes beyond just serving delicious meals; we believe in \nbuilding lasting relationships with our customers. \n"
                    "Every dish we create is a reflection of our values: freshness, quality, and innovation. \n"
                    "We constantly explore new flavors and culinary techniques to bring you unique experiences, \nwhether you're enjoying a casual meal or celebrating a special occasion."
                    "In addition to our exceptional food, we take pride in our sustainable practices.\n"
                    "We work with local farmers and suppliers to support the community while reducing our environmental impact.\n"
                    "By choosing organic and ethically sourced ingredients, we ensure that every bite not only tastes good but also contributes to a better world.\n"
                    "Our team is like a family, and we treat every customer as one of our own.\n"
                    "Whether it's your first visit or you've been with us from the beginning, \nwe are here to make you feel welcome, valued, and appreciated.\n"
                    "Join us on our journey and experience the love and passion that goes into every meal we serve.\n"
)
        
        Label(details_frame, text=f"Cafe Name: {cafe_name}", font=("Arial", 14, "bold"), bg="#F5DEB3").place(x=20, y=20)
        Label(details_frame, text=f"Description: {description}", font=("Arial", 12), fg="#452711").place(x=20, y=60)
        Label(details_frame, text=f"Experience: {experience_year}", font=("Arial", 12), fg="#452711").place(x=20, y=100)
        Label(details_frame, text="About Us:", font=("Arial", 16, "bold"), bg="#F5DEB3",fg="#452711").place(x=20, y=140)
        Label(details_frame, text=about_us, font=("Arial", 10), wraplength=700, justify="left",fg="#452711").place(x=20, y=170)
        
        # ================== Cafe Images ==================
        img3 = Image.open(r"images/cafe1.png")
        img3 = img3.resize((400, 450), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(details_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=710, y=20, width=400, height=450)

    def cust_detail(self):
        cust_win = importlib.import_module('customer').cust_win
        self.new_window = Toplevel(self.root)
        self.app = cust_win(self.new_window)

    def menu_detail(self):
        menu_win = importlib.import_module('menu').menu_win
        self.new_window = Toplevel(self.root)
        self.app = menu_win(self.new_window)

    def booking_detail(self):
        booking_win = importlib.import_module('booking').booking_win
        self.new_window = Toplevel(self.root)
        self.app = booking_win(self.new_window)

    def service_detail(self):
        service_win = importlib.import_module('sevice').service_win
        self.new_window = Toplevel(self.root)
        self.app = service_win(self.new_window)

    def feedback_detail(self):
        feedback_win = importlib.import_module('feedback').feedback_win
        self.new_window = Toplevel(self.root)
        self.app = feedback_win(self.new_window)

    def details_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = details_win(self.new_window)

    def order_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = order_win(self.new_window)

    def logout(self):
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            self.root.destroy()
            print("User logged out. Redirecting to login page...")

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = details_win(root)
    root.mainloop()