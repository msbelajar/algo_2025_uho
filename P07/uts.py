def F4(x,y):
    print("=== F4 ===")
    m = 3
    m += 2*m + 3
    print(f"m = {m}")
    print(f"x-y-m = {x-y-m}")
    
def F5(x,y):
    print("=== F5 ===")
    if x>=5 or y<3:
        c = x+y-5
    else:
        c = x+y+5
    print(f"c = {c}")
    

F4(2,4)
F5(2,4)