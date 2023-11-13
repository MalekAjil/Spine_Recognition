import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_array = mpimg.imread('001.png')

nx, ny = image_array.shape
print('nx= ' + str(nx) + " , ny= " + str(ny) + ' , nz= ')
plt.figure()
imgplot = plt.imshow(image_array)
plt.show()
plt.hist(image_array.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
print(image_array)
