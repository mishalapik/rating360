# add root directory to path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import backend.sheets_functions as sheets_functions


user_input: str = input("Enter team name: ")
result = sheets_functions.check_team(user_input)
print(result)