import numpy as np
from matplotlib import pyplot as plt
from skimage.io import imread
from tqdm import tqdm


def printDetails(image, description):
    print(description)
    print("-"*20)
    print(image.shape)
    print(image.dtype)
    print()


kernel = [-1, 0, +1]

image = imread("01.jpg")
image_out = np.zeros(image.shape, "uint8")
printDetails(image, "Original image")
printDetails(image, "Smoothed image")

for row in tqdm(range(image.shape[0])):
    for col in range(image.shape[1]):
        for channel in range(image.shape[2]):
            sum = 0
            cnt = 0
            for r_idx in range(len(kernel)):
                for c_idx in range(len(kernel)):
                    if 0 <= (row + kernel[r_idx]) < image.shape[0] and \
                            0 <= (col + kernel[c_idx]) < image.shape[1]:
                        sum += image[row + kernel[r_idx], col + kernel[c_idx], channel]
                        cnt += 1
            ave = int(sum / cnt)
            ave = max(0, min(ave, 255))
            image_out[row, col, channel] = ave

figure, axes = plt.subplots(2)
axes[0].imshow(image)
axes[1].imshow(image_out)
plt.show()
