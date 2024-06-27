import os

# Enter the directory for which you want to list the content

directory_path = '/Users/akshaygogate/Python'

# List all the files and directories in above path using listdir

contents = os.listdir(directory_path)

# Print each file and directory name

print(contents)

# OR - Both above or below statement can be used in this scenario

for item in contents:
    print(item)