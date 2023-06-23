import unittest, sys, os

#current_path = os.getcwd()
#sys.path.append(current_path+'/../Trello')
import connection

#sys.path.append(current_path+'/../P21')
import p21

class TestApi(unittest.TestCase):
	# Testing Framework
	def test_card_creation(self):
		con = connection
		card = con.create_card("2023 Fall Semester", "Backlog", "CS 110 - Lab 1 - 2023.09.17")
		self.assertEqual(card, "Pass")


	def test_full_update(self):
		#warnings.filterwarnings("ignore", category=ResourceWarning)
		deliverables = p21.Deliverable_Management()
		con = connection

		status = con.backlog_flush("2023 Fall Semester", "Bifrost Gateway", deliverables)
		self.assertEqual( status, "Pass" )


	# Following tests should use this format
	#def test_list_int(self):

if __name__ == '__main__':
	unittest.main()



## Comments for the Demo
# 2023.06.04
# Slow down and speak slowly
# Do not assume that the user knows the system as well as the developer
# Present all the related information together so the customer can understand and follow along
# Can split up the work among multiple people, 1 person preson and someone else run the command

# Can create as many feature branches as needed
# Create a release branch where the testing for all the related code is done.

# Make test cases, with acceptance criteria and use cases


# New use case
# User feedback: Date can be turned into trello card due date



## Agile project management model
# Envisioning
#	Envision what the product is gonna be
# Speculating
#	Start thinking about how to implement different features and functionalities
# Exploring
#	Performing iterations of learning. Develop code and software and testing + getting feedback.
# Adapting
#	Adapt and change plan as you learn
# Closing
#	Closing the whole project

## Charting a project
# Charter
# 	Makes clear how it will affect and benefit the entire team
# Vision statement -> Defines the why of the Charter
# 	How a product will add value and motivate the dev team
# 
# include risk management, team roles, success conditions, problems
# 
# 
# 
# 
# 
# 
# 
# 