import connection, p21

print("Running...")
deliverables = p21.Deliverable_Management()
connection.backlog_flush("2023 Fall Semester", "Bifrost Gateway", deliverables)
print("Program complete. Deliverables stored and pushed to Gateway.")
input("<Enter to Quit>")