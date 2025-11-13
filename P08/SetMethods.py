#contoh gabungan
print("\nGabungan")
A = {1,3,4}
B = {1,2,5}
gabungan = A | B
print(gabungan)

#contoh irisan
print("\nIrisan")
A = {1,3,5,8}
B = {3,5,10}
irisan = A & B
print(irisan)

#contoh selisih (difference)
print("\nContoh difference")
A = {1,3,5,7}
B = {3,5,10,11}
selisihAB = A - B
print(selisihAB)

#beda simetri
print("\nBeda simetri")
A = {1,3,5,7,9}
B = {1,5,9,11,13}
bedasimetri = A ^ B
print(bedasimetri)