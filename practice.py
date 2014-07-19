import os

if not os.path.exists("practice_folder"):
    os.makedirs("practice_folder")

with open("practice_folder/practice.txt", "w") as text:
	text.write("Hungry")