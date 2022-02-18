nombre = input("introduzca el nombre de su trabajador:")
sueldoxhora = float(input("cuanto cobra su empleado por hora:"))
horastotal = float(input("cuantas horas trabajo este mes?"))
horasextra = 0
sueldomerecido = 0
horasnormales = 0
if horastotal <= 35:
    horasextra = 0
else:
    horasextra = horastotal - 35    

horasnormales= horastotal - horasextra

if horasextra <= 7:
    sueldomerecido= (horasnormales*sueldoxhora)+ (sueldoxhora*horasextra*5/4)
else:
    sueldomerecido= (horasnormales*sueldoxhora)+ (sueldoxhora*7*5/4)+((horasextra-7)*sueldoxhora*6/4)

print(nombre + "deberia cobrar :")
print(sueldomerecido) 