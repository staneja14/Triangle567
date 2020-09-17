# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidTriangles(self):
        self.assertEqual(classifyTriangle(1, 3, 5), 'NotATriangle', '1,3,5 is not a Triangle')

    def testInvalidTrianglesB(self):
        self.assertEqual(classifyTriangle(1, 4, 5), 'NotATriangle', '1,4,5 is not a Triangle')

    def testInvalidTrianglesC(self):
        self.assertEqual(classifyTriangle(1, 0, 1), 'NotATriangle', '1,0,1 is not a Triangle')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral triangle')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral', '3,3,3 should be Equilateral triangle')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(5, 5, 1), 'Isoceles', '5,5,1 should be Isosceles Triangle')

    def testIsocelesTriangles2(self):
        self.assertEqual(classifyTriangle(5, 1, 5), 'Isoceles', '5,1,5 should be Isosceles Triangle')

    def testIsocelesTriangles3(self):
        self.assertEqual(classifyTriangle(1, 5, 5), 'Isoceles', '1,5,5 should be Isosceles Triangle')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5, 7, 3), 'Scalene', '5,7,3 should be Scalene Triangle')

    def testScaleneTriangles2(self):
        self.assertEqual(classifyTriangle(10, 8, 5), 'Scalene', '10,8,5 should be Scalene Triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
