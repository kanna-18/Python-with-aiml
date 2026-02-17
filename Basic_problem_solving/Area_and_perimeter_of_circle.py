def Area_and_perimeter_of_circle(r):
    area=3.14*r**2
    perimeter=2*3.14*r
    return (area,perimeter)
r=int(input("enter a num"))
c=Area_and_perimeter_of_circle(r)
print(c)
