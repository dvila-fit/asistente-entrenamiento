Asistente de sesión de entrenamiento

Programa de consola en Python que registra los datos básicos de un atleta, calcula su IMC y su frecuencia cardíaca máxima estimada, define sus zonas de entrenamiento y resume las series de una sesión de gimnasio. Es mi primer proyecto de programación, hecho con los conceptos de la Unidad 1 del curso de Python.

¿Qué hace?
Pide el nombre, la edad, el peso (kg) y la altura (m) del atleta.
Calcula el IMC y lo clasifica según las categorías de la OMS: bajo peso, normal, sobrepeso y obesidad.
Estima la frecuencia cardíaca máxima con la fórmula 220 - edad.
Calcula las 5 zonas de entrenamiento como porcentajes de esa frecuencia (50 % a 100 %).
Registra el peso de cada serie hasta que se escribe 0, y calcula el total levantado, el promedio y la mayor carga.
Muestra un reporte final ordenado.
Cómo ejecutarlo

Necesitas tener Python 3 instalado. En la terminal, dentro de la carpeta del proyecto:

python asistente_entrenamiento.py
Ejemplo de salida

Con datos de ejemplo (atleta ficticio de 24 años, 70 kg, 1,75 m) y las series 40, 50 y 60 kg:

Ingresa tu nombre completo: Atleta Ejemplo
Ingresa tu edad: 24
Ingresa tu peso en Kilogramos: 70
Ingresa tu altura en metros: 1.75
 Peso de la serie en Kilogramos (0 para terminar): 40
 Peso de la serie en Kilogramos (0 para terminar): 50
 Peso de la serie en Kilogramos (0 para terminar): 60
 Peso de la serie en Kilogramos (0 para terminar): 0
========================================
REPORTE DE LA SESION
========================================
Atleta: Atleta Ejemplo
Edad: 24 años
Peso 70.0 kg | Altura 1.75 metros
IMC: 22.9 | Clasificacion: Normal de peso
FC MAX: 196 lpm
========================================
Tus zonas de entrenamiento:
 Zona 1 (Recuperacion): 98 a 118 lpm
 Zona 2 ( Aerobica base):118 a 137 lpm
 Zona 3 (Moderada): 137 a 157 lpm
 Zona 4 (Umbral): 157 a 176 lpm
 Zona 5 (Maximo esfuerzo): 176 a 196 lpm
========================================
Series:3 | Peso total: 150.0 | Promedio: 50.0 | Mayor carga: 60.0
========================================
Conceptos que practica
Variables, tipos de datos (str, int, float) y conversión de tipos con input().
Operadores aritméticos y f-strings con formato (:.1f, :.0f).
Decisiones con if / elif / else.
Bucle while con valor centinela, acumulador, contador y búsqueda del máximo.
Protección contra la división entre cero.
Control de versiones con Git y publicación en GitHub.
Limitaciones conocidas
El IMC es una herramienta de tamizaje, no un diagnóstico, y no distingue masa muscular de grasa.
Con valores muy cercanos al límite (por ejemplo, IMC 24.96) el número mostrado se redondea a 25.0, pero la clasificación usa el valor exacto.
220 - edad es una estimación sencilla y discutida; existen otras fórmulas, como la de Tanaka (208 - 0.7 × edad).
Las zonas usan una convención popular de 5 zonas; otros autores usan otros cortes.
No valida las entradas: un texto en lugar de un número detiene el programa, y un peso negativo se acepta sin avisar.
El cálculo de las zonas tiene código repetido, que se resolverá con funciones.
Próximas mejoras
Validar las entradas con bucles y try / except.
Reemplazar el código repetido de las zonas por una función.
Permitir elegir una zona objetivo y mostrar solo su rango.
Calcular la carga relativa (mayor carga dividida entre el peso corporal).
Referencias
Organización Mundial de la Salud: Obesidad y sobrepeso
Tanaka, Monahan y Seals (2001): Age-predicted maximal heart rate revisited
Autor

Diego Andrés Dávila, estudiante de Licenciatura en Educación Física (Universidad de Antioquia), con certificaciones en nutrición deportiva y entrenamiento personalizado. Aprendo Python para llegar a ser programador.