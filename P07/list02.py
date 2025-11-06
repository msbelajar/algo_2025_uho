#akses anggota list menggunakan bilangan bulat
print("Contoh 1")
C = [1, 3, 5, 7, 9]

print(f'C = {C}')
print(f'C[0] = {C[0]}')
print(f'C[1] = {C[1]}')
print(f'C[4] = {C[4]}')
# print(C[5]) #error 

#nested list
print("\nContoh 2")
D = ['a', [True, 2023], 'u', [1, 2]]

print(f'D = {D}')
print(f'D[1][0] = {D[1][0]}')
print(f'D[3][1] = {D[3][1]}')

#indeks negatif
print("\nContoh 3")
X = [1, 3, 5, 7, 9, 11, 13, 15]

print(f'X = {X}')
print(f'X[-1] = {X[-1]}') #item terakhir pertama
print(f'X[-2] = {X[-2]}') #item terakhir kedua

#slice list
print("\nContoh 4")
X = [1, 3, 5, 7, 9, 11, 13, 15]

print(f'X = {X}')
print(f'X[0:2] = {X[0:2]}') # mulai X[0] sampai X[2-1]
print(f'X[:2] = {X[:2]}') # semua dari kiri sampai X[2-1]
print(f'X[3:] = {X[3:]}') # mulai dari X[3] sampai ke kanan
print(f'X[-3:] = {X[-3:]}') #3 item terakhir
print(f'X[:-3] = {X[:-3]}') # mulai dari kiri tidak lewat dari item 3 terakhir
print(f'X[-4:-1] = {X[-4:-1]}') #mulai dari item ke 4 terakhir sampai 2 terakhir