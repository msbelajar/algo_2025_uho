n = float(input("Nilai = ")) # n = nilai

#asumsikan nilai yang diinput bisa negatif atau > 100
if n<0 or n>100:
    print('Error!!! Input nilai >= 0 atau <= 100')
else:
    if n>=81:
        print('Nilai huruf A')
    elif n>=66:
        print('Nilai huruf B')
    elif n>=51:
        print('Nilai huruf C')
    elif n>=36:
        print('Nilai huruf D')
    else:
        print("Nilai huruf E")