import tkinter as tk
from tkinter import Toplevel, messagebox
import random
from category import Category_Win  
from product import pro_win

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard - Food Cafe")
        self.root.geometry("1800x900")  # Maximize Window Size
        self.root.configure(bg="#F8F9FA")

        # Sidebar
        self.sidebar = tk.Frame(self.root, bg="#343A40", width=290, height=900)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.title = tk.Label(self.sidebar, text="🍔 FOOD CAFE ", fg="white", bg="#343A40",
                              font=("Arial", 22, "bold"))
        self.title.pack(pady=20)

        self.create_sidebar_button("📊 Dashboard", "#007BFF")
        self.create_sidebar_button("📦 Categories", action=self.open_categories)
        self.create_sidebar_button("🛒 Products",action=self.open_product)
        self.create_sidebar_button("🔑 Logout", "#DC3545", action=self.logout)
        # Main Dashboard
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.header = tk.Label(self.main_frame, text="Admin Dashboard", font=("Arial", 28, "bold"), bg="white")
        self.header.pack(pady=10)

        self.create_dashboard_widgets()

        # Start Animation
        self.update_numbers()

    def open_categories(self):
        self.new_window = Toplevel(self.root)
        self.app=Category_Win(self.new_window)

    def open_product(self):
        self.new_window = Toplevel(self.root)
        self.app=pro_win(self.new_window)

    def create_sidebar_button(self, text, bg_color="#495057", action=None):
        """Create sidebar navigation buttons with optional actions."""
        btn = tk.Button(self.sidebar, text=text, bg=bg_color, fg="white",
                        font=("Arial", 16), bd=0, padx=20, pady=12, anchor="w",
                        command=action)
        btn.pack(fill=tk.X, pady=5)

    def logout(self):
        """Display a confirmation message before logging out."""
        response = messagebox.askyesno("Logout", "Are you sure you want to log out?")
        if response:
            self.root.destroy()  # Close the application

    def create_dashboard_widgets(self):
        """Create a single-row dashboard with 4 large widgets."""
        self.stats = [
            ("  New Orders  ", 150, "#17A2B8"),
            ("  Bounce Rate  ", 53, "#28A745"),
            (" User Registrations ", 44, "#FFC107"),
            (" Unique Visitors ", 65, "#DC3545"),
        ]

        self.dashboard_frame = tk.Frame(self.main_frame, bg="white")
        self.dashboard_frame.pack(pady=20)

        self.stat_labels = []  # Store label references for animation

        for idx, (label, value, color) in enumerate(self.stats):
            frame = tk.Frame(self.dashboard_frame, bg=color, width=400, height=180, bd=7, relief="ridge")
            frame.grid(row=0, column=idx, padx=20, pady=10)  # Ensure 4 in a row with spacing

            lbl_value = tk.Label(frame, text=value, fg="white", bg=color, font=("Arial", 50, "bold"))
            lbl_value.pack(pady=20)

            lbl_text = tk.Label(frame, text=label, fg="white", bg=color, font=("Arial", 22, "bold"))
            lbl_text.pack()

            self.stat_labels.append((lbl_value, value))  # Store reference for updating

    def update_numbers(self):
        """Animate number changes smoothly."""
        for i, (lbl, old_value) in enumerate(self.stat_labels):
            new_value = random.randint(old_value - 10, old_value + 10)  # Generate random change
            self.animate_number(lbl, old_value, new_value, 0)

        self.root.after(5000, self.update_numbers)  # Repeat every 5 seconds

    def animate_number(self, label, start, end, step):
        """Recursive function for smooth number change."""
        if start < end:
            start += 1
        elif start > end:
            start -= 1
        else:
            return

        label.config(text=str(start))
        self.root.after(30, lambda: self.animate_number(label, start, end, step + 1))  # Faster smooth effect

# Run Tkinter App
if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()
