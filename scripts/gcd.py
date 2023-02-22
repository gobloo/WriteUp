#!/usr/bin/env python3

def gcd(a,b):
        if b == 0:
                return a
        else:
                return gcd(b, a%b)

print(gcd(a, b)) # You only need to change a, b here and run the script 
