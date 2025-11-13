#contoh set
A = {1, 3, 5, 7, 9}
#print(A)

#contoh List
B = [1, 1, 3, 4] #anggota yang sama bisa lebih dari 1

#contoh set
C = {1, 3, 5, 7, 9, 11} 
# print(C)
C.add(2)
# print(C)

#contoh gabungan
print("\nGabungan")
A = {1,3,4}
B = {1,2,5}
gabungan = A.union(B)
print(gabungan)

#contoh irisan
print("\nIrisan")
A = {1,3,5,8}
B = {3,5,10}
irisan = A.intersection(B)
print(irisan)

#contoh selisih (difference)
print("\nContoh difference")
A = {1,3,5,7}
B = {3,5,10,11}
selisihAB = A.difference(B)
print(selisihAB)

#beda simetri
print("\nBeda simetri")
A = {1,3,5,7,9}
B = {1,5,9,11,13}
bedasimetri = A.symmetric_difference(B)
print(bedasimetri)