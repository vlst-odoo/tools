import git
import subprocess

def formatFileName(file_name):
    split_file_name = file_name.split("/")
    if split_file_name[0] == 'addons':
        return f"@{split_file_name[1]}/{'/'.join(split_file_name[4:])}"
    return f"@{split_file_name[0]}/{'/'.join(split_file_name[3:])}"

def get_renamed_files_from_path(repo_path):
    repo = git.Repo(repo_path)
    commit = repo.head.commit
    diff = commit.diff(commit.parents[0])  # Compare with the parent commit

    renamed_files = []
    for diff_entry in diff.iter_change_type('R'):
        new_name = formatFileName(diff_entry.a_path)
        old_name = formatFileName(diff_entry.b_path)
        renamed_files.append([old_name, new_name])

    return renamed_files

def get_all_renamed_files(paths):
    renamed_files = []
    for path in paths:
        renamed_files += get_renamed_files_from_path(path)
    return renamed_files

def findReplace(folder_path, search_str, replace_str):
    command = f"find {folder_path} -type f -name '*.js' -exec sed -i 's,{search_str},{replace_str},g' {{}} +"
    subprocess.run(command, shell=True)


repo_paths = ['/home/odoo/src/odoo', '/home/odoo/src/enterprise']
search_path = '/home/odoo/src'
renamed_files = get_all_renamed_files(repo_paths)
for file in renamed_files:
    print(f'Old Name: {file[0]} \n New Name: {file[1]}')
    if file[0].endswith('.js'):
        findReplace(search_path, file[0][:-3], file[1][:-3])
