import sys
def main():
    vals = [11,3,0,3,4,6,8,3,6,8,1]
    printHead()
    for i in range(len(vals)):
        printRow(i,vals[i])
    sys.exit()
def printHead():
    print("Indice","Valor","Histograma",sep="  ")

def printRow(i,v):
    print(f"{i:<8}{v:<6}","@"*v)

if __name__ == "__main__":
    main()