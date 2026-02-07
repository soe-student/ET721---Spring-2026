import math

def area_rectangle(length, width):
    return length * width   

def print_area_result(width, length, area):
    print(f"Area of rectangle (length={length}, width={width}): {area}")

#example 2: calculate the distane of two points
def collectnum():
    num = float(input("Enter a number: "))
    while (num < 1 or num > 100):
        num = float(input("Invalid input. Enter a number between 1 and 100: "))
    return num

# distance = square_root of ( (x2 - x1)^2 + (y2 - y1)^2 )
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# print result
def print_distance_result(x1, y1, x2, y2, distance):
    print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}): {distance}\n")


# Exercise