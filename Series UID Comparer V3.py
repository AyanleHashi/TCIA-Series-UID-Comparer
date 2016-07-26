import os

path_basename = []
location = os.getcwd()
print location

for (path, dirs, files) in os.walk(location, topdown=True):
            if not dirs:
                path_basename.append(os.path.basename(path))
print path_basename
