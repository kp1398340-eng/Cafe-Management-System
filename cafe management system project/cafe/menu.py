import importlib
from booking import booking_win
from sevice import service_win
from feedback import feedback_win
from details import details_win
from order import order_win
import tkinter as tk
from tkinter import RIDGE, Frame, Label, Button, Toplevel, messagebox, Listbox
from PIL import Image, ImageTk
import mysql.connector

class menu_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Menu - Food Cafe")
        self.root.geometry("1550x820")
        self.root.configure(bg="white")
        self.cart_items = []  # Store selected products

        # Database Connection
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="cafe_food")
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
        lbl_title = Label(self.root, text="cafe menu", font=("Bradley Hand ITC", 35, "bold"),
                          bg="#452711", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ================== Main Frame ==================
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


        # ================== Category Header ==================
        self.category_frame = Frame(self.root, bg="white", bd=2, relief="ridge")
        self.category_frame.place(x=240, y=200, width=1100, height=50)  

        # ================== Main Content Frame ==================
        self.main_frame = Frame(self.root, bg="white", bd=2, relief="ridge")
        self.main_frame.place(x=240, y=260, width=1090, height=400)

        # Canvas and Scrollbar for Main Content
        self.canvas = tk.Canvas(self.main_frame, bg="white")
        self.v_scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)

        self.scrollable_frame = Frame(self.canvas, bg="white")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        ))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.v_scrollbar.pack(side="right", fill="y")

        # Fetch Categories and Display Them
        self.fetch_categories()

    def fetch_categories(self):
        """ Fetch categories from the database and display them as buttons in category_frame """
        try:
            self.cursor.execute("SELECT id, name FROM categories")
            categories = self.cursor.fetchall()

            if not categories:
                Label(self.category_frame, text="No Categories Available", font=("Arial", 14)).pack()
                return

            for cat_id, cat_name in categories:
                cat_btn = Button(
                    self.category_frame, text=cat_name, font=("Arial", 12, "bold"),
                    bg="#987554", fg="white", bd=2, relief="ridge", padx=10, pady=5,
                    command=lambda id=cat_id: self.display_products(id)
                )
                cat_btn.pack(side="left", padx=5, pady=2)
        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch categories: {str(e)}")

    def display_products(self, category_id):
        """ Fetch and display products based on selected category """
        # Clear the previous products before displaying new ones
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        try:
            self.cursor.execute("SELECT id, name, price FROM products WHERE category_id=%s", (category_id,))
            products = self.cursor.fetchall()

            if not products:
                Label(self.scrollable_frame, text="No products available", font=("Arial", 12), fg="red").pack()
            else:
                for prod_id, name, price in products:
                    product_frame = Frame(self.scrollable_frame, bd=2, relief="ridge", padx=5, pady=5)
                    product_frame.pack(fill="x", padx=10, pady=5)

                    Label(product_frame, text=f"{name} - ₹{price}", font=("Arial", 12)).pack(side="left", padx=10)
                    Button(product_frame, text="Add to Cart", 
                           bg="#987554", fg="white").pack(side="right", padx=5)
        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch products: {str(e)}")

    def display_products(self, category_id):
        """ Fetch and display products based on selected category """
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        try:
            self.cursor.execute("SELECT id, name, price FROM products WHERE category_id=%s", (category_id,))
            products = self.cursor.fetchall()

            if not products:
                Label(self.scrollable_frame, text="No products available", font=("Arial", 12), fg="red").pack()
            else:
                for prod_id, name, price in products:
                    product_frame = Frame(self.scrollable_frame, bd=2, relief="ridge", padx=5, pady=5)
                    product_frame.pack(fill="x", padx=10, pady=5)

                    Label(product_frame, text=f"{name} - ₹{price}", font=("Arial", 12)).pack(side="left", padx=10)

                    # "Add to Cart" button now includes product_id
                    Button(product_frame, text="Add to Cart",
                        bg="#987554", fg="white",
                        command=lambda p_id=prod_id, n=name, p=price: self.add_to_cart(p_id, n, p)).pack(side="right", padx=5)

        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch products: {str(e)}")


        # Add a label for displaying success messages
        self.success_label = Label(self.root, text="", font=("Arial", 12, "bold"), fg="#452711", bg="white")
        self.success_label.place(x=250, y=660)  # Adjust position as needed


    def add_to_cart(self, product_id, name, price):
        """ Add selected product to the cart table in MySQL """
        try:
            quantity = 1  # Default quantity is 1
            total_price = price * quantity  # Calculate total price

            # Insert into the MySQL cart table
            self.cursor.execute(
                "INSERT INTO cart (customer_id, product_id, quantity, price, total_price) VALUES (%s, %s, %s, %s, %s)",
                (1, product_id, quantity, price, total_price)  # Replace '1' with actual customer_id if available
            )
            self.conn.commit()

            self.cart_items.append((product_id, name, price, quantity, total_price))

            # Show success message
            self.success_label.config(text=f"{name} added to cart!", fg="#452711")

            # Clear the message after a few seconds
            self.root.after(3000, lambda: self.success_label.config(text=""))

        except Exception as e:
            messagebox.showerror("Error", f"Could not add to cart: {str(e)}")




    def order_detail(self):
        """ Open Order Window and pass cart items """
        self.new_window = Toplevel(self.root)
        self.app = order_win(self.new_window, self.cart_items)  # Pass cart items


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


if __name__ == "__main__":
    root = tk.Tk()
    app = menu_win(root)
    root.mainloop()