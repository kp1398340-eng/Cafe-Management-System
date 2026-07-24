import tkinter as tk
from tkinter import Toplevel, messagebox, ttk
import mysql.connector

class pro_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard - Food Cafe")
        self.root.geometry("1550x800")
        self.root.configure(bg="#F8F9FA")

        # Database Connection
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="cafe_food")
        self.cursor = self.conn.cursor()

        # Sidebar
        self.sidebar = tk.Frame(self.root, bg="#343A40", width=250, height=700)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.title = tk.Label(self.sidebar, text="🍔 FOOD CAFE ", fg="white", bg="#343A40", font=("Arial", 22, "bold"))
        self.title.pack(pady=20)

        self.create_sidebar_button("📊 Dashboard", "#007BFF")
        self.create_sidebar_button("📦 Categories", command=self.open_categories)
        self.create_sidebar_button("🛒 Products", command=self.open_product)
        self.create_sidebar_button("🔑 Logout", "#DC3545", command=self.logout)

        # Product Management UI
        self.header = tk.Label(self.root, text="Manage Products", font=("Arial", 24, "bold"), bg="#F8F9FA")
        self.header.pack(pady=10)

        # Form Frame
        self.form_frame = tk.LabelFrame(self.root, text="Add/Edit Product", font=("Arial", 12, "bold"), bd=4, relief=tk.RIDGE)
        self.form_frame.place(x=240, y=70, width=400, height=350)

        tk.Label(self.form_frame, text="Product Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.product_name = tk.Entry(self.form_frame, width=30)
        self.product_name.grid(row=1, column=0, padx=10, pady=5)

        tk.Label(self.form_frame, text="Price:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.product_price = tk.Entry(self.form_frame, width=30)
        self.product_price.grid(row=3, column=0, padx=10, pady=5)

        tk.Label(self.form_frame, text="Category:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(self.form_frame, textvariable=self.category_var, state="readonly", width=28)
        self.category_dropdown.grid(row=5, column=0, padx=10, pady=5)

        self.add_button = tk.Button(self.form_frame, text="Add", font=("Arial", 10, "bold"), bg="green", fg="white", width=20, command=self.add_product)
        self.add_button.grid(row=6, column=0, pady=5)

        self.update_button = tk.Button(self.form_frame, text="Update", font=("Arial", 10, "bold"), bg="blue", fg="white", width=20, command=self.update_product)
        self.update_button.grid(row=6, column=1, pady=5)

        self.delete_button = tk.Button(self.form_frame, text="Delete", font=("Arial", 10, "bold"), bg="red", fg="white", width=20, command=self.delete_product)
        self.delete_button.grid(row=7, column=0, pady=5)

        self.reset_button = tk.Button(self.form_frame, text="Reset", font=("Arial", 10, "bold"), bg="gray", fg="white", width=20, command=self.reset_form)
        self.reset_button.grid(row=7, column=1, pady=5)

        # Table Frame
        self.table_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="white")
        self.table_frame.place(x=650, y=70, width=700, height=610)

        self.scroll_x = tk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL)
        self.scroll_y = tk.Scrollbar(self.table_frame, orient=tk.VERTICAL)

        self.product_table = ttk.Treeview(
            self.table_frame, columns=("ID", "Name", "Price", "Category"),
            xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set
        )

        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scroll_x.config(command=self.product_table.xview)
        self.scroll_y.config(command=self.product_table.yview)

        self.product_table.heading("ID", text="ID")
        self.product_table.heading("Name", text="Product Name")
        self.product_table.heading("Price", text="Price")
        self.product_table.heading("Category", text="Category")
        self.product_table["show"] = "headings"

        self.product_table.column("ID", width=50)
        self.product_table.column("Name", width=200)
        self.product_table.column("Price", width=100)
        self.product_table.column("Category", width=150)
        self.product_table.pack(fill=tk.BOTH, expand=True)

        self.product_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_categories()
        self.fetch_products()

    def add_product(self):
        name = self.product_name.get()
        price = self.product_price.get()
        category = self.category_var.get()

        if not name or not price or not category:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            self.cursor.execute("INSERT INTO products (name, price, category_id) VALUES (%s, %s, (SELECT id FROM categories WHERE name=%s))",
                                (name, price, category))
            self.conn.commit()
            messagebox.showinfo("Success", "Product added successfully")
            self.fetch_products()
            self.reset_form()
        except Exception as e:
            messagebox.showerror("Error", f"Error adding product: {str(e)}")

    def get_cursor(self, event):
        selected = self.product_table.focus()
        values = self.product_table.item(selected, "values")
        if values:
            self.product_name.delete(0, tk.END)
            self.product_price.delete(0, tk.END)
            self.category_var.set("")

            self.product_name.insert(tk.END, values[1])
            price_without_symbol = values[2].replace("₹", "")  # Remove ₹ for editing
            self.product_price.insert(tk.END, price_without_symbol)
            self.category_var.set(values[3])


    def fetch_categories(self):
        self.cursor.execute("SELECT name FROM categories")
        categories = self.cursor.fetchall()
        category_list = [category[0] for category in categories]
        self.category_dropdown["values"] = category_list

    def fetch_products(self):
        self.product_table.delete(*self.product_table.get_children())  # Clear existing data
        self.cursor.execute("""
            SELECT p.id, p.name, p.price, c.name 
            FROM products p 
            JOIN categories c ON p.category_id = c.id
        """)
        products = self.cursor.fetchall()
        
        for product in products:
            self.product_table.insert("", "end", values=product)



    def update_product(self):
        selected = self.product_table.focus()
        values = self.product_table.item(selected, "values")
        if not values:
            messagebox.showerror("Error", "No product selected!")
            return

        product_id = values[0]
        name = self.product_name.get()
        price = self.product_price.get()
        category = self.category_var.get()

        if not name or not price or not category:
            messagebox.showerror("Error", "All fields are required")
            return

        self.cursor.execute("UPDATE products SET name=%s, price=%s, category_id=(SELECT id FROM categories WHERE name=%s) WHERE id=%s", (name, price, category, product_id))
        self.conn.commit()
        self.fetch_products()
        self.reset_form()

    def delete_product(self):
        selected = self.product_table.focus()
        values = self.product_table.item(selected, "values")
        if not values:
            messagebox.showerror("Error", "No product selected!")
            return

        product_id = values[0]
        self.cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
        self.conn.commit()
        self.fetch_products()
        self.reset_form()

    def reset_form(self):
        self.product_name.delete(0, tk.END)
        self.product_price.delete(0, tk.END)
        self.category_var.set("")

    def create_sidebar_button(self, text, bg_color="#495057", command=None):
        btn = tk.Button(self.sidebar, text=text, bg=bg_color, fg="white", font=("Arial", 16), bd=0, padx=20, pady=12, anchor="w", command=command)
        btn.pack(fill=tk.X, pady=5)

    def open_categories(self):
        from category import Category_Win 
        self.new_window = Toplevel(self.root)
        self.app=Category_Win(self.new_window)

    def open_product(self):
        from product import pro_win
        self.new_window = Toplevel(self.root)
        self.app=pro_win(self.new_window)

    def logout(self):
        self.root.destroy()  # This will close the application

if __name__ == "__main__":
    root = tk.Tk()
    app = pro_win(root)
    root.mainloop()
