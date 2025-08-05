import os
folder_name = "test_folder"
current_directory = os.getcwd()
folder_path = os.path.join(current_directory, folder_name)
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print(f"Folder '{folder_name}' created at: {folder_path}")
else:
    print(f"Folder '{folder_name}' already exists at: {folder_path}")