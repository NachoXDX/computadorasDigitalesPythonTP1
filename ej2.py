import sys
f = input("Frase: ")
w = input("Palabra: ")

if w in f :
    print(f"Pos : {f.find(w) + 1} - {f.find(w) + len(w)}")
    print(f.replace(w,w.upper()))
    sys.exit()
else:
    print("No se encuentra")
    sys.exit(1)
