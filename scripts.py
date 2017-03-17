'''
import SimpleITK as sitk
import sitkUtils
f = 'filename'
slicer.util.loadVolume(f)
inputImage = sitkUtils.PullFromSlicer('image number')
filter = sitk.'DiscreteGaussianImageFilter'()
outputImage = filter.Execute(inputImage)
sitkUtils.PushToSlicer(outputImage,'outputImage')
'''