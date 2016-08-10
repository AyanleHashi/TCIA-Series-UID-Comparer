#Updated to read from .dcm files directly instead of folder names
from __future__ import print_function
import os
import dicom
import csv
import difflib

uid = []
csvlist = []

print('Reading .dcm files...')
for (path, dirs, files) in os.walk(os.getcwd(), topdown=True, onerror=False):
    for name in files:
        if name.endswith('.dcm'): #Check for .dcm files
            dcmfile = dicom.read_file(path + "\\" + name)#if found, then read data
            uid.append(dcmfile.SeriesInstanceUID)
uid = list(set(uid))#Remove duplicates from list
uid.sort()

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
    print('All files are present.')
else:
    d = difflib.Differ()
    diff = d.compare(uid, csvlist)
    difference = '\n'.join(diff).splitlines()
    missing = [m for m in difference if '-' in m]
    print('You are missing some files. Here is a list of the missing ones:\n', [i for i in missing])
