from sympy import Point, Line 
p1, p2, p3 = Point(1, 0), Point(1, 1), Point(3, 3)
l1 = Line(p1, p2)

print(p3.distance(l1))