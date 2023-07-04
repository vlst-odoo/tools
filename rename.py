import os
import shutil

def rename_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.xml') or file.endswith('.js'):
                old_name = os.path.join(root, file)
                new_name = os.path.join(root, convert_to_snake_case(file))
                os.rename(old_name, new_name)
                print(f'Renamed {old_name} to {new_name}')

def convert_to_snake_case(file_name):
    snake_case_name = file_name[0].lower()
    for char in file_name[1:]:
        if char.isupper():
            snake_case_name += '_' + char.lower()
        else:
            snake_case_name += char
    return snake_case_name

def rename_folders(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for folder in dirs:
            old_name = os.path.join(root, folder)
            new_name = os.path.join(root, convert_to_snake_case(folder))
            if os.path.exists(new_name):
                print(f'Skipped {old_name} as {new_name} already exists')
            else:
                os.rename(old_name, new_name)
                print(f'Renamed {old_name} to {new_name}')

def organize_files(root_dir):
    """
    this will put the js and xml files in a folder with the same name as the file
    """
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith((".js", ".xml")):
                file_path = os.path.join(root, file)
                new_folder = os.path.splitext(file)[0]  # Remove file extension from file name
                destination_folder = os.path.join(root, new_folder)
                if destination_folder.split("/")[-1] == destination_folder.split("/")[-2]:
                    print(f"Skipped {file_path} as it is already in {destination_folder}")
                    continue
                destination_path = os.path.join(destination_folder, file)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                if not os.path.exists(destination_path):
                    shutil.move(file_path, destination_path)
                    print(f"Moved {file_path} to {destination_path}")
                else:
                    print(f"Skipped {file_path} as {destination_path} already exists")



root_directory = '/home/odoo/src/enterprise/pos_settle_due/static/src/overrides/components'


rename_files(root_directory)
rename_folders(root_directory)
organize_files(root_directory)
