dineroaccion= float(input("cuanto dinero cuesta cada accion?:"))
beneficiomes= float(input("que porcentaje tiene de beneficio mensual?:"))
numeroacciones= float(input("cuantas acciones tiene compradas?"))
numeromeses=float(input("cuantos meses va a dejar usted su dinero guardado?:"))
total= (dineroaccion*numeroacciones)

for numeromeses in range(1):
    total += (dineroaccion*numeroacciones*beneficiomes/100)
for numeromeses in range >2:
    total +=  (total*beneficiomes/100)

print (total)


#falta por ajustar el interes repartido en los meses.
