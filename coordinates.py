import numpy as np
# import os
import argparse

parser = argparse.ArgumentParser(
    prog='coordinates',
    description='What the program can do',
    epilog='Make sure your file has been extracted from skeleton trees in webnossos (.NML)'
)

parser.add_argument('-f', '--file_path', action='store',
                    help='Write fill path to the folder + name of file (e.g. "D:\Download/test.nml")')
parser.add_argument('-k', '--keyword', action='store', default='Synapse',
                    help='Keyword to look in node comments. !Case-sensitive!')

args = parser.parse_args()

# Import NML File (downloaded from Webknossos)
file_path = args.file_path
with open(file_path, 'r') as file:
    file_content = file.readlines()

# Find all node id numbers with comment corresponding to what we look for (comment to rephrase)
ID_numb = []
com_looked = args.keyword
for i in range(len(file_content)):
    if com_looked in file_content[i]:
        ID_numb.append(file_content[i].split('"')[1])
if len(ID_numb) == 0:
    print("/!\ List empty, check keyword or --help /!\ ")
else:
    print(len(ID_numb))

# Create matrix with coordinates of each node identified in previous step
z_list = ['z']
y_list = ['y']
x_list = ['x']
for j in ID_numb:
    text_to_add = 'id="'
    text_to_add2 = '"'
    ID_to_find = f"{text_to_add}{j}{text_to_add2}"
    for i in range(len(file_content)):
        if ID_to_find in file_content[i]:
            y_list.append(file_content[i].split('"')[7])
            x_list.append(file_content[i].split('"')[5])
            z_list.append(file_content[i].split('"')[9])

# Save file
csv_file_path_without_ext = file_path.split('.')[0]
exten_ = '.csv'
csv_file_path = f"{csv_file_path_without_ext}{exten_}"
matrix = np.array([x_list, y_list, z_list]).T
np.savetxt(csv_file_path, matrix, delimiter=',', fmt='%s')
