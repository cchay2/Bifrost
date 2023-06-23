import unittest, sys, os
import trello
from dotenv import load_dotenv

current_path = os.getcwd()
sys.path.append(current_path+'/../Trello')
import connection

sys.path.append(current_path+'/../P21')
import p21

class TestApi(unittest.TestCase):
	# Testing Framework
	def test_card_creation(self):
		load_dotenv()

		API_KEY = os.getenv("TRELLO_API_KEY")
		TOKEN = os.getenv("TRELLO_TOKEN")

		client = trello.TrelloClient(
		api_key = API_KEY,
		token = TOKEN
		)

		board_name = "2023 Fall Semester"
		list_name = "Bifrost Gateway"
		card_name = "CS 110 - Lab 1 - 2023.09.17"
		con = connection
		card = con.create_card(board_name, list_name, card_name)

		b_name = board_name

		boards = client.list_boards()
		for board in boards:
			if board.name == b_name:
				b_id = board.id
				break

		board = client.get_board(b_id) ## Pass in Board id, not board name

		l_name = list_name

		l_id = 0
		for lst in board.list_lists():
			if lst.name == l_name:
				l_id = lst.id
				break

		if l_id == 0:
			print("List not found! Error")
			assert(False)
		else:
			l_obj = board.get_list(l_id) ## Pass in List id, not list name



		for c in l_obj.list_cards():
			self.assertEqual(card_name, c.name)
			c.delete()

	def test_parse_assignment(self):
		string = "NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Submit Your Immunization Records- Mandatory (Time to complete varies)  Fall 2023 (10756587) | 2023-08-02T03:59:59Z"
		con = connection
		parsed_list = con.parseAssignment(string)
		self.assertEqual(parsed_list, ['ADV ORIENT', 'NOVA ADVANCE Orientation', '2023-08-02', 'Submit Your Immunization Records- Mandatory'])

	def test_deliverable_management(self):
		deliverables = p21.Deliverable_Management()
		self.assertEqual(deliverables, ['NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Activate Your Patriot Pass Account- Mandatory (15 min to complete) (8865905) | 2023-08-02T03:59:59Z', 'NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Activate Your Patriot Pass Account- Mandatory (15 min to complete) Due by January 5th, 2023 (10756575) | 2023-08-02T03:59:59Z', 'NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Access your Mason Live Email - Mandatory (5 mins to complete)  (8865910) | 2023-08-02T03:59:59Z', 'NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Submit Your Immunization Records- Mandatory (Time to complete varies)  (8865911) | 2023-08-02T03:59:59Z', 'NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Career Readiness Guide (30 mins-1hr to complete)  (8865921) | None', 'NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Mason Campus Virtual Tour  (8865927) | None', 'NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Activate Your Patriot Pass Account- Mandatory (15 min to complete) Fall 2023 (10756585) | 2023-08-02T03:59:59Z', 'NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Access your Mason Live Email - Mandatory (5 mins to complete)  Fall 2023 (10756586) | 2023-08-02T03:59:59Z', 'NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Submit Your Immunization Records- Mandatory (Time to complete varies)  Fall 2023 (10756587) | 2023-08-02T03:59:59Z'])

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