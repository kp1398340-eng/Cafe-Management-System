from tkinter import *
from PIL import Image, ImageTk
from customer import cust_win
from menu import menu_win
from booking import booking_win
from sevice import service_win
from feedback import feedback_win
from details import details_win
from order import order_win
from tkinter import messagebox

class index_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
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
        lbl_title = Label(self.root, text="Brew Universe Cafe", font=("Bradley Hand ITC", 35, "bold"),
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

        # ================== image ==================
        img3 = Image.open(r"images/cafe7.png")
        img3 = img3.resize((1230, 640), Image.Resampling.LANCZOS)  # Updated
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg11 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg11.place(x=225, y=0, width=1230, height=640)

        # ================== DOWN image ==================
        img4 = Image.open(r"images/cafe8.png")
        img4 = img4.resize((230, 240), Image.Resampling.LANCZOS)  # Updated
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg14 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg14.place(x=0, y=340, width=230, height=240)

    def cust_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = cust_win(self.new_window)

    def menu_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = menu_win(self.new_window)

    def booking_detail(self):
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
            self.root.destroy()  # Destroy the current window

            from login import Login_Window  # Import the login window
            new_root = Tk()  # Create a new Tkinter root
            app = Login_Window(new_root)  # Initialize the login form
            new_root.mainloop()  # Run the new login window




if __name__ == "__main__":
    root = Tk()
    obj = index_win(root)
    root.mainloop()
