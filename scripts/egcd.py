#!/usr/bin/env python3
def egcd(a, b):
  a, b = int(a), int(b)
  if a == 0:
    return b, 0, 1
  else:
    gcd, x, y = egcd(b % a, a)
  return gcd, y - (b // a) * x, x

print(egcd(a, b)) # You only need to change a,b here.
