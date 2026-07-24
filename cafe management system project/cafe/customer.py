from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from menu import menu_win
from booking import booking_win
from sevice import service_win
from feedback import feedback_win
from details import details_win
from order import order_win
from tkinter import messagebox

class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("1550x800+0+0")

        # ================== Database Connection ==================
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cafe_food"
        )
        self.cursor = self.conn.cursor()

        # ================== Variables ==================
        self.var_ref = StringVar()
        self.var_name = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_table_no = StringVar()
        self.var_total_person = StringVar()
        self.var_address = StringVar()

        # ================== Header Image ==================
        img1 = Image.open(r"images/cafe0.png")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ================== Logo Image ==================
        img2 = Image.open(r"images/cafelogo3.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg_logo = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg_logo.place(x=0, y=0, width=230, height=140)

        # ================== Title ==================
        lbl_title = Label(self.root, text="Add Customer Details", font=("Bradley Hand ITC", 35, "bold"),
                          bg="#452711", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

         # ================== Main Frame ==================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)


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



        # ================== Customer Details Section ==================
        frame = LabelFrame(self.root, text="Customer Details", font=("Arial", 12, "bold"), bd=4, relief=RIDGE, padx=2, pady=2)
        frame.place(x=240, y=210, width=370, height=500)

        labels = ["Customer Ref:", "Customer Name:", "Mobile:", "Email:", "Table No:", "Total Person:", "Address:"]
        variables = [self.var_ref, self.var_name, self.var_mobile, self.var_email, self.var_table_no, self.var_total_person, self.var_address]

        for i, text in enumerate(labels):
            Label(frame, text=text, font=("Arial", 12, "bold")).grid(row=i, column=0, sticky=W, padx=5, pady=5)
            Entry(frame, textvariable=variables[i], font=("Arial", 12)).grid(row=i, column=1, pady=5)

        # ================== Buttons ==================
        btn_frame = Frame(frame, bd=0, relief=RIDGE)
        btn_frame.place(x=0, y=410, width=350, height=30)

        Button(btn_frame, text="Add", font=("Arial", 12, "bold"), bg="#452711", fg="gold", width=7, command=self.add_customer).grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Update", font=("Arial", 12, "bold"), bg="#452711", fg="gold", width=7, command=self.update_customer).grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Delete", font=("Arial", 12, "bold"), bg="#452711", fg="gold", width=7, command=self.delete_customer).grid(row=0, column=2, padx=5)
        Button(btn_frame, text="Reset", font=("Arial", 12, "bold"), bg="#452711", fg="gold", width=7, command=self.clear_fields).grid(row=0, column=3, padx=5)

        # ================== Message Display Label ==================
        self.msg_label = Label(frame, text="", font=("Arial", 12, "bold"), fg="green")
        self.msg_label.place(x=10, y=450, width=350, height=30)

        # ================== Data Table ==================
        table_frame = Frame(self.root, bd=4, relief=RIDGE)
        table_frame.place(x=615, y=210, width=740, height=475)

        self.cust_details_table = ttk.Treeview(table_frame, columns=("id", "ref", "name", "mobile", "email", "table_no", "total_person", "address"))
        for col in ("id", "ref", "name", "mobile", "email", "table_no", "total_person", "address"):
            self.cust_details_table.heading(col, text=col.capitalize())
            self.cust_details_table.column(col, width=100)
        self.cust_details_table["show"] = "headings"
        self.cust_details_table.pack(fill=BOTH, expand=1)

        self.fetch_data()

    # ================== Database Functions ==================
    def add_customer(self):
        try:
            self.cursor.execute("INSERT INTO customers (ref, name, mobile, email, table_no, total_person, address) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                (self.var_ref.get(), self.var_name.get(), self.var_mobile.get(), self.var_email.get(), self.var_table_no.get(), self.var_total_person.get(), self.var_address.get()))
            self.conn.commit()
            self.fetch_data()
            self.show_message("Customer added successfully", "green")  # Show message
        except Exception as e:
            self.show_message(f"Error: {str(e)}", "red")  # Show error

    def update_customer(self):
        self.cursor.execute("UPDATE customers SET name=%s, mobile=%s, email=%s, table_no=%s, total_person=%s, address=%s WHERE ref=%s",
            (self.var_name.get(), self.var_mobile.get(), self.var_email.get(), self.var_table_no.get(), self.var_total_person.get(), self.var_address.get(), self.var_ref.get()))
        self.conn.commit()
        self.fetch_data()
        self.show_message("Customer updated successfully", "green")  # Show message

    def delete_customer(self):
        self.cursor.execute("DELETE FROM customers WHERE ref=%s", (self.var_ref.get(),))
        self.conn.commit()
        self.fetch_data()
        self.show_message("Customer deleted successfully", "red")  # Show message

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM customers")
        rows = self.cursor.fetchall()
        self.cust_details_table.delete(*self.cust_details_table.get_children())
        for row in rows:
            self.cust_details_table.insert("", END, values=row)

    def clear_fields(self):
        for var in [self.var_ref, self.var_name, self.var_mobile, self.var_email, self.var_table_no, self.var_total_person, self.var_address]:
            var.set("")

    def show_message(self, message, color):
        """ Display message in the customer page instead of a pop-up """
        self.msg_label.config(text=message, fg=color)
        self.root.after(3000, lambda: self.msg_label.config(text=""))  # Clear after 3 seconds

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
            self.root.destroy()
            print("User logged out. Redirecting to login page...")

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = cust_win(root)
    root.mainloop()
