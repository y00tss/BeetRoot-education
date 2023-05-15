import json
import os

# creating additional directory with OS

directory_target = "C://Users//Mykhailo//Desktop//Python//BeetRoot-education//lesson_10//homework//task_1//additional_directory"
if not os.path.exists(directory_target):
    os.makedirs(directory_target)

# Main task. Creating file and adding info into it

with open("myfile.txt", "w") as file:
    file.write("Hello file world!")

# Main task. Reading file
with open("myfile.txt", "r") as file:
    text = file.readline()
    print(text)

# additional task

add_file = os.path.join(directory_target, "additional_directory/myfile2.txt")
with open("additional_directory/myfile2.txt", "w") as file:
    file.write("Hello file world!")
