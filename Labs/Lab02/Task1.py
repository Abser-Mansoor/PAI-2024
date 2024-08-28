from math import *

def areatrap(parallel_a,parallel_b,height) :
    return 0.5*(parallel_a+parallel_b)*height

def areapara(base,height) :
    return base*height;

def cylindervol(radius,height) :
    return radius*radius*pi*height
    
def cylinderarea(radius,height) :
    return radius*height*pi + pi*radius*radius
    
print(areatrap(4,5,10),areapara(10,20),cylindervol(5,3),cylinderarea(5,3),"\n")
