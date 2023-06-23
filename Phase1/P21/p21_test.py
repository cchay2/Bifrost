import unittest
import p21

class TestApi(unittest.TestCase):
	# Testing Framework
	def test_deliverable_management(self):
		p21.Deliverable_Management()

	# Following tests should use this format
	#def test_list_int(self):

if __name__ == '__main__':
	unittest.main()