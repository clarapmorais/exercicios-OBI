#I 1
#V 5
#X 10
#L 50
#C 100
#D 500
#M 1000
#1345 = MCCCXLV

roman_str = str(input("Escreva um número romano: "))

roman_int = 0
for e in roman_str:
    if(e in "Mm"):
        roman_int += 1000
    elif(e in "Dd"):
        roman_int += 500
    elif(e in "Cc"):
        roman_int += 100
    elif(e in "Ll"):
        roman_int += 50
    elif(e in "Xx"):
        roman_int += 10
    elif(e in "Vv"):
        roman_int += 5
    elif(e in "Ii"):
        roman_int += 1

print(roman_int)