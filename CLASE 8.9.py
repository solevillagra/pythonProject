dni= int(input ("ingrese dni: "))
puedeSubir = False

if dni % 2 == 0:
    puedeSubir = True
    print('Puede subir', puedeSubir)

else:
    puedeSubir = False
    print('No puede subir', puedeSubir)