import os.path

dir = str(os.path.dirname(os.path.realpath(__file__)))+"/"

# Goes through each file in directory
for file in os.listdir(dir):
    # Check file type
    ext = os.path.splitext(str(file))[1]
    ext = ext[1:]
    # Skips .py and folders
    if ext != "py" and os.path.isdir(str(file)) is False:
        # Checks if folder already exist if not makes it
        if os.path.isdir(dir+ext):
            os.rename(dir+str(file), dir+ext+"/"+str(file))
        else:
            os.makedirs(dir+ext)
            os.rename(dir + str(file), dir+ext+"/"+str(file))
