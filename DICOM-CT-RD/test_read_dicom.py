# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:10:22 2015

@author: jmoosmann
"""

import dicom
import os
import numpy
from matplotlib import pyplot, cm

PathDicom = "/home/jmoosmann/data/mayo/DICOM-CT-PD"
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    print dirName, subdirList, fileList
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))

# Get ref file
#RefDs = dicom.read_file(lstFilesDCM[0])

# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
#ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))

# Load spacing values (in mm)
#ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))
