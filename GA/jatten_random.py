import random

n, m = map(int, input().split())
    
if n <= 1 and m <= 1:
    exit()
    
line = input().split()
x1, y1, x2, y2 = map(int, line)

distance_between_legs = (x2 - x1) ** 2 + (y2 - y1) ** 2

while True:
    px = random.randint(0, n-1) 
    py = random.randint(0, m-1)
    
    a = distance_between_legs
    b = (px - x1) ** 2 + (py - y1) ** 2
    c = (px - x2) ** 2 + (py - y2) ** 2
    
    # Triangle is obtuse if the square of one side is greater than
    # the sum of the squares of the other two sides.
    if (a > c + b) or (b > a + c) or (c > a + b):
        # Ensure the three points are not collinear.
        if (py - y1) * (x2 - x1) != (px - x1) * (y2 - y1):
            print(px, py)
            break