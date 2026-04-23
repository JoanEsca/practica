import os
os.system("cls")

IVA = 1.19
PRESUPUESTO_MAXIMO = 50000000
presupuesto_ajustado = PRESUPUESTO_MAXIMO * 1.10

# Sistema de Presupuesto de Construcción
#  Objetivo
# Desarrollar un programa en Python que calcule el costo total de un proyecto de construcción y determine si está dentro del presupuesto.
# ________________________________________
#  Enunciado
# Una constructora necesita un programa para estimar el costo de un proyecto en base a materiales y mano de obra.
# El programa debe:
# 1.	Solicitar al usuario: 
# o	Nombre del proyecto 
# o	Cantidad de metros cuadrados a construir 
# o	Costo por metro cuadrado 
# o	Cantidad de trabajadores 
# o	Pago por trabajador 

nombre_proyecyo = input("Ingrese el Nombre del proyecto\n")
try:
    metros_cuadrado = float(input("Cantidad de metros cuadrados a construir\n"))
    costo_por_metro = float(input("Costo por metro cuadrado\n"))
    trabajadores = int(input("Cantidad de trabajadores\n"))
    pago_por_trabajador = float(input("Pago por trabajador\n"))
    if metros_cuadrado > 0 and costo_por_metro >0 and trabajadores >0 and pago_por_trabajador >0:
        
        costo_material = metros_cuadrado * costo_por_metro
        mano_de_obra = trabajadores * pago_por_trabajador
        costo_neto = costo_material + mano_de_obra
        Costo_total = costo_neto * IVA  
        ct_redondeado = round(Costo_total, 2)
        if Costo_total <= PRESUPUESTO_MAXIMO:
            estado = "dentro del presupuesto"
        elif Costo_total > PRESUPUESTO_MAXIMO and costo_neto <= presupuesto_ajustado:
            estado = "presupuesto ajustado"
        else:
            estado = "Fuera del presupuesto"
        
        print(f"nombre del proyecto: {nombre_proyecyo}")
        print(f"Costo Total: {ct_redondeado}")
        print(f"estado: {estado}")
    else:
        print("Los valores tienes que ser mayor a cero")
    
except:
    print("Solo valor numerico")


# 2.	Definir las siguientes constantes: 
# o	IVA = 0.19 
# o	PRESUPUESTO_MAXIMO = 50000000 (50 millones) 
# 3.	Validar que todos los datos numéricos: 
# o	Sean números válidos 
# o	Sean mayores que 0
# En caso de error, manejar la situación con try-except. 
# 4.	Calcular: 
# o	Costo de materiales = metros cuadrados × costo por metro 
# o	Costo de mano de obra = trabajadores × pago por trabajador 
# o	Costo neto = suma de ambos 
# o	IVA aplicado 
# o	Costo total del proyecto 
# 5.	Usar variables auxiliares para almacenar cálculos intermedios. 
# 6.	Determinar el estado del proyecto: 
# o	Si el costo total es menor o igual al presupuesto → Dentro del presupuesto 
# o	Si supera el presupuesto hasta en un 10% → Presupuesto ajustado 
# o	Si supera en más de un 10% → Fuera de presupuesto 
# 7.	Mostrar un resumen con: 
# o	Nombre del proyecto 
# o	Costo total (redondeado a 2 decimales) 
# o	Estado del proyecto 
# ________________________________________
#  Condiciones
# •	Debe utilizar try-except para evitar errores de entrada. 
# •	Debe usar if, elif y else. 
# •	Debe definir y utilizar constantes correctamente. 
# •	El programa no debe terminar abruptamente ante errores.





















