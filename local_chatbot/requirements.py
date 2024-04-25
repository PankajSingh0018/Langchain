import os

current_directory = os.getcwd()

try:
    file = open("requirements.txt",'r')
    file.read()
    print("Requirements.txt file exists in the system")


except FileNotFoundError as e:
    print("File not found in the directory")
