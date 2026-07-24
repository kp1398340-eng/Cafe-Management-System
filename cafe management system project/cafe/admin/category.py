import tkinter as tk
from tkinter import Toplevel, messagebox, ttk
import mysql.connector 


class Category_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard - Food Cafe")
        self.root.geometry("1550x800")
        self.root.configure(bg="#F8F9FA")

        # Database Connection
        self.conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="cafe_food"
        )
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

        # Main Frame
        self.main_frame = tk.Frame(self.root, bg="white", width=950, height=700)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Header Label
        self.header = tk.Label(self.main_frame, text="CATEGORIES", font=("Arial", 30, "bold"), bg="white")
        self.header.pack(pady=10)

        # Content Frames
        self.form_frame = tk.LabelFrame(self.main_frame, text=" Add Category ", font=("Arial", 12, "bold"), bd=4, relief=tk.RIDGE, padx=10, pady=10)
        self.form_frame.place(x=20, y=70, width=420, height=250)

        # Category Form
        tk.Label(self.form_frame, text="Category Name:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=55, pady=5)
        self.category_name = tk.Entry(self.form_frame, font=("Arial", 10))
        self.category_name.grid(row=1, column=0, padx=5, pady=5)

        # Buttons centered, one per line
        self.add_button = tk.Button(self.form_frame, text="Add", font=("Arial", 10, "bold"), bg="green", fg="white", width=20, command=self.add_category)
        self.add_button.grid(row=2, column=0, pady=20 )

        self.update_button = tk.Button(self.form_frame, text="Update", font=("Arial", 10, "bold"), bg="blue", fg="white", width=20, command=self.update_category)
        self.update_button.grid(row=2, column=1, pady=20)

        self.delete_button = tk.Button(self.form_frame, text="Delete", font=("Arial", 10, "bold"), bg="red", fg="white", width=20, command=self.delete_category)
        self.delete_button.grid(row=4, column=0, pady=5)

        self.reset_button = tk.Button(self.form_frame, text="Reset", font=("Arial", 10, "bold"), bg="gray", fg="white", width=20, command=self.reset_form)
        self.reset_button.grid(row=4, column=1, pady=5)

        # Table Frame
        self.table_frame = tk.Frame(self.main_frame, bd=4, relief=tk.RIDGE, bg="white")
        self.table_frame.place(x=450, y=70, width=680, height=600)

        # Scrollbars
        self.scroll_x = tk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL)
        self.scroll_y = tk.Scrollbar(self.table_frame, orient=tk.VERTICAL)

        # Treeview Table
        self.category_table = ttk.Treeview(
            self.table_frame, 
            columns=("ID", "Name"), 
            xscrollcommand=self.scroll_x.set, 
            yscrollcommand=self.scroll_y.set
        )

        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scroll_x.config(command=self.category_table.xview)
        self.scroll_y.config(command=self.category_table.yview)

        # Define Table Headings
        self.category_table.heading("ID", text="ID")
        self.category_table.heading("Name", text="Category Name")
        self.category_table["show"] = "headings"

        # Set Column Widths
        self.category_table.column("ID", width=80)
        self.category_table.column("Name", width=200)

        self.category_table.pack(fill=tk.BOTH, expand=True)

        # Fetch Categories
        self.fetch_categories()

    def open_categories(self):
        from category import Category_Win 
        self.new_window = Toplevel(self.root)
        self.app=Category_Win(self.new_window)

    def open_product(self):
        from product import pro_win
        self.new_window = Toplevel(self.root)
        self.app=pro_win(self.new_window)

    def fetch_categories(self):
        self.category_table.delete(*self.category_table.get_children())
        self.cursor.execute("SELECT id, name FROM categories")
        rows = self.cursor.fetchall()
        if rows:
            for row in rows:
                self.category_table.insert("", tk.END, values=row)

    def add_category(self):
        category_name = self.category_name.get()

        if not category_name:
            messagebox.showerror("Error", "Category Name is required!")
            return
        
        self.cursor.execute("INSERT INTO categories (name) VALUES (%s)", (category_name,))
        self.conn.commit()
        self.fetch_categories()
        self.reset_form()
        messagebox.showinfo("Success", "Category added successfully!")

    def update_category(self):
        selected_item = self.category_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a category to update!")
            return
        
        category_id = self.category_table.item(selected_item)['values'][0]
        category_name = self.category_name.get()

        self.cursor.execute("UPDATE categories SET name=%s WHERE id=%s", (category_name, category_id))
        self.conn.commit()
        self.fetch_categories()
        messagebox.showinfo("Success", "Category updated successfully!")

    def delete_category(self):
        selected_item = self.category_table.selection()
        if selected_item:
            category_id = self.category_table.item(selected_item)['values'][0]
            self.cursor.execute("DELETE FROM categories WHERE id=%s", (category_id,))
            self.conn.commit()
            self.fetch_categories()
            messagebox.showinfo("Success", "Category deleted successfully!")

    def reset_form(self):
        self.category_name.delete(0, tk.END)

    def create_sidebar_button(self, text, bg_color="#495057", command=None):
        btn = tk.Button(self.sidebar, text=text, bg=bg_color, fg="white", font=("Arial", 16), bd=0, padx=20, pady=12, anchor="w", command=command)
        btn.pack(fill=tk.X, pady=5)

    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to log out?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Category_Win(root)
    root.mainloop()
