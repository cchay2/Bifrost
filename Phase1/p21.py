from canvasapi import Canvas
from dotenv import load_dotenv
import os
import parse
import sys

load_dotenv()
current_path = os.getcwd()

# personal access token and url for dashboard
dashboard_url = os.getenv("canvas_dashboard_url") 
access_token = os.getenv("canvas_access_token") # new token needed per user

# Put the following line inside of canvas.get_courses() :
# enrollment_state="active"

def Deliverable_Management():
    canvas = Canvas(dashboard_url, access_token) # Canvas object to access student academic information 
    courses = canvas.get_courses(enrollment_state="active") # grabs a list of all pre-enrolled and enrolled courses in user's account

    # After program is run, list will be full of the individual assignments & quizzes
    master_list = []

    # size = os.path.getsize(current_path+"/../P21/academic_deliverables.txt")

    # file = open("academic_deliverables.txt", "a")
    # file.close()
    
    # grabs all assignments and quizzes per course
    for course in courses:
        try:
            assignments = course.get_assignments()
            for assignment in assignments:
                try:
                    # assigning a_info as a string with course, assignment, and due date:
                    a_info = (f"{course} | {assignment} | {assignment.due_at}")
                    parsed_a = parse.parseAssignment(a_info)

                    # adding each new assignment into the master list
                    if a_info not in master_list:
                        master_list.append(str(a_info))
                    else:
                        pass

                except:
                    pass

            quizzes = course.get_quizzes()
            for quiz in quizzes:
                try:
                    # assigning a_info as a string with course, quiz, and due date:
                    q_info = (f"{course} | {quiz} | {quiz.due_at}")
                    parsed_q = parse.parseAssignment(q_info)

                    # adding each new quiz into the master list
                    if q_info not in master_list:
                        master_list.append(q_info)                    
                    else:
                        pass

                except:
                    pass

        except:
            pass

    return master_list
