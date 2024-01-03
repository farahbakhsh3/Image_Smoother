
import numpy as np
from matplotlib import pyplot as plt
from skimage.io import imread
from tqdm import tqdm


def printDetails(image, description):
    print(description)
    print("-" * 20)
    print(image.shape)
    print(image.dtype)
    print()


kernel_width, kernwl_height = 3, 3
kernel = [[-1, 0, +1],
          [-1, 0, +1],
          [-1, 0, +1]]
kernel_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

image = imread("01.jpg")
image_height, image_width, image_channel = image.shape
image_out = np.zeros_like(image, "uint8")

printDetails(image, "Original image")
printDetails(image, "Filtered image")

for row in tqdm(range(image_height)):
    for col in range(image_width):
        for channel in range(image_channel):
            sum_value = 0
            sum_kernel = 0
            for position in kernel_positions:
                r = row + position[0]
                c = col + position[1]
                kernel_value = kernel[position[0] + 1][position[1] + 1]
                if r < 0 or r >= image_height or c < 0 or c >= image_width:
                    pixel_value = 0
                else:
                    pixel_value = image[r, c, channel] * kernel_value
                sum_value += pixel_value
                sum_kernel += kernel_value
            if(sum_kernel == 0):
                final_pixel_value = np.clip(sum_value, 0, 255)
            else:
                final_pixel_value = np.clip(sum_value // sum_kernel, 0, 255)
            image_out[row, col, channel] = final_pixel_value

fig, ax = plt.subplots(2)
ax[0].imshow(image)
ax[1].imshow(image_out)
plt.show()
