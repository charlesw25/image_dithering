import numpy as np
import argparse
import cv2
import os
import time

# Based off of: https://www.visgraf.impa.br/Courses/ip00/proj/Dithering1/ordered_dithering.html
def orderedDitheringBW(name, n = 2):
    img = cv2.imread(name, 0)
    height, width = img.shape

    thresh = generateBayerMatrix(n)
    thresh = (thresh+1)/(n*n)

    for i in range(height): # y
        for j in range(width): # x
            if img[i][j]/255 < thresh[i%n][j%n]:
                img[i][j] = 0
            else:
                img[i][j] = 255

    return img

# Based off of: https://en.wikipedia.org/wiki/Ordered_dithering#Algorithm
def orderedDithering(name, n = 2):
    img = cv2.imread(name)
    height, width, channels = img.shape

    # Initialize Bayer's Threshold Matrix and Pre-Calculated Threshold Map
    thresh = generateBayerMatrix(n)
    # Results in pattern noise being as high frequency as possible.
    thresh = (thresh+1)/(n*n)
    print(thresh)

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

# Helper Functions

def findClosestColor(px, values = [0, 128, 255]):
    dist = list(map(lambda x: abs(x-px), values))
    idx = dist.index(min(dist))
    return values[idx]

# Adopted from: https://github.com/tromero/BayerMatrix/blob/master/MakeBayer.py
def initializeBayer(x, y, n, value, matrix = np.array([])):
    if not matrix.size:
        matrix =  np.full((n, n), 1)

    if n == 1:
        matrix[y][x] = value
        return

    half = n//2

    # pattern is TL, BR, TR, BL
    initializeBayer(x        , y     , half, value+0, matrix)
    initializeBayer(x+half   , y+half, half, value+1, matrix)
    initializeBayer(x+half   , y     , half, value+2, matrix)
    initializeBayer(x        , y+half, half, value+3, matrix)

    return matrix

def generateBayerMatrix(n):
    res = initializeBayer(0, 0, n, 0)
    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Apply ordered dithering to an image.')
    parser.add_argument('input path', type=str, help='Path of image')
    args = parser.parse_args()
    name = vars(args)['input path']

    start_time = time.time()
    res = orderedDithering(name, 2)
    print('Image Created!')
    print(f'--- Elapsed Time: {time.time()-start_time}sec ---')
    cv2.imwrite(f'{os.path.dirname(os.path.realpath(__file__))}/results/dithered_{os.path.basename(name)}', res)

