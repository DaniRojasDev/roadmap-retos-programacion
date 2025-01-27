"""
Operaciones con string
"""

s1 = "Hola"
s2 = "Dani"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2]) #Muestra los caracteres que hay en las posiciones que le decimos

# Longitud
print(len(s2))

# Slicing (porción)
print(s1[2:4]) # Muestra desde la posición que le indiquemos hasta la que le volvamos a indicar
print(s1[2:]) # Muestra desde la posición que le indiquemos hasta el final
print(s1[0:2])  
print(s1[:2])  # Muestra desde el principio hasta la posición que le indiquemos

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("ol", "ar")) # Cambia lo primero que le indiquemos por lo segundo

# División
print(s2.split("a"))  # divide por la letra que le indiquemos

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("dani rojas".title()) # Pone la primera letra de cada palabra en mayuscula
print("danie rojas".capitalize())  # Pone solo la primera letra del string en mayuscula

# Eliminación de espacios al principio y al final
print(" Dani Rojas ".strip())

# Búsqueda al principio y al final  dan true o false según sea verdad o mentira que el str empieza por lo indicado
print(s1.startswith("Ho"))
print(s1.startswith("Da"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

# Búsqueda de posición
print(s1.find("l"))
print(s1.find("H"))
print(s1.find("a"))
print(s1.lower().find("h")) # Se pueden encadenar funciones, la primera pone todos los caracteres en minus y luego busca sin discriminar

s2="DANIdani"
# Búsqueda de ocurrencias
print(s2.lower().count("a")) # La primera pone todos los caracteres en minus y luego cuenta cauntas veces aparece lo que le indiquemos

s2="Dani"
# Formateo
print("Saludo: {}, nombre: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, nombre: {s2}!")

# Tranformación en lista de caracteres
print(list(s2)) # Convierte el string en una lista de caracteres

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1)) # Convierte la lista en un string

# Transformaciones numéricas
s3 = "123456"
s3 = int(s3)
print(s3)
print(type (s3))

s4 = "123456.123"
s4 = float(s4)
print(s4)
print(type(s4))

# Comprobaciones varias
s3 = "123456"
print(s1.isalnum())
print(s1.isdigit())
print(s1.isalpha())
print(s3.isalpha())
print(s3.isnumeric())
print(s3.isdigit())


'''
Extra
'''
