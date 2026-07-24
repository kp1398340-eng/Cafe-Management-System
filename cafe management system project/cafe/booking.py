from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry  # Install tkcalendar: pip install tkcalendar
import mysql.connector
from sevice import service_win
from feedback import feedback_win
from details import details_win
from order import order_win
import importlib

class booking_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("1550x800+0+0")

        # MySQL Connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Change if needed
            password="",  # Change to your MySQL password
            database="cafe_food"
        )
        self.cursor = self.conn.cursor()


        # ================== Header Image ==================
        img1 = Image.open(r"images/cafe0.png").resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ================== Logo ==================
        img2 = Image.open(r"images/cafelogo3.png").resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg_logo = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg_logo.place(x=0, y=0, width=230, height=140)

        # ================== Title ==================
        lbl_title = Label(self.root, text="ONLINE BOOK A TABLE", font=("Bradley Hand ITC", 35, "bold"),
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

        img4 = Image.open(r"images/cafe8.png").resize((230, 240), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE).place(x=0, y=340, width=230, height=240)

        img5 = Image.open(r"images/cafe0.png").resize((600, 500), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE).place(x=227, y=0, width=600, height=500)


        # ================== Reservation Frame ==================
        frame = LabelFrame(self.root, text="RESERVATION", font=("Arial", 12, "bold"), bd=4, fg="gold", bg="#563D2D", relief=RIDGE, padx=2, pady=2)
        frame.place(x=829, y=195, width=525, height=495)

        lbl_form_title = Label(frame, text="Fill Your Booking Details", font=("sarif", 14), bg="#452711", fg="white", bd=2, relief=RIDGE)
        lbl_form_title.place(x=0, y=15, width=515, height=40)

        # Input Fields
        Label(frame, text="Name", font=("Arial", 12), bg="#563D2D", fg="white").place(x=30, y=80)
        self.entry_name = Entry(frame, width=21, font=("Arial", 14))
        self.entry_name.place(x=180, y=80)

        Label(frame, text="Email", font=("Arial", 12), bg="#563D2D", fg="white").place(x=30, y=120)
        self.entry_email = Entry(frame, width=21, font=("Arial", 14))
        self.entry_email.place(x=180, y=120)

        Label(frame, text="Date", font=("Arial", 12), bg="#563D2D", fg="white").place(x=30, y=160)
        self.entry_date = DateEntry(frame, font=("Arial", 12), width=23, background="darkblue", foreground="white", borderwidth=2)
        self.entry_date.place(x=180, y=160)

        Label(frame, text="Time", font=("Arial", 12), bg="#563D2D", fg="white").place(x=30, y=200)
        self.entry_time = Entry(frame, width=21, font=("Arial", 14))
        self.entry_time.place(x=180, y=200)

        Label(frame, text="No. of People", font=("Arial", 12), bg="#563D2D", fg="white").place(x=30, y=240)
        self.combo_people = ttk.Combobox(frame, values=[str(i) for i in range(1, 21)], font=("Arial", 12), width=10)
        self.combo_people.set("1")
        self.combo_people.place(x=180, y=240)

        Label(frame, text="Special Request", font=("Arial", 12), bg="#563D2D", fg="white").place(x=30, y=280)
        self.text_special_request = Text(frame, width=45, height=5, font=("Arial", 12))
        self.text_special_request.place(x=30, y=310)

        # Book Now Button
        Button(frame, text="BOOK NOW", bg="#FFA500", fg="black", font=("Arial", 12, "bold"), command=self.book_now).place(x=200, y=420, width=140)

        # Success Message Label
        self.success_label = Label(frame, text="", font=("Arial", 14, "bold"), fg="green", bg="#563D2D")
        self.success_label.place(x=30, y=450, width=460)

    def clear_fields(self):
        """ Clears the input fields after booking """
        self.entry_name.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_time.delete(0, END)
        self.combo_people.set("1")
        self.text_special_request.delete("1.0", END)
        self.success_label.config(text="")  # Clear success message

    def __del__(self):
        """ Closes the database connection when the app is closed """
        self.conn.close()

    def book_now(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        date = self.entry_date.get()
        time = self.entry_time.get()
        num_people = self.combo_people.get()
        special_request = self.text_special_request.get("1.0", END).strip()

        # Validate the fields
        if not name or not email or not time:
            self.success_label.config(text="Please fill in all required fields.", font=("Arial", 12),fg="gold")
            return

        try:
            # Check if the same date and time is already booked
            self.cursor.execute("SELECT * FROM bookings WHERE booking_date = %s AND booking_time = %s", (date, time))
            existing_booking = self.cursor.fetchone()

            if existing_booking:
                self.success_label.config(text="This time slot is already booked. Please choose another time.",font=("Arial", 12), fg="gold")
                return

            # Insert into MySQL Database
            sql = "INSERT INTO bookings (name, email, booking_date, booking_time, people, special_request) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, email, date, time, num_people, special_request)
            self.cursor.execute(sql, values)
            self.conn.commit()

            # Show success message after booking
            self.success_label.config(text=f"Thank you {name}, your table is booked for {date} at {time}!", fg="green")

            # Clear input fields
            self.clear_fields()

        except Exception as e:
            self.success_label.config(text=f"Error: {e}", fg="red")

            
    def cust_detail(self):
        cust_win = importlib.import_module('customer').cust_win
        self.new_window = Toplevel(self.root)
        self.app = cust_win(self.new_window)

    def menu_detail(self):
        menu_win = importlib.import_module('menu').menu_win
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
            self.root.destroy()
            print("User logged out. Redirecting to login page...")

    def exit_app(self):
        self.root.destroy()


# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = booking_win(root)
    root.mainloop()
