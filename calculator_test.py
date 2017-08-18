#test file for calculator.py
#For donesafe coding test
#written by Nathaniel Henry

#program should be in the same directory as calculator.py
#no arguments are required

import unittest
from calculator import *

import json
import sys
from datetime import *
import re

class TestMethods(unittest.TestCase):
	def test_getWeeks(self):
		self.assertEqual(getWeeks("2017/08/18", datetime(2017,8,18)), 0) #same day
		self.assertEqual(getWeeks("2017/07/18", datetime(2017,8,18)), 4)
		self.assertEqual(getWeeks("2016/08/18", datetime(2017,8,18)), 52)
		self.assertEqual(getWeeks("2018/08/18", datetime(2017,8,18)), 0) #a future date
		self.assertEqual(getWeeks("2015/07/18", datetime(2017,8,18)), 108)

	def test_getPay(self):
		rules = [{u'applicableWeeks': u'1-26', u'overtimeIncluded': True, u'percentagePayable': 90}, 
		        {u'applicableWeeks': u'26-52', u'overtimeIncluded': True, u'percentagePayable': 80}, 
		        {u'applicableWeeks': u'53-79', u'overtimeIncluded': True, u'percentagePayable': 70},
		        {u'applicableWeeks': u'80-104', u'overtimeIncluded': False, u'percentagePayable': 60}, 
		        {u'applicableWeeks': u'104+', u'overtimeIncluded': False, u'percentagePayable': 10}]

		self.assertEqual(getPay(0, 0,0,rules), 0)
		self.assertEqual(getPay(100,200,20,rules), 270)
		self.assertEqual(getPay(1000,2500,0,rules), 0)
		self.assertEqual(getPay(75.0030*35.0,150.0*7.3,54,rules), 2604.0735)
		self.assertEqual(getPay(1500,200,500,rules), 150)
		self.assertEqual(getPay(1500,200,56,rules), 1190)

if __name__ == '__main__':
	unittest.main()