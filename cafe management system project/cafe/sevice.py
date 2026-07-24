from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from feedback import feedback_win
from details import details_win
from order import order_win
import importlib

class service_win:
    def __init__(self, root):
        self.root = root
        self.root.title("cafe Management System")
        self.root.geometry("1550x800+0+0")

        # ================== Image ==================
        img1 = Image.open(r"images/cafe0.png")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)  # Updated
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ================== Logo ==================
        img2 = Image.open(r"images/cafelogo3.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)  # Updated
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg_logo = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg_logo.place(x=0, y=0, width=230, height=140)

        # ================== Title ==================
        lbl_title = Label(self.root, text="SERVICES ", font=("Bradley Hand ITC", 35, "bold"),
                          bg="#452711", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ================== Main Frame ==================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ================== Menu Label ==================
        lbl_menu = Label(main_frame, text="HOME", font=("Arial Unicode MS", 20, "bold"),
                         bg="#563D2D", fg="WHITE", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ================== Button Frame ==================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=46, width=228, height=300)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_detail, width=22, font=("times new roman", 14, "bold"),
                          bg="#987554", fg="#664229", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="MENU",command=self.menu_detail, width=22, font=("times new roman", 14, "bold"),
                          bg="#987554", fg="#664229", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        booking_btn = Button(btn_frame, text="BOOKING",command=self.booking_detail, width=22, font=("times new roman", 14, "bold"),
                             bg="#987554", fg="#664229", bd=0, cursor="hand2")
        booking_btn.grid(row=2, column=0, pady=1)

        service_btn = Button(btn_frame, text="SERVICE", command=self.service_detail,width=22, font=("times new roman", 14, "bold"),
                             bg="#987554", fg="#664229", bd=0, cursor="hand2")
        service_btn.grid(row=3, column=0, pady=1)

        feedback_btn = Button(btn_frame, text="FEEDBACK",command=self.feedback_detail, width=22, font=("times new roman", 14, "bold"),
                              bg="#987554", fg="#664229", bd=0, cursor="hand2")
        feedback_btn.grid(row=4, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS",command=self.details_detail, width=22, font=("times new roman", 14, "bold"),
                             bg="#987554", fg="#664229", bd=0, cursor="hand2")
        details_btn.grid(row=5, column=0, pady=1)

        report_btn = Button(btn_frame, text="ORDER",command=self.order_detail, width=22, font=("times new roman", 14, "bold"),
                            bg="#987554", fg="#664229", bd=0, cursor="hand2")
        report_btn.grid(row=6, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout,width=22, font=("times new roman", 14, "bold"),
                            bg="#987554", fg="#664229", bd=0, cursor="hand2")
        logout_btn.grid(row=7, column=0, pady=1)

        # ================== DOWN image ==================
        img4 = Image.open(r"images/cafe8.png")
        img4 = img4.resize((230, 240), Image.Resampling.LANCZOS)  # Updated
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg14 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg14.place(x=0, y=340, width=230, height=240)

        #================service===============
        main_frame1 = Frame(self.root, bg="white")
        main_frame1.place(x=237, y=195, width=1200, height=493)

        img5 = Image.open(r"images/service1.png")
        img5 = img5.resize((270, 220), Image.Resampling.LANCZOS)  # Updated
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg15 = Label(main_frame1, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg15.place(x=10, y=10, width=270, height=220)

        img6 = Image.open(r"images/service.png")
        img6 = img6.resize((270, 220), Image.Resampling.LANCZOS)  # Updated
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lblimg16 = Label(main_frame1, image=self.photoimg6, bd=4, relief=RIDGE)
        lblimg16.place(x=290, y=10, width=270, height=220)

        img7 = Image.open(r"images/service2.png")
        img7 = img7.resize((270, 220), Image.Resampling.LANCZOS)  # Updated
        self.photoimg7 = ImageTk.PhotoImage(img7)

        lblimg17 = Label(main_frame1, image=self.photoimg7, bd=4, relief=RIDGE)
        lblimg17.place(x=570, y=10, width=270, height=220)

        img8 = Image.open(r"images/service3.png")
        img8 = img8.resize((260, 220), Image.Resampling.LANCZOS)  # Updated
        self.photoimg8 = ImageTk.PhotoImage(img8)

        lblimg18 = Label(main_frame1, image=self.photoimg8, bd=4, relief=RIDGE)
        lblimg18.place(x=850, y=10, width=260, height=220)

        img9 = Image.open(r"images/service4.png")
        img9 = img9.resize((270, 220), Image.Resampling.LANCZOS)  # Updated
        self.photoimg9 = ImageTk.PhotoImage(img9)

        lblimg19 = Label(main_frame1, image=self.photoimg9, bd=4, relief=RIDGE)
        lblimg19.place(x=10, y=250, width=270, height=220)

        img10 = Image.open(r"images/service5.png")
        img10 = img10.resize((270, 220), Image.Resampling.LANCZOS)  # Updated
        self.photoimg10 = ImageTk.PhotoImage(img10)

        lblimg20 = Label(main_frame1, image=self.photoimg10, bd=4, relief=RIDGE)
        lblimg20.place(x=290, y=250, width=270, height=220)

        img11 = Image.open(r"images/service7.png")
        img11 = img11.resize((270, 220), Image.Resampling.LANCZOS)  # Updated
        self.photoimg11 = ImageTk.PhotoImage(img11)

        lblimg21 = Label(main_frame1, image=self.photoimg11, bd=4, relief=RIDGE)
        lblimg21.place(x=570, y=250, width=270, height=220)

        img12 = Image.open(r"images/service6.png")
        img12 = img12.resize((260, 220), Image.Resampling.LANCZOS)  # Updated
        self.photoimg12 = ImageTk.PhotoImage(img12)

        lblimg22 = Label(main_frame1, image=self.photoimg12, bd=4, relief=RIDGE)
        lblimg22.place(x=850, y=250, width=260, height=220)

        

        
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
        self.new_window = Toplevel(self.root)
        self.app = service_win(self.new_window)

    def feedback_detail(self):
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
    obj = service_win(root)
    root.mainloop()