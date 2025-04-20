class ShoppingCart:
    def __init__(self, payment_gateway=None):
        self.items = {}
        self.discount = 0  # variable descuento
        self.payment_gateway = payment_gateway

    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity  # si esta en el carrito, agrega la cantidad
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}  # si no esta, lo agrega
    
    def remove_item(self, name):
        if name in self.items:  # busca el item en el carrito
            del self.items[name]  # elimina el item

    def calculate_total(self):
        total = sum(item["quantity"] * item["unit_price"] for item in self.items.values())
        if self.discount > 0:  # si hay descuento
            total *= (1 - self.discount / 100)  # aplica descuento
        return round(total, 2)  # redondeo a 2 decimales

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:  # si el descuento es valido
            self.discount = discount_percentage
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")

    def process_payment(self, amount):
        if not self.payment_gateway:  # si no hay objeto payment_gateway
            raise ValueError("No payment gateway provided.")
        try:
            success = self.payment_gateway.process_payment(amount)  # verifica el pago, aceptandolo
            return success
        except Exception as e:
            # Manejar excepciones según sea necesario
            raise e
