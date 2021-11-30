#Ejercicio 1

"""""
print("como te llamas?")
x = input("escribe tu nombre aqui..")
text = "Un gusto saludarte {} !!"
print(text.format((x)))
"""""

#Ejercicio 4

"""""
x = input("escribe una palabra")

print( x*1000)
"""""

#ejercicio 13

"""""
from typing import Text


x = int(input(" introdusca un valor numerico"))

text= "tabla de multiplicar del {}.. es"
print(text.format(x))

for y in range(0,13):
    print(f"{x} * {y} = {x*y}")
"""""

