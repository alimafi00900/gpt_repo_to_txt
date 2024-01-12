import os

def get_files_in_directory(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), directory)
            file_list.append(file_path)
    return file_list

# Replace 'your_directory_path' with the path of the directory you want to get the files from
directory_path = '/Users/alireza/Desktop/latencer-core copy'
files = get_files_in_directory(directory_path)

for file in files:
    print(file)