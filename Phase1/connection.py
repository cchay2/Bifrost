from dotenv import load_dotenv
import os
import trello
import sys


load_dotenv()

API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")

##print("API KEY:", API_KEY)

client = trello.TrelloClient(
	api_key = API_KEY,
	token = TOKEN
	)
print("Successful API Connection")

def create_card( board_name="2023 Fall Semester", list_name="Bifrost Gateway", card_name="CS 110 - Lab 1 - 2023.09.17" ):
	try:
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

			#card_name = "CS 110 - Lab 1 - 2023.09.17"
			new_card = l_obj.add_card(name=card_name, desc=None)
			return "Pass"

	except trello.exceptions.ResourceUnavailable as e:
		print("Error:", e)


def parseAssignment( string ):
	string = string.split(" ") 
	new_return = []
	course_id = string[0].split(".")
	course_id = course_id[1] + " " + course_id[2]
	new_return.append(course_id) #Course ID

	end_index = 0 ## Get the course name
	for i in range(1, 10):
		if string[i][0] == "(":
			break
		else:
			end_index = i+1
	course_name = ""
	for i in range(1, end_index):
		course_name = course_name + string[i]
		course_name += " "
	course_name = course_name.strip(" ")
	new_return.append(course_name)

	time = string[-1][0:10] # Get the Due Date
	new_return.append(time)

	description = ""
	index = 0
	for i in string:
		if i == "|":
			index += 1
			for i in range(index, len(string)):
				if "(" in string[i]:
					break
				description += string[i] + " "
			break
		else:
			index += 1
	description = description.strip(" ")
	new_return.append(description)

	# print(new_return)
	return new_return


#parseAssignment("NV280.ADV.ORIENT.ORG NOVA ADVANCE Orientation (265271) | Submit Your Immunization Records- Mandatory (Time to complete varies)  Fall 2023 (10756587) | 2023-08-02T03:59:59Z")
#parseAssignment("NV280.MTH.263.001A.SP21 (Spring 2021) MTH 263 (001A) - Calculus I (356246) | Homework, Ch 1 - 2 (7484534) | None")

def backlog_flush( board_name, list_name, academics ):
	"""Empties the entire Backlog List in the specified board and repopulates it with the given deliverables"""
	try:
		boards = client.list_boards()
		for board in boards:
			if board.name == board_name:
				board_id = board.id
				break

		board = client.get_board(board_id)

		list_id = 0
		for lst in board.list_lists():
			if lst.name == list_name:
				list_id = lst.id
				break

		if list_id == 0:
			print("Error! List not found!!")
			return
		else:
			list_obj = board.get_list(list_id) ## Pass in List id

		#print("List Object:", list_obj)
		# if list_obj:
		# 	for card in list_obj.list_cards():
		# 		card.delete()
		# 		print("Deleted Card:", card.name)
		# else:
		# 	print("List not found")
		# if len(list_obj.list_cards()) != 0:
		# 	return None

		#for academic in academics:
	except trello.exceptions.ResourceUnavailable as e:
		print("Error:", e)

	#print("Pass")

	try:
		print("Locating academic_deliverables.txt...")
		file = open("academic_deliverables.txt", "r")
		file.close()
	except:
		print("File not found. Creating academic_deliverables.txt...")
		file = open("academic_deliverables.txt", "x")
		file.close()
	else:
		print("academic_deliverables.txt located...")

	for academic in academics:
		# print("THERE IS AN ACADEMIC, YOUNGER BROTHER")
		parsed = parseAssignment( academic )
		assignment_class = parsed[0]
		assignment_class_full = parsed[1]
		if parsed[2] == None:
			assignment_date = "No Due Date"
		else:
			assignment_date = parsed[2]
		assignment_description = parsed[3]

		card_title = assignment_class + " - " + assignment_description + " - " + assignment_date
		
		file = open("academic_deliverables.txt", "r")
		file_content = file.readlines()
		file.close()

		#print("File Content: ", file_content)
		
		if f"{card_title}\n" not in file_content:
			list_obj.add_card(name=card_title, desc=None)
			#print("Creating")
			with open("academic_deliverables.txt", "a") as file:
				file.write(f"{card_title}\n")
		elif f"{card_title}\n" in file_content:
			#print("Passing")
			pass


	return "Pass"