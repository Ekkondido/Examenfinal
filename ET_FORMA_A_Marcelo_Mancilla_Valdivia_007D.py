import csv
import random

trabajadores = ["Juan Pérez", "Maria Garcia" , "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

nombres = []

def asignar_sueldo_aleatorios():
    for nombre in trabajadores:
        sueldos = random.randint(300000, 2500000)
        cantidades = random.randint(1, 1)
        nombres.append([{"nombre":nombre , "sueldo":sueldos , "cantidad": cantidades}])

    print("Sueldos aleatorios asignados")
 #   print(nombres["sueldo"])


def clasificar_trabajadores():
    if not nombres:
        print("No existen datos")
        return 

    bajo = [] #<800000
    mediano = []#  800000 -2000000
    alto = [] # > 20000000
    
    for nombre in trabajadores:

        monto = nombre["sueldo"]
        if monto < 800000:
            bajo.append(nombre["nombre"])

        elif 800000 <= monto <= 2000000:
            mediano.append(nombre["nombre"])
            
        else:
            alto.append(nombre["nombre"])

    print(bajo)
    print(mediano)
    print(alto)

    print(f"""

        Sueldos menores a $800000
        
        nombre empleado sueldo
        
        Sueldos entre 800000 y 2000000


        Sueldos de mas de 2000000

          
          """)
        
# Sueldo más alto
# Sueldo más bajo
# Promedio de sueldos
# Media geométrica
def verestadisticas():
    if not nombres:
        print("No existen datos")
        return
    
    sueldos = []
    cantidades = []

    sueldo_alto = nombres[0]
    sueldo_bajo = nombres[0]

    for persona in nombres:
        sueldos.append(persona["sueldo"])
        if nombres["sueldo"] > sueldo_alto:
            sueldo_alto = persona
        if nombres["sueldo"] < sueldo_bajo:
            sueldo_bajo = persona

    suma_sueldos = sum(sueldos)   
    cantidad_sueldos = len(sueldos)

    promedio_sueldos = suma_sueldos / cantidad_sueldos if cantidad_sueldos > 0 else 0

    sueldo_media_geom = 1
    for cantidad in cantidades:
        sueldo_media_geom *= cantidad

    media_gem_cantidades = (sueldo_media_geom) ** (1/len(cantidades)) if len(cantidad) > 0 else 0

    print(f"""
        Sueldo mas alto {sueldo_alto}
        Sueldos mas bajo {sueldo_bajo}
        Promedio de sueldos {promedio_sueldos}
        Media Geometrica {media_gem_cantidades}
          """)
    
def reporte_de_sueldos():
    with open ("reporte.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo liquido"])
        
        for persona in nombres:
            monto = persona["sueldo"]
            descuento_salud = monto * 0.07
            descuento_afp = monto * 0.12
            writer.writerow([nombres["nombre"], monto, descuento_salud, descuento_afp ])
            
def menu():
    while True:
        print("""
1)Asignar Sueldos Aleatorios
2)Clasificar Sueldos
3)Ver Estadisticas
4)Generar Reporte
5)Salir
              """)
        
        opc = input("Elige una opcion:")
        while not opc.isnumeric():
            opc = input("Elige una opcion:")
        opc = int(opc)

        if opc == 1:
            asignar_sueldo_aleatorios() 
        elif opc == 2:
            clasificar_trabajadores()
        elif opc == 3:
            verestadisticas()
        elif opc == 4:
            reporte_de_sueldos()
        elif opc == 5:
            print(f"""
Finalizando programa...
Desarrolado por Marcelo Mancilla
RUT 21.271.702-9
                  """)
            break
        else:
            print("Coloca una opcion valida")
menu()