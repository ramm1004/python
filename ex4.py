import os
current_directory = os.getcwd()
print("List of .txt files in current directory:")
for file in os.listdir(current_directory):
    if file.endswith(".txt"):
        print(file)
    else:
        print("no files")