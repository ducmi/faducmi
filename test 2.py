#phuong trinh bac 2
import math

a =  float(input("a: "))
b = float(input("b: "))
while True:
    if a == 0 and b == 0:
        print('mot trong hai he so phai khac 0: ')
        a = float('vui long nhap lai he so a: ')
        b = float('vui long nhap lai he so b: ')
    else:
        break
c = float(input("c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("vo nghiem")
elif (delta == 0):
    print('phuong trinh co lenh kep x1 = x2 =', -(b / (2 * a)))
else:
    print("phuong tring co 2 nghiem phan biet:")
    print("x1=", (-(b) + math.sqrt(delta))/(2*a))
    print("x1=", (-(b) + math.sqrt(delta))/(2*a))