x = float(input("Masukkan harga = Rp "))
if x > 100000 :
    diskon = 0.05 * x
    print(f"harga setelah diskon = Rp {x-diskon}")
else:
    print("tidak dapat diskon")
    print(f"harga = Rp {x}")