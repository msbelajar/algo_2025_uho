#fungsi tanpa parameter
def halo():
    print("Halo UHO")

#fungsi dengan parameter
def haloNama(nama):
    print(f"Halo {nama}")

#fungsi menghitung luas lingkaran
def lingkaran(r):
    L = 3.1415 * r**2
    print(f"Lingkaran jari-jari {r}")
    print(f"Luas = {L}")

def fufufafa(x,y):
    a = 5*x + 4*y
    c = 50 + a
    if c >= 100:
        r = 2*c + 10
    else:
        r = 3*c - 10
    print(f"r = {r}")

halo()
haloNama("iman")
lingkaran(1)
fufufafa(2,4) # x=2, y=4
fufufafa(y=0,x=0) #jika menggunakan keyparameter bisa dibalik