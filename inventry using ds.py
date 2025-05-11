import tkinter as tk
from tkinter import messagebox, ttk
from typing import Dict, List, Optional

class Product:
    """Base class for all products"""
    def __init__(self, name: str, brand: str, price: float, quantity: int):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
    
    def get_details(self) -> Dict:
        """Return product details as a dictionary"""
        return {
            "Name": self.name,
            "Brand": self.brand,
            "Price": f"${self.price:.2f}",
            "Quantity": self.quantity
        }
    
    def sell(self, quantity: int) -> bool:
        """Sell specified quantity of product"""
        if quantity <= 0:
            return False
        if self.quantity >= quantity:
            self.quantity -= quantity
            return True
        return False

class Pendrive(Product):
    """Pendrive product with size attribute"""
    def __init__(self, name: str, brand: str, price: float, quantity: int, size: str):
        super().__init__(name, brand, price, quantity)
        self.size = size  # e.g., "16GB", "32GB", etc.
    
    def get_details(self) -> Dict:
        details = super().get_details()
        details["Size"] = self.size
        return details

class Ringlight(Product):
    """Ringlight product with color temperature attribute"""
    def __init__(self, name: str, brand: str, price: float, quantity: int, color_temp: str):
        super().__init__(name, brand, price, quantity)
        self.color_temp = color_temp  # e.g., "3000K-6000K"
    
    def get_details(self) -> Dict:
        details = super().get_details()
        details["Color Temperature"] = self.color_temp
        return details

class Tripod(Product):
    """Tripod product with max height attribute"""
    def __init__(self, name: str, brand: str, price: float, quantity: int, max_height: str):
        super().__init__(name, brand, price, quantity)
        self.max_height = max_height  # e.g., "60 inches"
    
    def get_details(self) -> Dict:
        details = super().get_details()
        details["Max Height"] = self.max_height
        return details

class Stabilizer(Product):
    """Stabilizer product with compatible devices attribute"""
    def __init__(self, name: str, brand: str, price: float, quantity: int, compatible: str):
        super().__init__(name, brand, price, quantity)
        self.compatible = compatible  # e.g., "Smartphones, DSLRs"
    
    def get_details(self) -> Dict:
        details = super().get_details()
        details["Compatible Devices"] = self.compatible
        return details

class Standie(Product):
    """Standie product with material attribute"""
    def __init__(self, name: str, brand: str, price: float, quantity: int, material: str):
        super().__init__(name, brand, price, quantity)
        self.material = material  # e.g., "Plastic", "Metal"
    
    def get_details(self) -> Dict:
        details = super().get_details()
        details["Material"] = self.material
        return details

class InventorySystem:
    """Inventory management system"""
    def __init__(self):
        self.products: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> bool:
        """Add a product to inventory"""
        if product.name in self.products:
            return False  # Product already exists
        self.products[product.name] = product
        return True
    
    def sell_product(self, product_name: str, quantity: int) -> bool:
        """Sell a product"""
        if product_name not in self.products:
            return False  # Product not found
        return self.products[product_name].sell(quantity)
    
    def get_inventory(self) -> List[Dict]:
        """Get inventory details"""
        return [product.get_details() for product in self.products.values()]

