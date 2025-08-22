## Realizando y Aplicando atributos privados y protegidos a los ejercicios 40 y 41


Ejercicio 40:
Crea una clase base Factura que reciba una lista de ítems (tuplas (descripcion, precio)), y un
descuento en %.
• Métodos:
o subtotal() → suma de precios.
o total() → aplica descuento al subtotal.
Crea una clase hija FacturaConImpuesto que herede de Factura y agregue:
• iva en % (por ejemplo, 12)
• Sobrescriba total() para:
1. usar super().total() (ya con descuento aplicado),
2. luego sumar IVA sobre ese monto.
Nota: si el descuento es inválido (<0 o >100) debe ignorarse (o ajustar a límites).

Ejercicio 41: Nómina con horas extra y comisión
Crea una clase base Empleado con:
• nombre
• salario_base (mensual)
• pago_hora_extra (monto por hora)
• método calcular_pago(horas_extra) → salario_base + horas_extra * pago_hora_extra
Crea una clase hija EmpleadoComision que además reciba:
• porcentaje_comision (por ejemplo, 5 = 5%)
• Sobrescriba calcular_pago(horas_extra, ventas_mes) para:
1. llamar a super().calcular_pago(horas_extra)
2. agregar la comisión sobre ventas_mes.
Valida que horas_extra ≥ 0 y ventas_mes ≥ 0.
