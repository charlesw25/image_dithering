import numpy as np
import cv2
import time

# https://www.visgraf.impa.br/Courses/ip00/proj/Dithering1/ordered_dithering.html
def orderedDitheringBW(name, n = 2):
    img = cv2.imread(name, 0)
    height, width = img.shape

    thresh = np.array([[.25, .75], [1.0, .05]])

    for i in range(height): # y
        for j in range(width): # x
            if img[i][j]/255 < thresh[i%n][j%n]:
                img[i][j] = 0
            else:
                img[i][j] = 255


    cv2.imshow('a', img)
    cv2.waitKey()
    return img

# Based off: https://en.wikipedia.org/wiki/Ordered_dithering#Algorithm
def orderedDithering(name, n = 2):
    img = cv2.imread(name)
    height, width, channels = img.shape

    # Initialize Bayer's Threshold Matrix
    thresh = np.array([[.25, .75], [1.0, .05]])

    r = 255/channels
    offset = 0.5

    for i in range(height): # y
        for j in range(width): # x
            blu, grn, red = img[i][j]

            newB = findClosestColor(blu + r * (thresh[i%n][j%n] - offset))
            newG = findClosestColor(grn + r * (thresh[i%n][j%n] - offset))
            newR = findClosestColor(red + r * (thresh[i%n][j%n] - offset))

            img[i][j] = (newB, newG, newR)

    return img

def findClosestColor(px, values = [0, 128, 255]):
    dist = list(map(lambda x: abs(x-px), values))
    idx = dist.index(min(dist))
    return values[idx]

# Pattern Dithering

if __name__ == '__main__':
    start_time = time.time()

    # orderedDitheringBW('chonk.png')
    res = orderedDithering('gradient.png')

    print(f'--- Time: {time.time()-start_time}sec ---')

    cv2.imwrite('dither.png', res)
    # cv2.imshow('ditheredImage', res)
    # cv2.waitKey()
