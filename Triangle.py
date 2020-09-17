# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    instance_list = [isinstance(a, int), isinstance(b, int), isinstance(c, int)]
    if (max(a, b, c) > 200 or
            min(a, b, c) < 0 or
            not instance_list):
        return 'InvalidInput'

    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if ((a >= (b + c)) or
            (b >= (a + c)) or
            (c >= (a + b))):
        return 'NotATriangle'

    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif ((((a ** 2) + (b ** 2)) == (c ** 2)) or
          (((a ** 2) + (c ** 2)) == (b ** 2)) or
          (((c ** 2) + (b ** 2)) == (a ** 2))):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    return 'Isoceles'
