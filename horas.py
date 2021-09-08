minXhora = 60
horaEnSeg = 3600
segundosPorMinuto= 60

#1- Recibir cantidad de horas
horas = float(input("Ingrese la cantidad de horas: "))

#2- Recibir total minutos
minutos = float(input("Ingrese la cantidad de minutos: "))

#3- Convertir horas en minutos:
minutosEnHoras = horas * minXhora

#4- Sumar total de minutos
totalMinutos = minutosEnHoras + minutos

#5- Convertir  totalMinutos en segundos
totalSegundos = totalMinutos * segundosPorMinuto

print("La cantidad total de minutos transcurridos es:", totalMinutos)
print("La cantidad total de segundos transcurridos es:", totalSegundos)