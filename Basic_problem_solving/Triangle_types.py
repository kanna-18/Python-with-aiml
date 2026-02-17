angle1=int(input("enter the angle"))
angle2=int(input("enter the angle"))
angle3=180-(angle1+angle2)
if angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("The triangle is Right-angled.")
elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is scalar.")
