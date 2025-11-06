print("Contoh 1") #append
A = [1, 3]
print(A)
A.append(20)
print(A)

print("\nContoh 2") #clear
B = [1, 3, 4]
print(B)
B.clear() 
print(B)

print("\nContoh 3") #copy
C = [1, 2, 3]
print(C)
X = C.copy()
print(X)
Y = C
print(Y)

print("\nContoh 4") #count
D = [1, 2, 3, 'a', 'c', 1]
print(D.count(1))

print("\nContoh 5") #extend
X = [1, 2, 3]
print(X)
Y = ['x', 'y', 'z']
X.extend(Y)
print(X)
A = [1, 2, 3]
B = ['x', 'y', 'z']
print(A+B)

print("\nContoh 6") #index
X = [10, 20, 30, 'a', 2023]
print(X.index('a')) #mengembalikan index pertama dari 'a'
Y = [1, 2, 3, 10, 2, 20]
print(Y.index(2))