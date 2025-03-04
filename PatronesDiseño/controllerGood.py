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

# 📌 Controlador (Maneja la lógica y la comunicación)
class OrderController:
    def __init__(self):
        self.orders = []

    def create_order(self, user, items):
        order = Order(user, items)
        self.orders.append(order)
        return order  # Devuelve la orden para la vista

    def process_order(self, order):
        order.calculate_total()
        return order.validate_order(), order.total  # Retorna los datos en lugar de imprimirlos

# 📌 Vista / Interfaz Gráfica (Interactúa con el usuario)
class OrderGUI:
    def __init__(self, root):
        self.controller = OrderController()
        self.root = root
        self.root.title("Sistema de Pedidos")

        # Entrada del usuario
        tk.Label(root, text="Nombre del Cliente:").grid(row=0, column=0)
        self.user_entry = tk.Entry(root)
        self.user_entry.grid(row=0, column=1)

        # Lista de productos
        self.items = [
            {"name": "Laptop", "price": 1000, "stock": 5},
            {"name": "Mouse", "price": 50, "stock": 3},
            {"name": "Teclado", "price": 80, "stock": 2}
        ]

        tk.Label(root, text="Producto:").grid(row=1, column=0)
        self.product_var = tk.StringVar()
        self.product_var.set(self.items[0]["name"])
        self.product_menu = tk.OptionMenu(root, self.product_var, *[item["name"] for item in self.items])
        self.product_menu.grid(row=1, column=1)

        tk.Label(root, text="Cantidad:").grid(row=2, column=0)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=2, column=1)

        # Botón para procesar pedido
        self.process_button = tk.Button(root, text="Realizar Pedido", command=self.process_order)
        self.process_button.grid(row=3, columnspan=2)

    # 📌 Método que maneja la interacción con la UI
    def process_order(self):
        user = self.user_entry.get()
        product_name = self.product_var.get()
        
        # Validar entrada de cantidad
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida.")
            return

        # Buscar producto seleccionado
        selected_item = next((item for item in self.items if item["name"] == product_name), None)
        if selected_item:
            order_items = [{"name": selected_item["name"], "price": selected_item["price"], "quantity": quantity, "stock": selected_item["stock"]}]
            
            # 📌 Se usa el Controller para manejar la orden
            order = self.controller.create_order(user, order_items)
            is_valid, total = self.controller.process_order(order)

            # 📌 La Vista solo muestra resultados, no maneja la lógica
            if is_valid:
                messagebox.showinfo("Pedido Confirmado", f"✅ Pedido confirmado para {user} por un total de ${total}")
            else:
                messagebox.showerror("Error", "❌ Pedido inválido: No hay suficiente stock.")
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

# 🚀 Ejecutar la GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = OrderGUI(root)
    root.mainloop()
