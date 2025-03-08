import tkinter as tk
from tkinter import messagebox

# 📌 Modelo (Lógica de Negocio)
class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
        self.total = 0
        self.is_valid = False

    def calculate_total(self):
        self.total = sum(item['price'] * item['quantity'] for item in self.items)
        return self.total

    def validate_order(self):
        self.is_valid = all(item['stock'] >= item['quantity'] for item in self.items)
        return self.is_valid

# ✅ GRASP Controller: Encapsula la lógica de negocio y coordina el procesamiento de la orden
class OrderController:
    def __init__(self, items):
        self.items = items

    def process_order(self, user, product_name, quantity):
        # Buscar el producto seleccionado
        selected_item = next((item for item in self.items if item["name"] == product_name), None)
        if not selected_item:
            return {"success": False, "message": "Producto no encontrado."}

        order = Order(user, [{
            "name": selected_item["name"],
            "price": selected_item["price"],
            "quantity": quantity,
            "stock": selected_item["stock"]
        }])
        order.calculate_total()
        if order.validate_order():
            return {"success": True, "message": f"✅ Pedido confirmado para {user} por un total de ${order.total}"}
        else:
            return {"success": False, "message": "❌ Pedido inválido: No hay suficiente stock."}

# Interfaz Gráfica (GUI)
class OrderGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Sistema de Pedidos")

        # Entrada del usuario
        tk.Label(root, text="Nombre del Cliente:").grid(row=0, column=0)
        self.user_entry = tk.Entry(root)
        self.user_entry.grid(row=0, column=1)

        # Lista de productos
        self.items = controller.items
        tk.Label(root, text="Producto:").grid(row=1, column=0)
        self.product_var = tk.StringVar()
        self.product_var.set(self.items[0]["name"])
        self.product_menu = tk.OptionMenu(root, self.product_var, *[item["name"] for item in self.items])
        self.product_menu.grid(row=1, column=1)

        tk.Label(root, text="Cantidad:").grid(row=2, column=0)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=2, column=1)

        # Botón para procesar el pedido
        self.process_button = tk.Button(root, text="Realizar Pedido", command=self.process_order)
        self.process_button.grid(row=3, columnspan=2)

    def process_order(self):
        user = self.user_entry.get()
        product_name = self.product_var.get()
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida.")
            return

        # Se delega la lógica de negocio al GRASP Controller
        result = self.controller.process_order(user, product_name, quantity)
        if result["success"]:
            messagebox.showinfo("Pedido Confirmado", result["message"])
        else:
            messagebox.showerror("Error", result["message"])

# 🚀 Ejecución de la aplicación con el GRASP Controller
if __name__ == "__main__":
    items = [
        {"name": "Laptop", "price": 1000, "stock": 5},
        {"name": "Mouse", "price": 50, "stock": 3},
        {"name": "Teclado", "price": 80, "stock": 2}
    ]
    
    controller = OrderController(items)
    root = tk.Tk()
    app = OrderGUI(root, controller)
    root.mainloop()
