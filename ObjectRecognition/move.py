import os, shutil, pathlib, fnmatch
while True:
    # path to source directory
    dir = "C:/Users/Amira Chaib/darkflow/ckpt"
    # gets number of files in directory(dir)
    def get_num(dir):
        list = os.listdir(dir) # dir is your directory path
        number_files = len(list)
        return number_files
    # moves files from source to destination directory
    def move_dir(src: str, dst: str, pattern: str = '*'):
        # creates destination directory if there is none
        if not os.path.isdir(dst):
            pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
        # moves all files (except checkpoint and certain number) from source to destination directory
        for f in fnmatch.filter(os.listdir(src), pattern):
            if f == "checkpoint":
                continue
            else:
                shutil.move(os.path.join(src, f), os.path.join(dst, f))
                num = get_num(dir)
                if num < 10:
                    return

    a = get_num(dir)
    while a > 9:
        move_dir("C:/Users/Amira Chaib/darkflow/ckpt", "E:/Checkpoints")
        a = get_num(dir)
