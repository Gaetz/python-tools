import os
cwd = os.getcwd()

if not os.path.exists("Exercice"):
    os.makedirs("Exercice")
exo_path = os.path.join(cwd, "Exercice")
exo_path_file = os.path.join(cwd, "Exercice", "paths.txt")

file = open(exo_path_file, "a")

def write_line(file, to_write):
    file.write(to_write)
    file.write("\n")

# files at folder root
for i in range(0, 15):
    file_path = os.path.join(exo_path, "data_" + str(i) + ".txt")
    write_line(file, file_path)

# folders and files paths
for i in range(0, 3):
    folder_path = os.path.join(exo_path, "collection_" + str(i))
    write_line(file, folder_path)
    for j in range(0, 15):
        file_path = os.path.join(folder_path, "data_" + str(j) + ".txt")
        if i == 0:
            if j % 2 == 0:
                write_line(file, file_path)
        elif i == 1:
            if j % 2 == 1:
                write_line(file, file_path)
        elif i == 2:
            if j == 0 or j == 10:
                write_line(file, file_path)
file.close()

def is_folder(path):
    return not path[-2:] == ".txt"

# Create files and folders
file = open(exo_path_file)
line = file.readline()
while(line != ''):
    line = line[:-1]                # Delete "/n"
    if is_folder(line):             # Folder
        os.makedirs(line)
    else:                           # File
        f = open(line, "w")
        f.close()
    line = file.readline()
    