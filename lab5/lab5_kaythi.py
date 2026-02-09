"""
Soe Kaythi
Feb 5, 2026
Lab 5, Functions
"""

from lab5_function_kaythi import *
print(f"Area of rectangle (5, 10): {area_rectangle(5, 10)}")

print("\n---Example 1: User-defined function---")  
width = 8
length = 12
area = area_rectangle(length, width)
print_area_result(width,length,area)

print("\n---Example 2: Collect number between 1 and 10---")
x1 = collectnum()
x2 = collectnum()
y1 = collectnum()
y2 = collectnum()
#print(f"You entered points: ({x1}, {y1}) and ({x2}, {y2})\n")
#print(f"Distance between two points: {calculate_distance(x1, y1, x2, y2)}\n") 
print_distance_result(x1, y1, x2, y2, calculate_distance(x1, y1, x2, y2))

print("\n---Exercise---\n")
number = generate_random(1, 10)
print("Random number:", number)
compare_number(number)