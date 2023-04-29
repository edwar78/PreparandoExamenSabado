from Escuderia import Escuderia

escuderias=[]
contador = 1
numeroEscuderias= int(input("Digite el numero de escuderias"))
while contador <= numeroEscuderias:
    escuderia=Escuderia()
    escuderia.nombre=input("digite el nombre de la escuderia")
    escuderia.casaMotor=input("digite la casa motor de la escuderia")
    escuderia.pilotoPrincipal.nombre=input("digite el nombre de la piloto")
    escuderia.piloto2.nombre=input("digite el nombre de la escuderia")
    escuderia.piloto2.pais=input("dite el pais del piloto principal")
    escuderia.piloto2.fechanacimiento=input("dite el fecha de nacimineto del piloto")
    escuderia.piloto2.salarioanula=input("dite el salario del piloto principal")
    escuderia.pilotoPrincipal.salarioanula=input("dite el salario del piloto principal")
    escuderia.pilotoPrincipal.fechanacimiento=input("dite el fecha de nacimineto del piloto principal")
    escuderia.pilotoPrincipal.pais=input("dite el pais del piloto principal")
    escuderia.costo=input("ingrese costo")

    escuderia.append(Escuderia)

    contaor=contador+1

    #recorriendo la lista de erscuderia
    for escuderia in escuderias:
        print (escuderia.nombre, escuderia.costo)
    
    
    costoMayor=0
    nombreEscuderiamascara=None
    for escuderia in escuderias:
        if escuderia.costo >costoMayor:
            costoMayor= escuderia.costo