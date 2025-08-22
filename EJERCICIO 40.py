# EJERCICIO 40
título = "EJERCICIO 40 :)"
print("-" * len(título) + "\n" + título + "\n" + "-" * len(título))


class Factura:
    def __init__(self, productos, descuento):
        self.productos = productos
        
        if descuento < 0:
            self.descuento = 0
        elif descuento > 100:
            self.descuento = 100
        else:
            self.descuento = descuento

    def subtotal(self):
        total = 0
        for descripcion, precio in self.productos:
            total += precio
        return total

    def total(self):
        subtotal = self.subtotal()
        return subtotal * (1 - self.descuento / 100)
    

class FacturaConImpuesto(Factura):
    def __init__(self, productos, descuento, iva):
        super().__init__(productos, descuento)
        self.iva = iva

    def total(self):
        total = super().total()
        return total + total * self.iva / 100    #Iva * 100 es el porcentaje de IVA
    
    
    
    
#prueba

print("Ejemplos de facturas:")

# Creamos algunos productos (tuplas con descripción y precio)
productos = [
    ("Camiseta", 25.50),
    ("Sopitas magui", 15.00),
    ("Playera", 80.00)
]

# Creamos una factura normal con 10% de descuento
mi_factura = Factura(productos, 10)

print("Productos en la factura")
for descripcion, precio in productos:
    print(f"- {descripcion}: Q{precio}")

print(f"\nSubtotal: Q{mi_factura.subtotal()}")
print(f"Descuento aplicado: {mi_factura.descuento}%")
print(f"Total a pagar: Q{mi_factura.total():.2f}")

print("\n" + "-"*40) 
print("factura dcon impuesto:")

# Creamos una factura con impuesto (IVA 12%)
mi_factura_con_iva = FacturaConImpuesto(productos, 15, 12)

print("Ítems en la factura:")
for descripcion, precio in productos:
    print(f"- {descripcion}: Q{precio}")

print(f"\nSubtotal: Q{mi_factura_con_iva.subtotal()}")
print(f"Descuento aplicado: {mi_factura_con_iva.descuento}%")
print(f"IVA aplicado: {mi_factura_con_iva.iva}%")
print(f"Total a pagar: Q{mi_factura_con_iva.total():.2f}")

print("\n" + "-"*40)

print("Probando un descuento no valido")
factura_error = Factura([("Libro", 20.00)], 150)  # <<<<<usando descuento mayor a 100% (150%)
print(f"Descuento ingresado: 150%")
print(f"Descuento aplicado: {factura_error.descuento}% (se ajustó a 100%)")
print(f"Total a pagar: Q{factura_error.total():.2f}")  # Ahora el producto es gratis por ser el descuento más cercano a 150 :D
    