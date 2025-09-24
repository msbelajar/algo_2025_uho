#menentukan input merupakan kelipatan 2, 3 atau keduanya
x = int(input())

if x%2 == 0 and x%3 == 0:
    print(f"{x} merupakan bilangan kelipatan 2 dan 3")
elif x%2 == 0:
    print(f"{x} merupakan bilangan kelipatan 2")
elif x%3 == 0:
    print(f"{x} merupakan bilangan kelipatan 3")
else:
    print(f"{x} bukan merupakan kelipatan 2 atau 3")