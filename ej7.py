import sys

def main():
    while True:
        l = input("Caracter: ")
        if len(l) != 1:
            print("Debe ser solo un caracter")
        else:
            break
    while True:
        try:
            s = int(input("Tamano: "))
        except:
            print("Debe ser un entero!")
        else:
            break
    imprimirCuadrado(l,s)
    sys.exit()
    
def imprimirExt(l,s):
    print(f"{l}"*s)

def imprimirMed(l,s):
    for i in range(s-2):
        print(l," "*(s-2),l,sep="")

def imprimirCuadrado(l,s):
    imprimirExt(l,s)
    imprimirMed(l,s)
    imprimirExt(l,s)


if __name__ == "__main__":
    main()