class InventoryApp:
    """GUI application for inventory management"""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Gadget Store Inventory System")
        self.inventory = InventorySystem()
        
        # Create tabs
        self.tab_control = ttk.Notebook(root)
        
        # Add Product Tab
        self.add_product_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.add_product_tab, text="Add Product")
        self.setup_add_product_tab()
        
        # Sell Product Tab
        self.sell_product_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.sell_product_tab, text="Sell Product")
        self.setup_sell_product_tab()
        
        # View Inventory Tab
        self.view_inventory_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.view_inventory_tab, text="View Inventory")
        self.setup_view_inventory_tab()
        
        self.tab_control.pack(expand=1, fill="both")
        
        # Add some sample products
        self.add_sample_products()
        self.update_product_dropdown()  # Initialize the dropdown
    
    def add_sample_products(self):
        """Add some sample products for demonstration"""
        sample_products = [
            Pendrive("Ultra Flash Drive", "SanDisk", 12.99, 50, "64GB"),
            Ringlight("Pro Ring Light", "Neewer", 49.99, 20, "3000K-6000K"),
            Tripod("Compact Tripod", "Amazon Basics", 24.99, 30, "60 inches"),
            Stabilizer("Smartphone Gimbal", "DJI", 99.99, 15, "Smartphones"),
            Standie("Phone Stand", "Lamicall", 9.99, 40, "Aluminum")
        ]
        
        for product in sample_products:
            self.inventory.add_product(product)
    
    def setup_add_product_tab(self):
        """Setup the Add Product tab"""
        # Product Type Selection
        tk.Label(self.add_product_tab, text="Product Type:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.product_type_var = tk.StringVar()
        self.product_type_var.set("Pendrive")
        product_types = ["Pendrive", "Ringlight", "Tripod", "Stabilizer", "Standie"]
        tk.OptionMenu(self.add_product_tab, self.product_type_var, *product_types).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Common Fields
        tk.Label(self.add_product_tab, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.add_product_tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.add_product_tab, text="Brand:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.brand_entry = tk.Entry(self.add_product_tab)
        self.brand_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.add_product_tab, text="Price:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.price_entry = tk.Entry(self.add_product_tab)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.add_product_tab, text="Quantity:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.quantity_entry = tk.Entry(self.add_product_tab)
        self.quantity_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Type-specific Field
        tk.Label(self.add_product_tab, text="Special Attribute:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.special_attr_entry = tk.Entry(self.add_product_tab)
        self.special_attr_entry.grid(row=5, column=1, padx=5, pady=5)
        self.update_special_attr_label()
        
        # Bind product type change to update label
        self.product_type_var.trace("w", lambda *args: self.update_special_attr_label())
        
        # Add Button
        tk.Button(self.add_product_tab, text="Add Product", command=self.add_product).grid(row=6, column=0, columnspan=2, pady=10)
    
    def update_special_attr_label(self):
        """Update the special attribute label based on product type"""
        product_type = self.product_type_var.get()
        if product_type == "Pendrive":
            tk.Label(self.add_product_tab, text="Size (e.g., 16GB):").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        elif product_type == "Ringlight":
            tk.Label(self.add_product_tab, text="Color Temp (e.g., 3000K-6000K):").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        elif product_type == "Tripod":
            tk.Label(self.add_product_tab, text="Max Height (e.g., 60 inches):").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        elif product_type == "Stabilizer":
            tk.Label(self.add_product_tab, text="Compatible Devices:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        elif product_type == "Standie":
            tk.Label(self.add_product_tab, text="Material:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    
    def add_product(self):
        """Add a new product to inventory"""
        try:
            name = self.name_entry.get().strip()
            brand = self.brand_entry.get().strip()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
            special_attr = self.special_attr_entry.get().strip()
            
            if not name or not brand or not special_attr:
                raise ValueError("All fields must be filled")
            if price <= 0 or quantity <= 0:
                raise ValueError("Price and quantity must be positive numbers")
            
            product_type = self.product_type_var.get()
            product = None
            
            if product_type == "Pendrive":
                product = Pendrive(name, brand, price, quantity, special_attr)
            elif product_type == "Ringlight":
                product = Ringlight(name, brand, price, quantity, special_attr)
            elif product_type == "Tripod":
                product = Tripod(name, brand, price, quantity, special_attr)
            elif product_type == "Stabilizer":
                product = Stabilizer(name, brand, price, quantity, special_attr)
            elif product_type == "Standie":
                product = Standie(name, brand, price, quantity, special_attr)
            
            if self.inventory.add_product(product):
                messagebox.showinfo("Success", f"{product_type} '{name}' added to inventory!")
                self.clear_add_product_fields()
                self.update_product_dropdown()  # Update the dropdown after adding
                self.refresh_inventory_view()  # Also refresh the inventory view
            else:
                messagebox.showerror("Error", f"A product with name '{name}' already exists!")
        
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    
    def clear_add_product_fields(self):
        """Clear all fields in the Add Product tab"""
        self.name_entry.delete(0, tk.END)
        self.brand_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.special_attr_entry.delete(0, tk.END)
    
    def setup_sell_product_tab(self):
        """Setup the Sell Product tab"""
        # Product Selection
        tk.Label(self.sell_product_tab, text="Product:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.product_var = tk.StringVar()
        self.product_dropdown = ttk.Combobox(self.sell_product_tab, textvariable=self.product_var, state="readonly")
        self.product_dropdown.grid(row=0, column=1, padx=5, pady=5)
        self.update_product_dropdown()
        
        # Quantity
        tk.Label(self.sell_product_tab, text="Quantity:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.sell_quantity_entry = tk.Entry(self.sell_product_tab)
        self.sell_quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Sell Button
        tk.Button(self.sell_product_tab, text="Sell Product", command=self.sell_product).grid(row=2, column=0, columnspan=2, pady=10)
    
    def update_product_dropdown(self):
        """Update the product dropdown with current inventory"""
        products = [product.name for product in self.inventory.products.values()]
        self.product_dropdown['values'] = products
        if products:
            self.product_var.set(products[0])
        else:
            self.product_var.set('')
    
    def sell_product(self):
        """Sell a product"""
        try:
            product_name = self.product_var.get()
            if not product_name:
                raise ValueError("No product selected")
            
            quantity = int(self.sell_quantity_entry.get())
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number")
            
            if self.inventory.sell_product(product_name, quantity):
                messagebox.showinfo("Success", f"Successfully sold {quantity} of {product_name}")
                self.sell_quantity_entry.delete(0, tk.END)
                self.update_product_dropdown()  # Refresh dropdown
                self.refresh_inventory_view()  # Refresh inventory view
            else:
                available = self.inventory.products[product_name].quantity
                messagebox.showerror("Error", f"Insufficient stock! Only {available} available.")
        
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    
    def setup_view_inventory_tab(self):
        """Setup the View Inventory tab"""
        # Treeview for displaying inventory
        self.inventory_tree = ttk.Treeview(self.view_inventory_tab, columns=("Brand", "Price", "Quantity", "Details"), show="headings")
        self.inventory_tree.heading("Brand", text="Brand")
        self.inventory_tree.heading("Price", text="Price")
        self.inventory_tree.heading("Quantity", text="Quantity")
        self.inventory_tree.heading("Details", text="Details")
        self.inventory_tree.column("Brand", width=100)
        self.inventory_tree.column("Price", width=80)
        self.inventory_tree.column("Quantity", width=80)
        self.inventory_tree.column("Details", width=200)
        self.inventory_tree.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Refresh Button
        tk.Button(self.view_inventory_tab, text="Refresh Inventory", command=self.refresh_inventory_view).pack(pady=10)
        
        # Initial refresh
        self.refresh_inventory_view()
    
    def refresh_inventory_view(self):
        """Refresh the inventory view"""
        # Clear current view
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)
        
        # Add all products
        for product in self.inventory.products.values():
            details = product.get_details()
            details_str = ", ".join(f"{k}: {v}" for k, v in details.items() if k not in ["Name", "Brand", "Price", "Quantity"])
            self.inventory_tree.insert("", "end", values=(details["Brand"], details["Price"], details["Quantity"], details_str), text=details["Name"])

def main():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
