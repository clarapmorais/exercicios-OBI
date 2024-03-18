from random import randint

n = int(input("Insira o tamanho do array: "))

arr = []
for i in range(0, n):
    arr.append(int(input()))

triplets=0
for j in range(0, n):

    for k in range(j+1, n):

        if(arr[j] + arr[k] in arr):
            triplets+=1
            print(f"found triplet: {arr[j]} + {arr[k]} = {arr[j]+arr[k]}")

print(f"total found triplets: {triplets}")