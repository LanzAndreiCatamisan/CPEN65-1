import math

while True:
  Method = float(input("What is your given for solving the area of circle? "
                       "Enter 1 for radius and 2 for diameter:"))
  if Method == 1:
    radius1 = float(input("Enter the radius:"))
    area1 = math.pi * radius1 *radius1
    print(area1)
    break
  elif Method == 2:
    radius2 = float(input("Enter the diameter:"))
    area2 = math.pi * ((radius2 * radius2) / 4)
    print(area2)
    break
  else:
   print("Enter Again")

