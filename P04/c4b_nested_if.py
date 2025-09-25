#menentukan bilangan termasuk genap positif/negatif, ganjil positif/negatif, nol
x = int(input())

if x%2 == 0:
    if x == 0:
        print("nol")
    else:
        if x > 0:
            print(f"{x} bilangan genap positif")
        else:
            print(f"{x} bilangan genap negatif")
else:
    if x > 0:
        print(f"{x} bilangan ganjil positif")
    else:
        print(f"{x} bilangan ganjil negatif")