import math


def is_a_triangle(lado1, lado2, base): 
    triangle = bool 
    if (lado1 + lado2) < base:
        triangle = False
        return triangle
    else:
        triangle = True
        return triangle

def areatriangle(lado1, lado2, base, triangle):
    
    if triangle:
        s = (lado1 + lado2 + base) / 2
        a = math.sqrt(s * (s - lado1) * (s - lado2) * (s - base))
        return a
    else:
        print("This is not triangle")
       
lado1 = ''
lado2 = ''
base = ''
while((lado1 == '') or (lado2 == '') or (base == '')):
    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    base = int(input("base: "))

    if is_a_triangle(lado1, lado2, base):
        print("This is a triangle.")
        print("The triangle area:", areatriangle(lado1, lado2, base, triangle=True))
    else:
        print("Is not triangle.")
