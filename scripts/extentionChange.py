import os
File = "Filename.ext"
base = os.path.splitext(File)[0]
os.rename(File, base + ".newext")
