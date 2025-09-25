# mengecek nilai yang diinput antara 10 dan 20 (inklusif)

x = input("Masukkan nilai x = ")
x = float(x)

if x>=10 and x<=20:
    print("Nilai dalam selang 10 <= x <= 20")
else:
    print("Nilai di luar selang 10 <= x <= 20")