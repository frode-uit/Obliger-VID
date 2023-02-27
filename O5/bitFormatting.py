# int til binær
from re import S


print(f'{ord("a"):08b}') # ledende 0 i bredde 8
print(f'{255:08b}')
number = 1
print(f'{number:08b}')
print(bin(255))
print(f'{255:02x}')

#binær til int / hex
binStr = "11111111"
print(f'{int(binStr,2)}') # 2 er basen
print(f'{int("ff",16)}') # 16 er basen

# Bitwise operasjoner
first = "10101110"
second = "10010010"
f = int(first,2)
s = int(second,2)
print(f'first :{f:08b}')
print(f'second:{s:08b}\n')
print(f'AND   :{f & s:08b}') # bitwise AND
print(f'OR    :{f | s:08b}') # bitwise OR
print(f'XOR   :{f ^ s:08b}') # bitwise exclusive OR
print(f'ECOMP :{~f & 255:08b}') # eners komplement
print(f'SHIFTL:{f<<2 & 255:08b}')
print(f'SHIFTR:{f>>2:08b}')
