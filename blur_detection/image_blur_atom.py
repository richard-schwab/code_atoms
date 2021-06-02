import csv
import cv2
from datetime import datetime
from glob import glob
import PIL.Image
import os
import sys
from tqdm import tqdm
import traceback

import imquality.brisque as brisque

# === Laplacian Blur Detection ====

def laplacian_blur_detect(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()


def blur_detect(imagePath):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_score = laplacian_blur_detect(gray)
    return image, blur_score


# === Brisque Blur Detection ===

def brisque_score(an_img):
    if type(an_img) == str:
        an_img = PIL.Image.open(an_img)
    return brisque.score(an_img)


# === Batch Image Collection ====

def file_or_dir_exists(a_dir):
    if not os.path.exists(a_dir):
        print("Directory:", a_dir, "does not exist.")
        return False
    return True

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


# === CSV Results ====

def read_list_of_dicts(file_name):
    with open(file_name) as f:
        a = [{k: v for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]
    return a

def write_list_of_dicts(toCSV, file_name):
    keys = toCSV[0].keys()
    with open(file_name, "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
    print("Written:", len(toCSV), "rows to:", file_name)


# === Batch get image blur ===

def batch_get_image_blur(a_folder):
    results = []
    error_list = []
    images = glob_image_files(a_folder)
    pbar = tqdm(total=len(images))
    errors = tqdm(total=len(images))
    pbar.set_description("Image: ".ljust(50))
    errors.set_description("Error: ".ljust(50))
    for a_file in images:
        try:
            results.append({"file": a_file, "brisque": brisque_score(a_file), "laplace": blur_detect(a_file)[1]})
            pbar.set_description(str("Image: " + a_file).ljust(50))
            pbar.update(1)
        except Exception as e:
            errors.set_description(str("Error: " + a_file).ljust(50))
            errors.update(1)
            error_list.append([a_file, traceback.format_exc()])
            pass
    pbar.close()
    errors.close()
    if error_list:
        print("\nError List:")
        for an_error in error_list:
            print(an_error[0])
            print(an_error[1])
    write_list_of_dicts(results, "image_blur_report.csv")



if __name__ == "__main__":

    if len(sys.argv) > 1:
        a_dir = sys.argv[1]
    else:
        a_dir = input("Enter directory to blur detect: ")
    if os.path.exists(a_dir):
        if os.path.isdir(a_dir):
            batch_get_image_blur(a_dir)
        else:
            print("Directory exists, but is not a directory: ", a_dir)
    else:
        print("Directory does not exist: ", a_dir)
