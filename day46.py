import os

folder_name = "my_folder"

try:
    os.mkdir(folder_name)
    print("Folder created successfully.")
except FileExistsError:
    print("Folder already exists. Skipping creation.")