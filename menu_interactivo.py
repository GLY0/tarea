#menu interactivo por consola
x = input("introduzca su nombre...")
print("Bienvenido a tu menu interactivo",x)

while(True):
    print("""elije una opcion
    1) Calcular si un número es par o impar
    2) Calcular la edad del usuario
    3) salir""")

    opcion = input()

    if opcion == "1":
        y = int(input("introduzca un valor numerico:"))
        y=y%2
        if y==0:
            print("su numero es par")
        else:
            print("su numero es impar")          
    elif opcion == "2":
        anio = int(input("introduzca su año de nacimiento"))
        actual = 2021
        def resta():
            k= actual - anio
            print("su edad actual es",k)
            resta()
    elif opcion == "3":
        print("Gracias por visitarnos",x,"=D")
        break


        

