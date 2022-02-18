nota1 = float(input("introduzca la primera nota:"))
nota2= float(input("introduzca la segunda nota:"))
nota3= float(input("introduzca la tercera nota:"))
media=0
ponderacionnota1 = float(input("cuanto pondera la primera nota en porcentaje:"))
ponderacionnota2 = float(input("cuanto pondera la segunda nota en porcentaje:"))
ponderacionnota3 = float(input("cuanto pondera la tercera nota en porcentaje:"))
media = nota1*ponderacionnota1 + ponderacionnota2*nota2 + ponderacionnota3*nota3
print("su media es de :")
print(media)

#faltaria por asegurar que las medias suman 100 y que las notas son menores o iguales a 10.