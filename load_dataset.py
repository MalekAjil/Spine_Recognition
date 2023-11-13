import os
import sys
import nibabel as nib
import tkinter as tk
from tkinter import filedialog

from read_lml import read_lml


def load_dataset():
    """to load nii files from multiple folders inside specified folder"""
    img_dataset = []
    lml_dataset = []
    root = tk.Tk()
    root.withdraw()
    try:
        input_folder = filedialog.askdirectory()
        if input_folder == '':
            raise FileExistsError
        print(input_folder)
        for folder in os.listdir(input_folder):
            path1 = os.path.join(input_folder, folder)
            for x in os.listdir(path1):
                path2 = os.path.join(path1, x)
                for y in os.listdir(path2):
                    path3 = os.path.join(path2, y)
                    if y.endswith('.nii.gz'):
                        # print('nii file is $ ' + path3)
                        img = nib.load(path3).get_fdata()
                        if img is not None:
                            img_dataset.append(img)
                    elif y.endswith('.lml'):
                        # print('LML file is % ', path3)
                        lml_data = read_lml(path3)
                        if lml_data is not None:
                            lml_dataset.append(lml_data)

    except Exception as e:
        print(e)
        sys.exit(2)
    finally:
        return img_dataset, lml_dataset


def load_dataset2():
    """to load nii files directly from one specified folder"""
    img_dataset = []
    root = tk.Tk()
    root.withdraw()
    try:
        input_folder = filedialog.askdirectory()
        if input_folder == '':
            raise FileExistsError
        print(input_folder)
        for file in os.listdir(input_folder):
            path1 = os.path.join(input_folder, file)
            if file.endswith('.nii.gz'):
                # print('nii file is $ ' + path1)
                img = nib.load(path1).get_fdata()
                if img is not None:
                    img_dataset.append(img)

    except Exception as e:
        print(e)
        sys.exit(2)
    finally:
        return img_dataset


# niidata, lmldata = load_dataset()
# print(len(niidata))
# print(len(lmldata))
# for lml in lmldata[16]:
#     print(str(lml.id) + '\t' + lml.name + '\t' + str(lml.pos) + '\n')

# niidata = load_dataset2()
# print(len(niidata))
