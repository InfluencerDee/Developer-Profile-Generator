#A terminal-based app that asks a user for their personal dev info, stores it
import random

print("👋 Welcome, Developer! Let's build your profile.\n")

# Get developer's input
dev_name = input("Enter your name: ").capitalize()
dev_age = input("Enter your age: ")
dev_skill = input("Enter your skill level (Beginner/Intermediate/Advanced): ").capitalize()
dev_gender = input("Enter your gender: ").capitalize()
dev_languages = input("Enter the languages you know (separated by commas): ").split(',')

# Clean up whitespace in languages
dev_languages = [lang.strip().capitalize() for lang in dev_languages]

#Stores data in a dictionary
dev_keys_lst = ["Name", "Age", "Skill Level", "Gender", "Language(s)"]
dev_values_lst = [dev_name, dev_age, dev_skill, dev_gender, dev_languages]
dev_dct = dict(zip(dev_keys_lst, dev_values_lst))

#Outputs a nicely formatted string summary
print("Here's your Dev Profile: \n")

for key, value in dev_dct.items():
    print(f"{key}: {value}")

#Saves the summary to a text file
with open ('../First-Python-Project/dev_profile.txt', 'w') as file:
    file.write("Dev Profile\n")
    for key, value in dev_dct.items():
        file.write(f"{key}: {value}\n")

#Randomly suggests next steps from a list
print("\n Suggested next steps: \n")

next_steps_lst = [
    "Learn Git branching",
    "Try building a simple calculator GUI",
    "Explore Python OOP",
    "Contribute to an open-source project",
    "Build a portfolio site"
]

print(random.choice(next_steps_lst))










