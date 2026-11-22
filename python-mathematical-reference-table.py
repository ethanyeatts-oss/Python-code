
import math

start = int(input("Enter the starting integer (default = 1): ") or 1)
end = int(input("Enter the ending integer (default = 10): ") or 10)

for i in range(start, end + 1):
    square = i ** 2
    square_root = math.sqrt(i)
    cube_root = i ** (1 / 3)

    print(f"{i:3d}    {square:12,d}    {square_root:7.3f}    {cube_root:7.3f}")
