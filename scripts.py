import SimpleITK as sitk
import sitkUtils
#loaded image by dragging file into slicer 
inputImage = sitkUtils.PullFromSlicer('007.CTDC.nrrd')
filter = sitk.DiscreteGaussianImageFilter()
outputImage = filter.Execute(inputImage)
sitkUtils.PushToSlicer(outputImage,'outputImage')
