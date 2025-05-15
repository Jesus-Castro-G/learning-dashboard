import csv

ruta_archivo = "data/progreso.csv"

usuarios = []
porcentajes = []
horas = []

# Leer los datos del CSV
with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        usuarios.append(fila["nombre_usuario"])
        porcentajes.append(float(fila["porcentaje_completado"]))
        horas.append(float(fila["horas_estudio"]))

# Calcular promedios
promedio_porcentaje = sum(porcentajes) / len(porcentajes)
promedio_horas = sum(horas) / len(horas)

# Mostrar resultados
print("Resumen de Progreso de Aprendizaje")
print("-----------------------------------")
print(f"Total de usuarios: {len(usuarios)}")
print(f"Promedio de porcentaje completado: {promedio_porcentaje:.2f}%")
print(f"Promedio de horas de estudio: {promedio_horas:.2f} horas")
