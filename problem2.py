#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

'''
If a2+b2=c2

then the triangle is right.

If a2+b2<c2

then the triangle is obtuse (assuming the sides actually form a triangle.)

If a2+b2>c2
then the triangle is acute.
'''
'''
a+b > c

b+c > a

c+a > b
'''
def triangle(a,b,c):
    y = 0
    x = 0
    z = 0
    TriList = [a,b,c]
    TriList.sort()
    if (((TriList[0] ** 2) + (TriList[1] ** 2)) ** (1/2)) == TriList[2]:
        return 2
    if (((TriList[0] ** 2) + (TriList[1] ** 2)) ** (1/2)) > TriList[2]:
        return 1
    if (((TriList[0] ** 2) + (TriList[1] ** 2)) ** (1/2)) < TriList[2]:
        if a + b > c:
            x = 1
        if b + c > a:
            y = 1
        if c + a > b:
            z = 1
        if x == 1 and y == 1 and z == 1:
            return 3
        else:
            return 0

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
