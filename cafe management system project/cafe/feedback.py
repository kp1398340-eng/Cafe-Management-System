from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from details import details_win
from order import order_win
import importlib
from tkinter import messagebox

class feedback_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("1550x800+0+0")

        # ================== MySQL Connection ==================
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="cafe_food")
        self.cursor = self.conn.cursor()

        # ================== UI Design ==================
        img1 = Image.open(r"images/cafe0.png").resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        img2 = Image.open(r"images/cafelogo3.png").resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg_logo = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg_logo.place(x=0, y=0, width=230, height=140)

        lbl_title = Label(self.root, text="CUSTOMER RESPONSE", font=("Bradley Hand ITC", 35, "bold"),
                          bg="#452711", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        lbl_menu = Label(main_frame, text="HOME", font=("Arial Unicode MS", 20, "bold"),
                         bg="#563D2D", fg="WHITE", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

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



        feedback_frame = Frame(self.root, bd=4, relief=RIDGE)
        feedback_frame.place(x=233, y=190, width=1123, height=495)

        img = Image.open(r"images/feedback7.png").resize((1115, 180), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(self.root, image=self.photoimg)
        lbl_img.place(x=237, y=195, width=1115, height=180)

        feedback1_frame = LabelFrame(self.root, text="Customer Feedback", font=("Arial", 16, "bold"), bd=6, fg="brown",
                                     relief=RIDGE, padx=10, pady=10)
        feedback1_frame.place(x=233, y=370, width=1123, height=315)

        lbl_name = Label(feedback1_frame, text="Name:", font=("Arial", 16))
        lbl_name.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.entry_name = Entry(feedback1_frame, font=("Arial", 12))
        self.entry_name.grid(row=0, column=1, pady=5)

        lbl_contact = Label(feedback1_frame, text="Contact No:", font=("Arial", 16))
        lbl_contact.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.entry_contact = Entry(feedback1_frame, font=("Arial", 12))
        self.entry_contact.grid(row=1, column=1, pady=10)

        lbl_feedback = Label(feedback1_frame, text="Feedback:", font=("Arial", 16))
        lbl_feedback.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txt_feedback = Text(feedback1_frame, font=("Arial", 12), width=70, height=5)
        self.txt_feedback.grid(row=2, column=1, columnspan=3, pady=10)

        btn_submit_feedback = Button(feedback1_frame, text="Submit Feedback", font=("Arial", 12, "bold"),
                                     bg="#452711", fg="gold", width=15, command=self.submit_feedback)
        btn_submit_feedback.grid(row=3, column=2, pady=10)

        # Message Label to display success or error messages
        self.message_label = Label(feedback1_frame, text="", font=("Arial", 14, "bold"), fg="green", bg="lightyellow")
        self.message_label.grid(row=4, column=0, columnspan=4, pady=10)

    def submit_feedback(self):
        name = self.entry_name.get().strip()
        contact = self.entry_contact.get().strip()
        feedback = self.txt_feedback.get("1.0", END).strip()

        if name and contact and feedback:
            try:
                self.cursor.execute("INSERT INTO feedback (name, contact, feedback) VALUES (%s, %s, %s)",
                                    (name, contact, feedback))
                self.conn.commit()
                # Update the message label with success message
                self.message_label.config(text="Feedback submitted successfully!", fg="green")
                self.clear_fields()
            except mysql.connector.Error as e:
                # Update the message label with error message
                self.message_label.config(text=f"Database Error: {e}", fg="red")
        else:
            # Update the message label with input error message
            self.message_label.config(text="Please fill out all fields.", fg="red")

    
    def clear_fields(self):
        self.entry_name.delete(0, END)
        self.entry_contact.delete(0, END)
        self.txt_feedback.delete("1.0", END)
        # Clear message label
        self.message_label.config(text="")

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
    obj = feedback_win(root)
    root.mainloop()
