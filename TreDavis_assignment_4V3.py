student_name = "Tre Davis"
current_gpa = 4.0
study_hours = 25
social_points = 50
stress_level = 80

if Course_load == "Type 1":
    if current_gpa <= 2.5:
        study_hours = 15
        stress_level = 45
        social_points = 80
        print(f"you have choosen Light work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
        print("Consider taking a bigger work load")
        print("Low GPA")
    elif current_gpa > 2.5:
        stress_level = 30
        social_points = 85
        study_hours = 10
        print(f"you have choosen Light work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
    elif current_gpa >= 3.8:
        stress_level = 25
        social_points = 90
        study_hours = 6
        print(f"you have choosen Light work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
elif Course_load == "Type 2":
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
    elif current_gpa >= 3.8:
        study_hours = 14
        stress_level = 45
        social_points = 78
        print(f"you have choosen Medium work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
elif Course_load == "Type 3":
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
    elif current_gpa >= 3.8:
        study_hours = 30
        stress_level = 88
        social_points = 40
        print(f"you have choosen Heavy work load. Study at least {study_hours} hours a week, your stress level is {stress_level}, your social level is {social_points}")
if current_gpa >= 3.8:
    print("Good job")
elif current_gpa <= 3.0:
    print("Study harder")

else:
    print("Invalid GPA")

Study_option = ["Programming","Math", "English", "History"]
print("Programming, Math, English, History")

choice1 = input("Enter a study subject")

if choice1 in Study_option:
    if (current_gpa > 2.5) and (stress_level > 50):
        if (choice1 == "Programming") or (choice1 == "Math"):
            stress_level = 80
            social_points = 50
            print("You have alot to study you need to get on ASAP, But you can do it your GPA High enough ")
        if (choice1 == "English") or (choice1 == "History"):
            stress_level = 70
            social_points = 60
            print("You have alot of reading to do GOODLUCK! But your GPA High enough you can do it")
    if (current_gpa <= 2.5)
        if (choice1 == "Programming") or (choice1 == "Math"):
            stress_level = 90
            social_points = 40
            print("You have alot to do and catch up on consider taking in a higher work load")

   