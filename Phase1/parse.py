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