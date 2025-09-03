#Solicitar datos del terreno
base= float(input("Ingrese la base del terreno en metros: "))
altura= float(input("Ingrese la altura del terreno en metros: "))

#Calcular el area del terreno 
Area_triangulo= (base * altura)/2
Area_cuadrado= (base * base)
Area_total= Area_triangulo + Area_cuadrado

#Precio del terreno 
Precio_metro_cuadrado = 4400000
Precio_total_terreno= Area_total*Precio_metro_cuadrado

#Mostrar informacion
print (f"El area total del terreno es: {Area_total} mts^2")
print(f" El precio toral del terreno es: ${Precio_total_terreno} COP")