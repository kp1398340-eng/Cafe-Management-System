import tkinter as tk
from tkinter import RIDGE, Button, Frame, Label, Toplevel, ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import datetime


class order_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("1550x800")

        # Database Connection
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cafe_food"
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {e}")
            return

        self.create_ui()
        self.fetch_cart_data()
    
    def create_ui(self):
        """Create the main UI elements for the order window"""
        # Header Image
        img1 = Image.open(r"images/cafe0.png").resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1, bd=1, relief=RIDGE).place(x=0, y=0, width=1550, height=140)

        # Logo Image
        img2 = Image.open(r"images/cafelogo3.png").resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2, bd=1, relief=RIDGE).place(x=0, y=0, width=230, height=140)

        # Title
        Label(self.root, text="Order", font=("Bradley Hand ITC", 35, "bold"), bg="#452711", fg="gold", bd=4, relief=RIDGE).place(x=0, y=140, width=1550, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1355, height=500)

        # ================== Sidebar Menu ==================
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

        img4 = Image.open(r"images/cafe8.png").resize((230, 240), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE).place(x=0, y=340, width=230, height=240)

        # Customer Name
        Label(main_frame, text="Customer Name:", font=("Arial", 14)).place(x=250, y=20)
        self.customer_name_var = tk.StringVar()
        self.customer_name_entry = tk.Entry(main_frame, textvariable=self.customer_name_var, font=("Arial", 14))
        self.customer_name_entry.place(x=400, y=20, width=200)
        
        # Cart Section
        self.tree = ttk.Treeview(
            main_frame,
            columns=("ID", "Product Name", "Price", "Quantity"),
            show="headings"
        )

        # Define headings
        self.tree.heading("ID", text="ID")
        self.tree.heading("Product Name", text="Product Name")
        self.tree.heading("Price", text="Price (₹)")
        self.tree.heading("Quantity", text="Quantity")

        # Define column widths
        self.tree.column("ID", width=50)
        self.tree.column("Product Name", width=200)
        self.tree.column("Price", width=100)
        self.tree.column("Quantity", width=100)

        # Adding Scrollbars
        tree_scroll_y = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        tree_scroll_x = ttk.Scrollbar(main_frame, orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)

        # Placing widgets
        self.tree.place(x=250, y=70, width=600, height=300)
        tree_scroll_y.place(x=855, y=70, height=300)  # Adjust x-position based on width
        tree_scroll_x.place(x=250, y=370, width=600)  # Adjust y-position based on height


                
        # Remove from Cart Button
        self.delete_button = Button(main_frame, text="Remove from Cart", command=self.remove_from_cart)
        self.delete_button.place(x=250, y=380, width=200)
        
        # Bill Section
        self.bill_label = Label(main_frame, text="Total: ₹0.00", font=("Arial", 14, "bold"))
        self.bill_label.place(x=250, y=420)
        
        # Generate Bill Button
        self.bill_button = Button(main_frame, text="Generate Bill", command=self.generate_bill)
        self.bill_button.place(x=250, y=460, width=200)

        # Bill Display Box
        self.bill_text = tk.Text(main_frame, font=("Arial", 12), height=10, width=50, bd=4, relief=RIDGE)
        self.bill_text.place(x=880, y=20, width=450, height=440)

        # Insert default text
        self.bill_text.insert(tk.END, "  BILL AREA :  ")

    
    def fetch_cart_data(self):
        """Fetch cart data from the database and display it in the cart table"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            self.cursor.execute("""
                SELECT cart.id, products.name, cart.price, cart.quantity, cart.total_price
                FROM cart
                INNER JOIN products ON cart.product_id = products.id
            """)
            rows = self.cursor.fetchall()
            total_price = sum(float(row[4]) for row in rows)
            gst = total_price * 0.18
            final_price = total_price + gst
            
            for row in rows:
                self.tree.insert("", tk.END, values=(row[0], row[1], f"₹{row[2]:.2f}", row[3]))
            
            self.bill_label.config(text=f"Total: ₹{total_price:.2f} | GST: ₹{gst:.2f} | Final: ₹{final_price:.2f}")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch cart data: {e}")
    
    def remove_from_cart(self):
        """Remove a selected item from the cart"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to remove.")
            return
        
        try:
            item_id = self.tree.item(selected_item, "values")[0]
            self.cursor.execute("DELETE FROM cart WHERE id = %s", (item_id,))
            self.db.commit()
            self.fetch_cart_data()
            messagebox.showinfo("Success", "Item removed from cart.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to remove item: {e}")
    
    import datetime

    def generate_bill(self):
        """Generate the bill and display it in the text box"""
        customer_name = self.customer_name_var.get().strip()
        if not customer_name:
            messagebox.showwarning("Warning", "Please enter customer name before generating the bill.")
            return

        try:
            self.cursor.execute("""
                SELECT products.name, cart.quantity, cart.total_price
                FROM cart
                INNER JOIN products ON cart.product_id = products.id
            """)
            rows = self.cursor.fetchall()

            if not rows:
                messagebox.showwarning("Warning", "Cart is empty! Add items before generating the bill.")
                return

            total_price = sum(float(row[2]) for row in rows)
            gst = total_price * 0.18
            final_price = total_price + gst

            # Get current date and time
            now = datetime.datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS

            # Bill Format
            bill_content = f"Customer Name: {customer_name}\n"
            bill_content += f"Date & Time: {date_time}\n"
            bill_content += "-" * 50 + "\n"
            bill_content += f"{'Product Name':<20}{'Qty':<10}{'Total (₹)':<10}\n"
            bill_content += "-" * 50 + "\n"
            for row in rows:
                bill_content += f"{row[0]:<20}{row[1]:<10}{row[2]:<10.2f}\n"
            bill_content += "-" * 50 + "\n"
            bill_content += f"{'Total':<30} ₹{total_price:.2f}\n"
            bill_content += f"{'GST (18%)':<30} ₹{gst:.2f}\n"
            bill_content += f"{'Final Amount':<30} ₹{final_price:.2f}\n"
            bill_content += "-" * 50 + "\n"

            # Display Bill in Text Box
            self.bill_text.delete(1.0, tk.END)
            self.bill_text.insert(tk.END, bill_content)

            # Clear cart after bill generation
            self.cursor.execute("DELETE FROM cart")
            self.db.commit()
            self.fetch_cart_data()

            # Show success label instead of messagebox
            if hasattr(self, "success_label"):
                self.success_label.config(text="Bill Generated Successfully!", fg="green")
            else:
                self.success_label = Label(self.root, text="Bill Generated Successfully!", font=("Arial", 14, "bold"), fg="green")
                self.success_label.place(x=900, y=655)  # Adjust placement as needed

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to generate bill: {e}")

    def cust_detail(self):
        import customer
        customer.cust_win(Toplevel(self.root))

    def menu_detail(self):
        import menu
        menu.menu_win(Toplevel(self.root))

    def booking_detail(self):
        import booking
        booking.booking_win(Toplevel(self.root))

    def service_detail(self):
        import sevice
        sevice.service_win(Toplevel(self.root))

    def feedback_detail(self):
        import feedback
        feedback.feedback_win(Toplevel(self.root))

    def details_detail(self):
        import details
        details.details_win(Toplevel(self.root))

    def order_detail(self):
        order_win(Toplevel(self.root))

    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = order_win(root)
    root.mainloop()
