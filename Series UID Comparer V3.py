import os
import csv
import difflib

path_basename = []
UIDList = []
difflist = []

with open('Series Instance UID List.csv') as uid_csv:
    csvreader = csv.reader(uid_csv)
    for i in csvreader:
        for x in i:
            UIDList.append(x)

while '' in UIDList:
    UIDList.remove('')
UIDList.sort()
location = os.getcwd()
location = 'C:\Users\Ayanle\AppData\Local\Temp\REMBRANDT\900-00-1961'

for (path, dirs, files) in os.walk(location, topdown=True):
            if not dirs:
                path_basename.append(os.path.basename(path))
path_basename.sort()

d = difflib.Differ()
diff = d.compare(UIDList, path_basename)
difference = '\n'.join(diff)

difflines = difference.splitlines()

if '+' or '-' in difference:
    print 'There was a difference:'
    print difference
