from glob import glob

# ============= Glob Functions ==============

def glob_all_files(a_dir="./images/", silent=True):
    if not file_or_dir_exists(a_dir):
        print("Directory does not exist:", a_dir)
        return []
    if not silent:
        print("Globbing all files in dir:", a_dir)
    t0 = datetime.now()
    all_files = glob(a_dir + "**/*.*", recursive=True)
    t1 = datetime.now()
    if not silent:
        print(str(t1-t0) + " secs.")
        print("Found: " + str(len(all_files)) + " files")
    return all_files


def glob_all_folders(a_dir="./images/", silent=True):
    if not file_or_dir_exists(a_dir):
        return False

    if not silent:
        print("\nGlobbing all files...", end="")
    t0 = datetime.now()
    all_folders = glob(a_dir + "**/", recursive=True)
    t1 = datetime.now()
    if not silent:
        print("done. " + str(t1-t0) + " secs.")
        print("Found:", len(all_folders), "files")
    return all_folders


def glob_ext_files(a_dir="./images/", exts=[], verbose=True, sort=True, silent=False):
    if not file_or_dir_exists(a_dir):
        print("Folder does not exist.")
        return []

    if not silent:
        print("\nGlobbing all ext files: ", str(exts))
    t0 = datetime.now()
    if not a_dir.endswith("/"):
        a_dir += "/"
    ext_files = []
    for an_ext in exts:
        ext_files += glob(a_dir + "*." + an_ext, recursive=False)
        ext_files += glob(a_dir + "**/*." + an_ext, recursive=True)
    t1 = datetime.now()
    if not silent:
        print("Time:", str(t1-t0) + " seconds")
    ext_files = list(set(ext_files))
    if not silent:
        print("Found:", str(len(ext_files)) + " files")
    if sort:
        return sorted(ext_files)
    else:
        return ext_files

def glob_image_files(a_dir, img_exts=["jpg", "jpeg", "JPG", "JPG", "png", "PNG"], sort=True, silent=True):
    return glob_ext_files(a_dir, img_exts, sort=sort, silent=silent)


def glob_video_files(a_dir, vid_exts=["mkv", "mp4", "mov", "avi", "wmv", "MOV", "MKV"], sort=True, silent=True):
    return glob_ext_files(a_dir, vid_exts, sort=sort, silent=silent)


def glob_data_files(a_dir, data_exts=["json", "csv", "pkl", "txt", "h5"], sort=True, silent=True):
    return glob_ext_files(a_dir, data_exts, sort=sort, silent=silent)



def glob_search_files(dir_name, file_name, recursive=True, sort=True):
    print("Searching in " + dir_name + " for " + file_name + " files.")
    t0 = datetime.now()
    search_files = []
    if not recursive:
        # takes about 7 seconds
        search_files += glob(dir_name + "*/" + file_name, recursive=False)
        search_files += glob(dir_name + "*/*/" + file_name, recursive=False)
    else:
        # takes about 7 minutes
        search_files += glob(dir_name + "*/" + file_name, recursive=True)
        search_files = glob(dir_name + "**/" + file_name, recursive=True)
    t1 = datetime.now()
    print("Time taken: ", t1-t0, "seconds.")
    search_files = list(set(search_files))     # remove possible duplicates.
    if sort:
        search_files = sorted(search_files)
    return search_files


def get_glob_filesize(glob_or_dir):
    file_sizes = []
    file_size_total = 0
    if type(glob_or_dir) == str:
        glob_files = glob_all_files(glob_or_dir)
    else:
        glob_files = glob_or_dir

    for a_glob in glob_files:
        glob_file_size = os.path.getsize(a_glob)
        file_sizes.append([a_glob, glob_file_size])
        file_size_total += glob_file_size
    return file_sizes, file_size_total
