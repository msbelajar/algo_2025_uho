#keyword return
def F1(x):
    c = x**2 + x + 2
    R = x**3
    Z = 2*x
    return c #mengembalikan nilai fungsi = c

def F2(t):
    c = t**2 + 1
    print("ccccccccc")
    return c #mem-break alur fungsi
    print("Haloo c")
    print("EXIT")

nilai = F1(2)
print(nilai)
u = F2(0)
print(u)