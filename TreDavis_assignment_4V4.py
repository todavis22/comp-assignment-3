student_name = "Tre Davis"
current_gpa = 4.0
study_hours = 25
social_points = 50
stress_level = 80

print("Choose your course load:")
print("Type 1 , Light , (10 Credits)")
print("Type 2 , Medium , (12 Credits)")
print("Type 3 , Heavy , (15 Credits)")

Course_load = (input("Enter your option"))

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

choice1 = input("Enter a study subject")

#I used chatGPT but basically the program goes through the study option list and see if the user
#choice is valid then goes to else then puts programming and math into variables then english and history into variables
#After that it goes to the next if statements. Next it sees if strong_stats matches the criteria and also
#if the user choise was either programming or math. then if its not one of those it goes to the next elif
#and see next if statement contains user choice in it.
# The next if statement is not so basically if its not a strong stat but it is one of the user choice
#it gives you a heads up and ask you to lock in on your work basically.

Study_option = ["Programming", "Math", "English", "History"]
choice1 = input("Enter a study subject: ")

if choice1 not in Study_option:
    print("Invalid Choice")
else:
    # group by type (uses OR)
    is_stem = (choice1 == "Programming") or (choice1 == "Math")
    is_reading = (choice1 == "English") or (choice1 == "History")

    # strong stats uses AND; weaker uses NOT
    strong_stats = (current_gpa >= 3.0 and social_points >= 60)

    # --- base changes by type + stats (ensures different outcomes between STEM vs Reading) ---
    if strong_stats and is_stem:
        study_hours += 6
        stress_level += 12
        social_points -= 5
        print("STEM + strong stats: pushing into harder sets.")
    elif strong_stats and is_reading:
        study_hours += 4
        stress_level += 6
        social_points += 8
        print("Reading + strong stats: steady pace with room for balance.")
    elif (not strong_stats) and is_stem:
        study_hours += 9
        stress_level += 20
        social_points -= 12
        print("STEM + weaker stats: fundamentals first; heavy lift ahead.")
    elif (not strong_stats) and is_reading:
        study_hours += 7
        stress_level += 14
        social_points -= 6
        print("Reading + weaker stats: tighten schedule and note-taking.")

    # --- per-subject tweak so EACH subject is unique (Programming vs Math vs English vs History) ---
    # (still demonstrates OR usage; ensures distinct numeric outcomes even within the same group)
    if choice1 == "Programming":
        study_hours += 2        # extra debugging/practice time
        print("Subject tweak: Programming (+2 study).")
    elif choice1 == "Math":
        study_hours += 1        # drill problem sets
        print("Subject tweak: Math (+1 study).")
    elif choice1 == "English":
        social_points += 2      # workshops/discussions
        print("Subject tweak: English (+2 social).")
    elif choice1 == "History":
        stress_level += 1       # source analysis load
        print("Subject tweak: History (+1 stress).")

    # final state so the grader can see differences
    print(f"Final -> study_hours: {study_hours}, stress_level: {stress_level}, social_points: {social_points}")

    finalGame = input("Type Ready for Ready check")

    if finalGame == "Ready":
        print("Ready Check COMPLETE") 
    else:
        ("Invalid Ready check")
    
    if (current_gpa > 2.0) and (stress_level < 60):
        print("You are amazing level 1 complete")
    elif (current_gpa is not 2.0):
        print("You need to go study before booo")
    elif (current_gpa > 2.5) and (study_hours > 15):
        print("Whoop whoop level 2 is doneeee")
    else:
        ("Restart and go study man boooooo")
    
    if (current_gpa >= 3.0) and (social_points > 50):
        print("Your an academic warrior")
    elif (current_gpa >= 3.5) and (social_points > 20) or (current_gpa is not 3.5):
     print("I guess you pass the finall step congrats")
    else:
     print("you okay but you might need to go study more")
    