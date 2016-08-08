import os
import dicom
import time
start = time.time()

dcm = []
uid = []

for (path, dirs, files) in os.walk(os.getcwd()):
    for name in files:
        if name.endswith('.dcm'):
            dcm.append(name)
            dcmfile = dicom.read_file(path + "\\" + name)
            uid.append(dcmfile.SeriesInstanceUID)
uid = list(set(uid))
print("Done in", time.time() - start, "seconds.")