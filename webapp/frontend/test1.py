temp = b'\t\x01\x02\x03@'
print(temp)
integers = []

for byte in temp:
    integers.append(byte)
    
print(integers)