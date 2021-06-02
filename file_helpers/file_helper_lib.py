from datetime import datetime
from pathlib import Path
import os, sys
import shutil


# ========= File Path Helpers ========

def full_path(a_file, parent=False):
    if parent:
        return str(Path(a_file).absolute().parent)
    return str(Path(a_file).absolute())

def new_file_path(a_file, old_dir, new_dir):
    return a_file.replace(old_dir, new_dir)

def file_or_dir_exists(a_dir):
    if not os.path.exists(a_dir):
        print("Directory:", a_dir, "does not exist.")
        return False
    return True


# ========= Dir Helpers ========

def get_parent_directory(a_file):
    if not os.path.exists(a_file):
        print("File does not exist")
        return ""
    return os.path.dirname(a_file)

# in case I space on original function name.
def parent_dir(a_file):
    return get_parent_directory(a_file)


def check_folders_exist(folder_list=[]):
    for a_folder in folder_list:
        if not os.path.exists(a_folder):
            print("Folder does not exist:", a_folder)
            sys.exit()


def mkdirs_if_dne(a_dir_or_file, parent=True):
    if os.path.isfile(a_dir_or_file) or parent:
        a_dir_or_file = str(Path(a_dir_or_file).parent)
    if not os.path.exists(a_dir_or_file):
        Path(a_dir_or_file).mkdir(parents=True, exist_ok=True)
        return True
    return False


# ========= File Helpers ========

def file_or_dir_exists(a_dir):
    if not os.path.exists(a_dir):
        print("Directory:", a_dir, "does not exist.")
        return False
    return True


def file_missing(a_file):
    return not os.path.exists(a_file)

def get_file_size(a_file):
    return os.path.getsize(a_file)

def file_basename(a_file):
    return os.path.basename(a_file)

def get_file_contents(a_file):
    with open(a_file) as f:
        content = f.readlines()
    return [x.strip() for x in content]

def move_if_dne(a_file, new_path, is_file=True, mk_dne_dirs=True):
    if mk_dne_dirs:
        if is_file:
            mkdirs_if_dne(new_path, parent=True)

    if not os.path.exists(new_path):
        full_file_path = full_path(a_file)

        if is_file:
            shutil.copy(full_file_path, full_path(new_path, parent=True))
        else:
            shutil.move(full_file_path, full_path(new_path))
        if is_file:
            os.remove(full_file_path)
        else:
            shutil.rmtree(full_file_path)
        return True
    else:
        return False

def force_move(a_file, new_path, only_if_same_filesize=False, mk_dne_dirs=True):
    if mk_dne_dirs:
        mkdirs_if_dne(new_path, parent=True)

    if os.path.exists(new_path):
        if os.path.getsize(new_path) != os.path.getsize(a_file):
            if only_if_same_filesize:
                return False
    try:
        shutil.copy(full_path(a_file), full_path(new_path, parent=True))
        os.remove(full_path(a_file))
    except shutil.Error:
        # shutil.move(full_path(a_file), full_path(new_path, parent=True))
        return False
    return True
