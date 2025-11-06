#buat list berisi 5 bilangan genap positif pertama
G = []
for i in range(1,6):
    G.append(2*i)
print(G)

#buat list berisi 6 bilangan ganjil pertama: 1,3,5,7,9,11
B = []
for j in range(6):
    B.append(2*j+1)
print(B)

#list comprehension
G = [2*i for i in range(1,6)]
print(G)
C = [2*j-1 for j in range(1,7)]
print(C)