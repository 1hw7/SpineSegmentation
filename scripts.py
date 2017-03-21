# source used http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
import SimpleITK as sitk
import sitkUtils
import cv2
import numpy as np
from matplotlib import pyplot as plt


inputImage = sitkUtils.PullFromSlicer('007.CTDC.nrrd')
filter = sitk.DiscreteGaussianImageFilter()
outputImage = filter.Execute(inputImage)
sitkUtils.PushToSlicer(outputImage,'outputImage')



ret,thresh1 = cv2.threshold(outputImage,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(outputImage,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(outputImage,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(outputImage,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(outputImage,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [outputImage, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
