#!/usr/bin/python3
"""
Unittest for the 'Base' class.
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
	"""Tests the 'Base' class.

	Args:
		unittest (class): unittest
	"""

	def test_constructor(self):
		"""Tests the constructor of the 'Base' class."""
		obj = Base()
		obj2 = Base()
		self.assertIsInstance(obj, Base)
		self.assertEqual(obj.id, 1)
		self.assertEqual(obj2.id, 2)

	def test_constructor_with_id(self):
		"""Tests the class contstructor with attribute 'id'."""
		obj = Base(5)
		obj2 = Base(27)
		self.assertEqual(obj.id, 5)
		self.assertEqual(obj2.id, 27)

if __name__ == "__main__":
	unittest.main()