

#bucle for para recorrer lista array.
for i in range(21):
    print(i)
lista_frutas=["manzana", "pera", "uva", "mango", "fresa"]

for i in lista_frutas:
    print(i)
#añadir un elemento a la lista
lista_nueva=["manzana", "pera", "uva", "mango", "fresa"]
for i in lista_frutas:
    lista_nueva.append(i)
print(lista_nueva)
verduras=["zanahoria", "lechuga", "tomate", "pepino", "papa"]
for i in lista_nueva:
    verduras.insert(0, i)
print(verduras)
#tablas de multiplicar
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("\n")
print("fin")

#list comprehension
listaNumeros=[]
[listaNumeros.append(i) for i in range(1, 21)]
print(listaNumeros)

#con map
listaNumeros2=list((map(lambda i: i , range(1, 21))))
print(listaNumeros2)

#añadir elementos con map
listaFrutasMap=list(map(lambda i: i, lista_frutas))
print(listaFrutasMap)

#recorrer lista con for y enumerate

coches_deportivos = [
    "Porsche 911",
    "Maserati MC20",
    "Porsche 718 Cayman",
    "Porsche 718 Boxster",
    "Audi R8",
    "BMW M2",
    "Toyota GR Yaris",
    "Alpine A110",
    "BMW M4 Competition",
    "Volkswagen Golf GTI",
    "BMW Z4",
    "Mercedes CLE",
    "Honda Civic Type R",
    "Toyota GR Supra",
    "Ford Mustang",
    "Hyundai Ioniq 5 N",
    "Mazda MX-5",
    "Cupra León",
    "Cupra Formentor",
    "BMW M3",
    "Audi RS5 Sportback",
    "Audi RS7 Sportback",
    "Porsche Panamera",
    "Abarth 595 Competizione",
    "Ford Focus ST",
    "Peugeot 208 GTi",
    "Subaru BRZ",
    "Nissan Z",
    "Chevrolet Corvette",
    "Jaguar F-Type"
]

coches_deportivos.insert(2, "Bugatti Veyron")
coches_deportivos.append("Bugatti Chiron")
coches_deportivos.insert(2, "Bugatti Veyron Super Sport")
if "Porsche 911" in coches_deportivos:
    print("Porsche 911 está en la lista")

print(coches_deportivos)

#opcion para no usar enumerate usando range(len())


for i in range(len(coches_deportivos)):
    print(f" Este resultado es for con range(len()) => {i} - {coches_deportivos[i]}")


for i, coche in enumerate(coches_deportivos):
    print("{} - {}".format(i, coche))

#otra forma de hacerlo while
i=0
while i < len(coches_deportivos):
    print(f" ESTE BUCLE ES CON WHILE {i} - {coches_deportivos[i]}")
    i+=1


#otra forma con un contador
contador=0
for i in coches_deportivos:
    print(f"{contador} / {i}")
    contador+=1


listaNuevaCochesUpper=list(map(lambda i : i.upper(), coches_deportivos))
print(listaNuevaCochesUpper)

#con lis comprension
listaNuevaCochesComprension=[i  for i in coches_deportivos]
print(listaNuevaCochesComprension)

listaVacia=[]
for i in coches_deportivos:
    listaVacia.append(i.upper())
print(f"este resultado es con el bucle for normal \n{listaVacia}")


listaTecnologias=["Python", "Java", "JavaScript", "C#", "C++", "PHP", "Ruby", "Swift", "Kotlin", "Go", "Rust", "Scala",
                  "Perl", "R", "Objective-C", "TypeScript", "Dart", "Shell", "PowerShell", "SQL", "HTML", "CSS", "XML", "JSON",
                  "YAML", "Markdown", "LaTeX", "Bash", "Batch", "Vim", "Emacs", "Sublime Text", "Visual Studio Code", "Eclipse",
                  "NetBeans", "IntelliJ IDEA", "Android Studio", "Xcode", "Atom", "Brackets", "Notepad++", "Nano", "Pico", "Gedit", "Kate"]




listaNuevaConA=list(filter(lambda i: i[0]=="A", listaTecnologias))
print(listaNuevaConA)
print(len(listaNuevaConA))

lista2=[]
for i in listaTecnologias:
    if i[0]=="A":
        lista2.append(i)
print(f"este es con for tradicional {lista2}")

#con list comprehension
lista3=[i for i in listaTecnologias if "e" in i]
print(lista3)
listaCochesConPorsche=[i for i in coches_deportivos if 'Porsche'in i]
print(listaCochesConPorsche)
listaBugatis=list(filter(lambda i: i if 'Bugatti'in i else "", coches_deportivos))
print(listaBugatis)


























