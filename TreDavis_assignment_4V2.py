student_name = "Tre Davis"
current_gpa = 4.0
study_hours = 25
social_points = 50
stress_level = 80

print("Choose your course load:")
print("Type 1 , Light , (10 Credits)")
print("Type 2 , Medium , (12 Credits)")
print("Type 3 , Heavy , (15 Credits)")

Course_load = int(input("Enter your option"))

if Course_load == 1:
    if current_gpa <= 2.5:
        study_hours = 15
        stress_level = 45
        social_points = 80
        print(f"you have choosen Light work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
        print("Consider taking a bigger work load")
    elif current_gpa >= 2.5:
        stress_level = 30
        social_points = 85
        study_hours = 10
        print(f"you have choosen Light work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
if Course_load == 2:
    if current_gpa < 3.0:
        study_hours = 18
        stress_level = 67
        social_points = 73
        print(f"you have choosen Medium work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
    elif current_gpa >= 3.0:
        study_hours = 16
        stress_level = 55
        social_points = 76
        print(f"you have choosen work Medium work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
if Course_load == 3:
    if current_gpa <= 3.5:
        study_hours = 20
        stress_level = 70
        social_points = 65
        print(f"you have choosen Heavy work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
    elif current_gpa > 3.5:
        study_hours = 25
        stress_level = 80
        social_points = 50
        print(f"you have choosen Heavy work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
    else:
        print("Invalid GPA")

    


