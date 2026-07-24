import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import json
import os

# File for storing categories
DATA_FILE = "categories.json"

# Load categories from JSON
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        categories = json.load(file)
else:
    categories = []

def save_categories():
    with open(DATA_FILE, "w") as file:
        json.dump(categories, file, indent=4)

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for category in categories:
        img = Image.open(category["image"]).resize((50, 50))
        img = ImageTk.PhotoImage(img)
        image_refs.append(img)  # Store reference to avoid garbage collection
        tree.insert("", "end", values=(category["id"], category["name"], category["description"]), image=img)

def add_category():
    name = name_entry.get().strip()
    desc = desc_entry.get("1.0", tk.END).strip()
    img_path = image_path.get()
    if not name or not img_path:
        messagebox.showerror("Error", "Category name and image are required")
        return
    
    new_id = max([c["id"] for c in categories], default=0) + 1
    categories.append({"id": new_id, "name": name, "description": desc, "image": img_path})
    save_categories()
    refresh_table()
    name_entry.delete(0, tk.END)
    desc_entry.delete("1.0", tk.END)
    image_path.set("")
    messagebox.showinfo("Success", "Category added successfully!")

def delete_category():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a category to delete.")
        return
    item = tree.item(selected_item)
    category_id = item["values"][0]
    global categories
    categories = [c for c in categories if c["id"] != category_id]
    save_categories()
    refresh_table()
    messagebox.showinfo("Success", "Category deleted successfully!")

def upload_image():
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filename:
        image_path.set(filename)

# Main Window
root = tk.Tk()
root.title("Category Management")
root.geometry("900x500")
root.configure(bg="white")

# Sidebar
sidebar = tk.Frame(root, bg="#343a40", width=200, height=500)
sidebar.pack(side="left", fill="y")

# Sidebar Labels & Buttons
tk.Label(sidebar, text="FOOD_CAFE", fg="white", bg="#343a40", font=("Arial", 14, "bold")).pack(pady=15)
for btn_text in ["Dashboard", "Categories", "Products", "Settings"]:
    tk.Button(sidebar, text=btn_text, fg="white", bg="#495057", padx=20, pady=5, relief="flat").pack(fill="x", pady=2)

# Main Content Frame
main_frame = tk.Frame(root, bg="white", padx=20, pady=20)
main_frame.pack(side="right", expand=True, fill="both")

tk.Label(main_frame, text="Categories", font=("Arial", 16, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

# Input Fields
name_entry = tk.Entry(main_frame, width=30)
desc_entry = tk.Text(main_frame, height=3, width=30)
image_path = tk.StringVar()

tk.Label(main_frame, text="Category Name:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(main_frame, text="Description:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky="w")
desc_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(main_frame, text="Upload Image", command=upload_image, bg="#007bff", fg="white", padx=10).grid(row=3, column=0, pady=5)
tk.Entry(main_frame, textvariable=image_path, width=30).grid(row=3, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(main_frame, bg="white")
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Add", command=add_category, bg="#28a745", fg="white", padx=10).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Delete", command=delete_category, bg="#dc3545", fg="white", padx=10).grid(row=0, column=1, padx=5)

# Table (Treeview)
image_refs = []
table_frame = tk.Frame(main_frame)
table_frame.grid(row=5, column=0, columnspan=2, pady=10)
columns = ("ID", "Category Name", "Description")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
tree.heading("ID", text="ID")
tree.heading("Category Name", text="Category Name")
tree.heading("Description", text="Description")
tree.pack()

refresh_table()
root.mainloop()
