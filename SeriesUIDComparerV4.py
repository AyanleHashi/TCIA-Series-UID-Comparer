import os
import dicom
import time
import csv
import difflib

start = time.time()
uid = []
pathlist = []
csvlist = []

print('Reading .dcm files...')
for (path, dirs, files) in os.walk(os.getcwd(), topdown=True, onerror=False):
    for name in files:
        if name.endswith('.dcm'): #Check for .dcm files
            dcmfile = dicom.read_file(path + "\\" + name)#if found, then read data
            pathlist.append(path + '\\' + name)
            uid.append(dcmfile.SeriesInstanceUID)
uid = list(set(uid))#Remove duplicates from list
uid.sort()
print("Done reading in", time.time() - start, "seconds.")

for name in os.listdir(os.getcwd()):#Look for series instance UID .csv file
    if name.endswith('.csv'):
        csvname = name
with open(csvname) as csvfile:#Read csv file
    csvreader = csv.reader(csvfile)
    for i in csvreader:
        for x in i:
            csvlist.append(x)
    csvlist.sort()
while '' in csvlist:
    csvlist.remove('')#Remove whitespaces
if uid == csvlist:#Check the difference between the csv and extracted data
    print 'ok'
else:
    print 'There was a difference'
    d = difflib.Differ()
    diff = d.compare(uid, csvlist)
    difference = '\n'.join(diff).splitlines()
    missing = [m for m in difference if '-' in m]
    print missing
