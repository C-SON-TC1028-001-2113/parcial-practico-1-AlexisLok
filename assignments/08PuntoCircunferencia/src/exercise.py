import math

def main():
    # Escribe tu código abajo de esta línea
    radio = float(input("Introduce el radio: "))
    x1= float(input("Introduce x1: ")) #x del centro circunferencia
    y1= float(input("Introduce y1: ")) #y del centro circunferencia
    x2= float(input("Introduce x2: "))
    y2= float(input("Introduce y2: "))

    dis= math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    if dis == radio:
       print("SOBRE")
       pass
    elif dis > radio:
        print("FUERA")
        pass
    else:
        print("DENTRO")
        pass



if __name__ == '__main__':
    main()
