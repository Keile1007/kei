import tkinter as tk
from tkinter import messagebox

class Product:
    def __init__(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Date: {self.date}"

class GroceryAssistant:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        messagebox.showinfo("Success", "Product added successfully!")

    def view_products(self):
        if not self.products:
            messagebox.showinfo("Info", "No products available.")
        else:
            product_list = "\n".join(str(product) for product in self.products)
            messagebox.showinfo("Product List", product_list)

    def delete_product(self, name):
        initial_count = len(self.products)
        self.products = [product for product in self.products if product.name != name]
        if len(self.products) < initial_count:
            messagebox.showinfo("Success", "Product deleted successfully!")
        else:
            messagebox.showinfo("Error", "Product not found.")

def main():
    def add_product_gui():
        name = entry_name.get()
        try:
            price = float(entry_price.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid price.")
            return
        date = entry_date.get()

        if name and date:
            product = Product(name, price, date)
            assistant.add_product(product)
            entry_name.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            entry_date.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid input", "Please fill in all fields.")

    def view_products_gui():
        assistant.view_products()

    def delete_product_gui():
        name = entry_delete_name.get()
        if name:
            assistant.delete_product(name)
            entry_delete_name.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid input", "Please enter a product name to delete.")

    assistant = GroceryAssistant()

    # Create main window
    root = tk.Tk()
    root.title("GreenGrocer")

    # Add Product section
    tk.Label(root, text="Enter Product Name:").pack(pady=5)
    entry_name = tk.Entry(root, width=40)
    entry_name.pack(pady=5)

    tk.Label(root, text="Enter Product Price:").pack(pady=5)
    entry_price = tk.Entry(root, width=40)
    entry_price.pack(pady=5)

    tk.Label(root, text="Enter Product Date (YYYY-MM-DD):").pack(pady=5)
    entry_date = tk.Entry(root, width=40)
    entry_date.pack(pady=5)

    # Buttons for adding, viewing, and deleting products
    tk.Button(root, text="Add Product", width=40, command=add_product_gui).pack(pady=10)
    tk.Button(root, text="View Products", width=40, command=view_products_gui).pack(pady=10)

    # Delete Product section
    tk.Label(root, text="Enter Product Name to Delete:").pack(pady=5)
    entry_delete_name = tk.Entry(root, width=40)
    entry_delete_name.pack(pady=5)

    tk.Button(root, text="Delete Product", width=40, command=delete_product_gui).pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
