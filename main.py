import numpy as np
import cv2

img = cv2.imread('test.jpg', 0)
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('testgray.png',img)
#     cv2.destroyAllWindows()
#print(np.shape(img))
print(img[0][0])
x = len(img[0])
y = len(img)
for i in range(y):
     for j in range(x):
         oldPixel = img[i][j]
         newPixel = int(oldPixel / 256)
         img[i][j] = oldPixel
         quantError = oldPixel - newPixel
         print(quantError)
         if j + 1 < x:
             img[i][j+1] = img[i][j+1] + quantError * (7/16)
         if j - 1 >= 0 and i + 1 < y:
             img[i+1][j-1] = img[i+1][j-1] + quantError * (3/16)
         if i + 1 < y:
             img[i+1][y] = img[i+1][y] + quantError * (5/16)
         if j + 1 < x and i + 1 < y:
             img[i+1][y+1] = img[i+1][y+1] + quantError * (1/16)



cv2.imwrite('test.png',img)
