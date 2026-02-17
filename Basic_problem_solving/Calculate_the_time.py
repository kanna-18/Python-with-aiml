def calculate_the_time(u):
    T=2*u/g
    return T
u = float(input("enter intial velocity"))
g = 9.8
v =calculate_the_time(u)
print("The time taken to touch the ground ",v)
