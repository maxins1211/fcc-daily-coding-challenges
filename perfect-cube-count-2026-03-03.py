# Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

# The lower number is not garanteed to be the first argument.
# A number is a perfect cube if there exists an integer (n) where n * n * n = number.
# For example, 27 is a perfect cube because 3 * 3 * 3 = 27.

# 1. count_perfect_cubes(3, 30) should return 2.
# 2. count_perfect_cubes(1, 30) should return 3.
# 3. count_perfect_cubes(30, 0) should return 4.
# 4. count_perfect_cubes(-64, 64) should return 9.
# 5. count_perfect_cubes(9214, -8127) should return 41.
def count_perfect_cubes(a:int, b:int) -> int:
    if (a > b):
        a,b = b,a
    start: int = cube_root(a)
    end: int = cube_root(b) 
    counter: int = 0
    for i in range (start,end + 1):
        if(i**3 >=a and i**3 <=b):
            counter+=1
    return counter

def cube_root(n:int) -> int:
    if n >= 0:
        return int(n**(1/3))
    else:
        return -int((-n)**(1/3))