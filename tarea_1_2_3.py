#Ejercicio 1
"""""
print("como te llamas?")
x = input("escribe tu nombre aqui..")
text = "Un gusto saludarte {} !!"
print(text.format((x)))
"""""
#Ejercicio 2
"""
n = input("ingresa tu nombre:")
print("Hola",n)

while(True):
    print(""elije una opcion"
    "1)Calcular el perimetro de un circulo
    "2) Calcular el area de un circulo
    "3) salir"")
    opcion = input()

    if opcion == "1":
        r = int(input("ingresa el valor del radio del circulo"))
        p = (2*3.14)
        print(p*r)
        

    elif opcion == "2":
        R = int(input("ingresar el valor del radio del circulo"))
        a = 3.14
        print(a*R**2)

    elif opcion == "3":
        print("Gracias por visitarnos",n,"=D")
        break    
"""
#Ejercicio 3
"""
numero1 = int(input("ingrese un valor numerico"))
numero2 = int(input("ingrese un valor numerico"))

def suma():
    s= numero1 + numero2
    print("la suma entre ambos numeros es",s)
suma()

def resta():
    r= numero1 - numero2 
    print("la resta entre ambos numeros es",r)
resta()

def multiplicacion():
    m= numero1*numero2
    print("la multiplicacion entre ambos numeros es",m)
multiplicacion()

print("Eso es todo =D")
"""
#Ejercicio 4
"""""
x = input("escribe una palabra")

print( x*1000)
"""""
#Ejercicio 5
"""
m= int(input("ingrese una cantidad determinada de minutos"))

def conversion():
    h = m//60
    M = *60 
    print(m,"equivalea a",h,"horas con",M,"minutos")
conversion() 
incompleto"""
#Ejercico 6
"""
print("Manejado con el sistema internacional")
alto = int(input("ingrese el valor de la altura del rectangulo"))
ancho = int(input("ingrese el valor del ancho del rectangulo"))  
area = alto*ancho
Perimetro = 2*alto + 2*ancho
print("Segun los datos proporcionados: el area del rectangulo es",area,"y el perimetro del rectangulo es",Perimetro)
"""
#Ejercicio 7
"""
while(True):
    a = int(input("ingrese un primer valor numerico")) 
    b = int(input("ingrese un segundo valor numerico"))
    c = a + b 
    print(c)
    0==0 
    if (c<0):
        print("la suma entre ambos numeros es negativa")
    elif (c>0): 
        print("la suma entre ambos numeros es positiva")
    elif (c==0):
        print("la suma entre ambos numeros es igual a 0")
    break
"""
#Ejercico 8

"""
while(True):
    y = int(input("introduzca un valor numerico:"))
    y=y%2
    if y==0:
        print("su numero es par")
    else:
        print("su numero es impar")
    break
"""
#Ejercicio 9
"""
a=int(input("Mes(numero segun el orden del calendario):"))

if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("el mes tiene 31 dias")

elif a==2:
    print("el mes tiene 28 dias")

elif  a==4 or a==6 or a==9 or a==11:
    print("el mes tiene 30 dias")

else:
    print("incorrecto")
"""
#Ejercicio 10
"""
nombre_de_usuario = input("ingresar el nombre de usuario")
contraseña = input("ingresar la contraseña")

if nombre_de_usuario == "pepe" and contraseña=="passwd#":
    print("has entrado al sistema")
else:
    print("error")
"""
#Ejercicio 11
"""     
year = int(input("año:"))

if 0==year%4 or 0!=year%100 and 0==year%400:
    print("este año es bisiesto")
else:
    print("error")
"""
#Eejercicio 12
"""
letra=input("Letra:")		
if letra>="A" and letra<="Z":
	print("Mayuscula")
else:
	print("No mayuscula")
"""
#Ejercicio 13
"""
x = int(input(" introdusca un valor numerico"))

text= "tabla de multiplicar del {}.. es" 
print(text.format(x))

for y in range(0,13):
    print(f"{x} * {y} = {x*y}")
"""
#Ejercicio 14
"""
d = int(input("ingrese un numero factoreable"))

fact=1
for i in range(2,d+1):
	fact*=i
print("El resultado es %x" % d)
""" #incompleto
#Ejercicio 15
               


