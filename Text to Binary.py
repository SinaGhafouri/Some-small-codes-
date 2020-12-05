T = 'HEY YOU.'

asc = []
for i in T:
    asc.append(ord(i))
binary = []
for num in asc:
    for i in range(7, -1, -1):
        if 2**i <= num:
            num -= 2**i
            print(1,end="")
            binary.append(1)
        else:
            print(0,end="")
            binary.append(0)

print('\n\n = \n')

#binary = '0100100001000101010110010010000001011001010011110101010100101110'

j = 0
for i in range(int(len(binary)/8)):
    s = 0
    for k in range(8):
        if int(binary[k+j]) == 1:
            s += 2**(7-k)
    print(chr(s), end="")
    s = 0
    j+=8
    
