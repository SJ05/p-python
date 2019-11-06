# example on how to catch an Exception Error
# particularly ZeroDivisionError
x=0
y=0

# using try except
try:
	z1 = x / y
except ZeroDivisionError
	z1 = 0
print(z1)
	
# check null
if y != 0:
	z2 = x / y
else:
	z2 = 0
print(z2)

# can be reduced to
z3 = (x / y) if y != 0 else 0
print(z3)