import sys

l = []
while True:
    tmp = input("Ingrese elemento [empty enter -> exit]: ")
    if tmp == "":
        break
    else:
        l.append(tmp)
try:        
    if l[0] == l[-1] : 
        print("Son iguales")
        sys.exit()
    else: 
        print("Son Distintos")
        sys.exit(1)
except IndexError:
    print("Lista Vacia")
    sys.exit(1)