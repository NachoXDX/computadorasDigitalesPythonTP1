import sys
r = int(input("R[ohm] : "))
i = int(input("I[A] : "))
p = i**2 * r
if p > 5 :
    print("Evacuar Calor")
sys.exit()