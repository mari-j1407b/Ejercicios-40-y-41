# EJERCICO 41
título = "EJERCICIO 41 :)"
print("-" * len(título) + "\n" + título + "\n" + "-" * len(título))

class Empleado:
    def __init__(self, nombre, salario_base, pago_hora_extra):
        self.nombre = nombre
        self.salario_base = salario_base
        self.pago_por_hora_etra = pago_hora_extra  
    
    def calcular_pago(self, numero_horas_extra):
        
        if numero_horas_extra < 0:     # horas extra no  deben ser negativas
            numero_horas_extra = 0
        #     v<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Esto es para el pago total mensual
        #     v
        pago_horas_etra = numero_horas_extra * self.pago_por_hora_etra  
        pago_total_mensual = self.salario_base + pago_horas_etra
        return pago_total_mensual


class EmpleadoComision(Empleado):
    def __init__(self, nombre, salario_base, pago_hora_extra, porcentaje_comision):
        # Se llama siempre al constructor de la clase padre
        super().__init__(nombre, salario_base, pago_hora_extra)
        self.porcentaje_comsion = porcentaje_comision 
    
    def calcular_pago(self, numero_horas_extra, monto_ventas_mes):
       
        if monto_ventas_mes < 0:
            monto_ventas_mes = 0
        
        # Primero calculamos el pago base con horas extra
        pago_base_con_horas = super().calcular_pago(numero_horas_extra)
        
        # Calcular la comisión por las ventas
        comision_ventas = monto_ventas_mes * (self.porcentaje_comsion / 100)  
        
        # Sumar todo para el pago total
        pago_final_del_mes = pago_base_con_horas + comision_ventas
        return pago_final_del_mes

print("\n" + "-"*40) 
# EJEMPLO DE USO
print("empleado normal")
empleado_normal = Empleado("Carlos López", 3000, 25)  
pago_mensual = empleado_normal.calcular_pago(10)
print(f"nombre del empleado: {empleado_normal.nombre}")
print(f"salario base mensual: Q{empleado_normal.salario_base}")
print(f"pago por cada hora extra: Q{empleado_normal.pago_por_hora_etra}")  
print(f"número de horas extra trabajadas: 10")
print(f"pago total a recibir: Q{pago_mensual}")

print("\n" + "-"*40) 
print("empleado con comision")
empleado_comision = EmpleadoComision("Ana Martínez", 3500, 30, 8)  # Quetzales
pago_total_ana = empleado_comision.calcular_pago(12, 15000)  # Quetzales
print(f"nombre del empleado: {empleado_comision.nombre}")
print(f"salario base mensual: Q{empleado_comision.salario_base}")
print(f"pago por cada hora extra: Q{empleado_comision.pago_por_hora_etra}")  # Error
print(f"porcentaje de comision: {empleado_comision.porcentaje_comsion}%")  # Error
print(f"número de horas extra trabajadas: 12")
print(f"monto total de ventas: Q{15000}")
print(f"pago final del mes: Q{pago_total_ana}")

print("\n" + "-"*40) 
print("prueba con numeros negativos")
# Probamos con número de horas extra negativo
pago_con_error = empleado_normal.calcular_pago(-5)
print(f"Q{pago_con_error}")

# Probamos con monto de ventas negativo  
pago_con_error_ventas = empleado_comision.calcular_pago(8, -5000)
print(f" Q{pago_con_error_ventas}")

print("\n" + "-"*40) 
print("ejemplo con ventas altas")
empleado_exitoso = EmpleadoComision("Pedro Gómez", 4000, 35, 10)
pago_exitoso = empleado_exitoso.calcular_pago(15, 25000)
print(f"nombre: {empleado_exitoso.nombre}")
print(f"ventas: Q{25000}")
print(f"horas extra: 15")
print(f"pago final: Q{pago_exitoso}")