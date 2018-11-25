# This script makes a folder for every type of file in the directory
# and moves every file to its corresponding folder.
import os.path
DIR = str(os.path.dirname(os.path.realpath(__file__)))+"/"


def move_file():
    os.rename(DIR + str(file), DIR + ext + "/" + str(file))


# Goes through each file in directory
for file in os.listdir(DIR):
    # Skips self and folders
    if str(file) != os.path.basename(__file__) and os.path.isdir(str(file)) is False:
        # Gets file type
        ext = os.path.splitext(str(file))[1][1:]
        # Checks if folder already exist if not makes it
        if os.path.isdir(DIR+ext):
            move_file()
        else:
            os.makedirs(DIR+ext)
            move_file()
