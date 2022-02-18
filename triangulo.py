h1= float(input("introduzca la altura relativa del primer lado:"))
h2= float(input("introduzca la altura relativa del sugundo lado:"))
h3= float(input("introduzca la altura relativa del tercer lado:"))

longitud1 = float(input("introduzca la longitud del primer lado:"))
longitud2 =float(input("introduzca la longitud  del sugundo lado:"))
longitud3 = float(input("introduzca la longitud  del tercer lado:"))

angulo12 = float(input("introduzca el angulo que forman los lados 1 y 2:"))
angulo13= float(input("introduzca el angulo que forman los lados 1 y 3:"))
angulo23= float(input("introduzca el angulo que forman los lados 2y 3:"))

area = longitud1 * (h1 /2)
if angulo12 or angulo13 or angulo23 == 90:
    area= longitud1*(longitud2/2)


#falta por dar las diversas posibilidades de obtener el area dependiendo de los angulos y en funcion 
#del resto de los lados y sus alturas.