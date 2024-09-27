mi_string="Hola Mundo"
print(mi_string)
print(mi_string[0])
print(mi_string[0:4])
print(mi_string[5:])
print(mi_string[:4])
print(mi_string.find("Mundo"))
print(mi_string.lower())
print(mi_string.upper())
texto= mi_string.replace("Mundo", "universo")
print(texto)
print(len(mi_string))
print(mi_string)
print(mi_string.split(" "))
print(type(mi_string.split(" ")))
print(texto.title())
print(texto.capitalize())
texto2="             Hola Mundo"
print(texto2.strip())
print(f"este metodo es como .lower {texto.casefold()}")

variabele1="hola mi nombre es {} y tengo {} años".format("Juan", 32)
print(variabele1)
nombre="Juan"
edad=32
pais="Colombia"
print("hola mi nombre es {} y tengo {} años y soy de {}".format(nombre, edad, pais))
print(f"hola mi nombre es {nombre} y tengo {edad} años y soy de {pais}")
print("hola mi nombre es {1} y tengo {0} años y soy de {2}".format(edad, nombre, pais))