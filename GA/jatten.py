n, m = map(int, input().split())
    
if n <= 1 and m <= 1: 
    exit()
    
line = input().split()
x1, y1, x2, y2 = map(int, line)

x_center_point = (x1 + x2)//2
y_center_point = (y1 + y2)//2

predefined_points = [
    (0, m-1),
    (n-1, 0),
    (n-1, m-1),
    (0, 0),
    (x_center_point, y_center_point + 1),
    (x_center_point, y_center_point - 1),
    (x_center_point + 1, y_center_point + 1),
    (x_center_point - 1, y_center_point + 1),
    (x_center_point - 1, y_center_point - 1),
    (x_center_point + 1, y_center_point - 1),
]

for x, y in predefined_points: 
    if 0 <= x < n and 0 <= y < m:
        a = (x2 - x1) ** 2 + (y2 - y1) ** 2
        b = (x - x1) ** 2 + (y - y1) ** 2
        c = (x - x2) ** 2 + (y - y2) ** 2
    
        # if (y - y1) * (x2 - x1) != (x - x1) * (y2 - y1):
        #if (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) != 0:
        if (x - x1) * (y - y2) - (y - y1) * (x - x2) != 0:
            if (a > c + b) or (b > a + c) or (c > a + b):
                print(int(x), int(y))
                break
    else:
        continue