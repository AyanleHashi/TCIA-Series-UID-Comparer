import os
import csv
import difflib

path_basename = []
uid_list = []

for name in os.listdir(os.getcwd()):
    if name.endswith('.csv'):
        csvname = name

with open(csvname) as uid_csv:
    csvreader = csv.reader(uid_csv)
    for i in csvreader:
        for x in i:
            uid_list.append(x)

while '' in uid_list:
    uid_list.remove('')
uid_list.sort()

for (path, dirs, files) in os.walk(os.getcwd()):
            if not dirs:
                path_basename.append(os.path.basename(path))
path_basename.sort()

d = difflib.Differ()
diff = d.compare(uid_list, path_basename)
difference = '\n'.join(diff)

difflines = difference.splitlines()
find = '-'
missing = [m for m in difflines if find in m]

if '-' in difference:
    print('You are missing files. \nHere is a list of missing files:')
    print(missing)
elif '+' in difference:
    print('You have extra files. \nHere is a list of extra files:')
    print(difference)
else:
    print('No extra file downloads are needed.')
