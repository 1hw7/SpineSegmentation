# source used http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
import SimpleITK as sitk
import sitkUtils
import SampleData

sdl = SampleData.SampleDataLogic()
h = sdl.downloadMRHead()

import SimpleITK as sitk
import sitkUtils
inputImage = sitkUtils.PullFromSlicer('007.CTDC.nrrd')
filter = sitk.BinaryThresholdImageFilter()
filter.SetLowerThreshold(100)
outputImage = filter.Execute(inputImage)
sitkUtils.PushToSlicer(outputImage,'outputImage')


#inputImage = sitkUtils.PullFromSlicer('007.CTDC.nrrd')
#filter = sitk.DiscreteGaussianImageFilter()
#outputImage = filter.Execute(inputImage)
#sitkUtils.PushToSlicer(outputImage,'outputImage')
plt.show()
