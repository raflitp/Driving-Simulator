sym = ("*")
count = 8
mult = 1
while mult <= count:
    print (" " * (count - mult) + "*" * mult + "*" * (mult-1))
    mult=mult+1

count = 8
mult = 1
while mult <= count:
    print (" " * (count - mult) + "*" * mult)
    mult=mult+1

count = 8
mult = 1
while mult<= count:
    print mult*sym
    mult=mult+1

n=8
for idx in range (n-1):
    print((n-idx)*' '+(2*idx+1)*'*')
for idx in range (n-1,-1,-1):
    print((n-idx)*' '+(2*idx+1)*'*')

