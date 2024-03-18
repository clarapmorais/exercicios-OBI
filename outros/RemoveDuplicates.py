s = str(input("insira string: "))

found_elements = ''
for e in s:
    if e not in found_elements:
        found_elements+=e
    
print(found_elements)