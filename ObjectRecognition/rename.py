import os, sys

# change path to directory in which you want to rename all files
path = "C:/Users/Amira Chaib/darkflow/training/annotations/"

# enumerates filename (to 6 digit) in directory (path)
def rename():
    i = 1

    # loop through all files in current directory
    for filename in os.listdir(path):
        # filename of length 6
        # change extension in case of different filetype
        fname = "{:06}.xml".format(i)
        # path to source file
        src = path + filename
        # path to renamed file
        dst = path + fname
        # rename file
        os.rename(src, dst)
        i += 1

# calls methods when running this script
if __name__ == '__main__':
    rename()
