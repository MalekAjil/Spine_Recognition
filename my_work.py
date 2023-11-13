import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd
import cv2
import sys
import tkinter as tk
from tkinter import filedialog

from read_lml import read_lml


def show_slices(slices):
    """Function to display row of image slices """
    # fig, axes = plt.subplots(1, len(slices))
    # for i, slic in enumerate(slices):
    #     axes[i].imshow(slic.T, cmap='gray', origin='lower')
    rows = 21
    columns = 5
    fig = plt.figure()
    slc = 1
    for i in range(slices.shape[2]):
        fig.add_subplot(rows, columns, slc)
        plt.imshow(slices[:, :, i], cmap='gray', origin='lower')
        plt.axis('off')
        plt.title(str(slc))
        slc += 1

    plt.show()
    plt.suptitle('slices for image')


def my_work():
    input_file = ''
    lml_file = ''
    root = tk.Tk()
    root.withdraw()
    try:
        input_file = filedialog.askopenfilename()
        if input_file == '':
            raise FileExistsError
        lml_file = input_file[:-6] + "lml"
        if lml_file == '':
            print('there is no lml file associated with image file..!')
            sys.exit(1)
        print('Input file is ', input_file)
        print('LML file is ', lml_file)

        image_array = nib.load(input_file).get_fdata()

        nx, ny, nz = image_array.shape
        print('nx= ' + str(nx) + " , ny= " + str(ny) + ' , nz= ' + str(nz))

        lml_data = read_lml(lml_file)
        for x in lml_data:
            print(str(x.id) + '\t' + x.name + '\t' + str(x.pos) + '\n')

        # show_slices(image_array)

        fig = plt.figure()
        fig.add_subplot(1, 2, 1)
        plt.imshow(image_array[:, :, 0], cmap='gray', origin='lower')
        plt.axis('off')
        plt.title('original image')

        img = np.array([[512, 512]])
        cv2.edgePreservingFilter(image_array[:, :, 0], img, 1, 1, 1)
        fig.add_subplot(1, 2, 2)
        plt.imshow(img, cmap='gray', origin='lower')
        plt.axis('off')
        plt.title('filtered image')

        plt.show()

        # for current_slice in range(0, 5):  # total_slices):
        #     img = image_array[:, :, current_slice]
        #     plt.figure()
        #     imgplot = plt.imshow(img)
        #     plt.show()
        #     plt.figure()
        #     plt.hist(img.ravel())
        #     print(img)
        #     # cv2.imshow(image_array[:, :, 0])

    except Exception as e:
        print(e)
        sys.exit(2)


my_work()
