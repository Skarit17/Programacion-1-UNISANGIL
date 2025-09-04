# Reto 2 - Agua en un edificio
# Programa de acuerdo al Quiz

# Pedir datos al usuario
consumo_persona = float(input("¿Cuál es el consumo promedio de agua por persona en litros/día?: "))
numero_personas = int(input("¿Cuántas personas viven en el edificio?: "))
capacidad_tanque = float(input("¿Cuál es la capacidad de cada tanque en litros?: "))
eficiencia_tanque = float(input("¿Cuál es la eficiencia del tanque en %?: ")) / 100
dias_inactivos = int(input("¿Cuántos días al año está inactivo el sistema por mantenimiento?: "))
area_tanque = float(input("¿Cuántos metros cuadrados ocupa un tanque?: "))
area_disponible = float(input("¿Cuál es el área total disponible en metros cuadrados?: "))

# Cálculos
consumo_diario = consumo_persona * numero_personas
consumo_anual = consumo_diario * 365
consumo_total = consumo_anual + (consumo_diario * dias_inactivos)
capacidad_util = capacidad_tanque * eficiencia_tanque
tanques_necesarios = consumo_total / capacidad_util
area_total = tanques_necesarios * area_tanque
autonomia = (tanques_necesarios * capacidad_util) / consumo_diario
litros_por_persona = (tanques_necesarios* capacidad_util) / (numero_personas * 30)

# Resultados
print(f"Consumo diario del edificio: {consumo_diario }litros")
print(f"Consumo anual del edificio: {consumo_anual} litros")
print(f"Consumo total con días extra: {consumo_total} litros")
print(f"Capacidad útil de un tanque: {capacidad_util} litros")
print(f"Número de tanques necesarios (aprox): {tanques_necesarios}")
print(f"Área total requerida: {area_total} m^2")
print(f"Área disponible: {area_disponible} m^2")
print(f"Autonomía del sistema (días): {autonomia}")
print(f"Litros por persona en 30 días de sequía: {litros_por_persona}")
