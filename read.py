import csv

def openA():
    with open("data.csv","r")as file:
        x = csv.reader(file,delimiter="|")
        for line in x:             
            print line
def readA():
    nombre = raw_input("Nombre:     ")
    email = raw_input("Email:       ")
    with open("data.csv", "a")as file:
        y = csv.writer(file,delimiter="|")
        y.writerow([nombre, email])
print "**Agneda**"
eleccion = 0
while eleccion <= 2:
    print("Menu \n 1.- Leer archivo \n 2.- Nuevo contacto \n 3.- Salir")
    eleccion = int(raw_input("Elige una opcion:        ")) 
    if eleccion == 1:
        openA()
    elif eleccion == 2:
        readA()
print "Fin del programa"
