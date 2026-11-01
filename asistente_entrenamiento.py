"""
Asistente de sesion de entrenamiento 

Descripción: 
Programa de consola de python que restra los datos de una persona, calculando su IMC
y su frecuencia cardiaca maxima estimada, restra la series de un  ejercicios y muestra
un reporte final 

Autor: Diego Davila 
Fecha: 31/10/2026
Version: 0.1 

¿Que hace?
1. Pide nombre, edad, peso, y estatura
2. Calcula el IMC y lo califica segunas las categorias de la OMS
3. Estima la FC maxima, con la formula 220- edad
4. Restra el peso de cada serie, hasta que se ingrese 0
5. Muestra el total levantado, el promedio y la mayor carga 

Conceptos de la Unidad 1 que usa: 
Variables, tipos de datos, input y casting, operadores if/elif/else
bucle while, f-strings. 
"""
# Informacion personal 
nombre = input("Ingresa tu nombre completo: ")
edad = int(input("Ingresa tu edad: "))
peso_kg = float(input("Ingresa tu peso en Kilogramos: "))
altura_m = float(input("Ingresa tu altura en metros: "))

# Clasificacion del IMC
imc = peso_kg / altura_m **2
if imc < 18.5: 
    clasificacion = "Bajo peso" 
elif imc < 25:
    clasificacion = "Normal de peso"  
elif imc < 30:
    clasificacion = "Sobrepeso" 
else:
    clasificacion = "Obesidad" 

# Calculo de frecuencia cardiaca maxima 
fc_max = 220 - edad

# Calculo de zonas de entrenamiento 
z1_min = fc_max * 0.5 
z1_max = fc_max * 0.6
z2_min = fc_max * 0.6
z2_max = fc_max * 0.7
z3_min = fc_max * 0.7
z3_max = fc_max * 0.8 
z4_min = fc_max * 0.8 
z4_max = fc_max * 0.9 
z5_min = fc_max * 0.9 
z5_max = fc_max * 1.0 

# Informacion del entrenamiento 
peso_serie= float(input(" Peso de la serie en Kilogramos (0 para terminar): "))
total_kg= 0
series= 0 
mayor_peso = 0 

while peso_serie != 0:
    total_kg= total_kg + peso_serie
    series= series + 1 
    if peso_serie > mayor_peso:
        mayor_peso= peso_serie
    peso_serie= float(input(" Peso de la serie en Kilogramos (0 para terminar): "))

if series == 0: 
    promedio_kg= 0
    print("No restraste ninguna serie")
    print("No restraste ningun peso")
else: 
    promedio_kg = total_kg / series

# Muestra de salidas con su informacion
print("=" * 40) 
print("REPORTE DE LA SESION")
print("=" * 40) 
print(f"Atleta: {nombre}")
print(f"Edad: {edad} años")
print(f"Peso {peso_kg} kg | Altura {altura_m} metros") 
print(f"IMC: {imc:.1f} | Clasificacion: {clasificacion}") 
print(f"FC MAX: {fc_max} lpm") 
print("=" * 40) 
print("Tus zonas de entrenamiento:")
print(f" Zona 1 (Recuperacion): {z1_min:.0f} a {z1_max:.0f} lpm ") 
print(f" Zona 2 (Aerobica base):{z2_min:.0f} a {z2_max:.0f} lpm ")
print(f" Zona 3 (Moderada): {z3_min:.0f} a {z3_max:.0f} lpm")
print(f" Zona 4 (Umbral): {z4_min:.0f} a {z4_max:.0f} lpm") 
print(f" Zona 5 (Maximo esfuerzo): {z5_min:.0f} a {z5_max:.0f} lpm") 
print("=" * 40) 
print(f"Series:{series} | Peso total: {total_kg:.1f} | Promedio: {promedio_kg:.1f} | Mayor carga: {mayor_peso:.1f}")
print("=" * 40) 


