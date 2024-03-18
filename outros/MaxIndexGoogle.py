from random import randint

def createArray():
    size = randint(10,20)
    
    filledArray = list()
    for i in range(0, size):
        filledArray.append(randint(1,55))

    return filledArray


#main
filledArray = createArray()
biggerDistancing = 0

index1=None
index2=None

for i in range(0, len(filledArray)-1):

    for j in range(0,len(filledArray[i:len(filledArray)])):

        if(filledArray[i] < filledArray[j]):
            
            if(j-i > biggerDistancing):
                biggerDistancing = j-i

                index1 = i
                index2 = j

print(f"max record: {biggerDistancing}")

print(f"input 1: {index1}")
print(f"input 2: {index2}")
print()
print(filledArray)

lenArray = []

print('[', end='')
for i in range(0, len(filledArray)):

    print(f'0{i} ', end='')

print(']', end='')