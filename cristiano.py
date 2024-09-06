import imageio.v3 as iio

filenames = ['suii/1.png', 'suii/2.png', 'suii/3.png', 'suii/4.png', 'suii/5.png', 'suii/6.png', 'suii/7.png', ]
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('suii.gif', images, duration = 400, loop = 0)