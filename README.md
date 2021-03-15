# image_dithering
A rudimentary image dithering algorithm done in python with the OpenCV library with the help of numpy alongside other miscellaneous libraries. 

This was more of a means to get my feet wet with ordered dithering, and **should not** be a means of practical use. The script takes seconds to run for a single image, and could do with some improvements.


## Running the script...
In order to start the script, run:
`python image_dithering/main.py [path_to_whatever_image]`

You need to pass in the path to whatever image you want to apply dithering to.

## How it Works
The file itself contains only one main method `orderedDithering` which generates a threshold map that assists in generating new colors for each pixel. Each color channel for each pixel in the image is then iterated over, and a new value (either 0, 128, or 255) is chosen. By utilizing the threshold map and the means of finding a new fixed value for each color channel, we are able to create a dithering effect. In-depth implementation details can be found [here](https://en.wikipedia.org/wiki/Ordered_dithering#Algorithm).


## Inspirations and Resources Used
Threshold map initialization was heavily inspired by [this code](https://github.com/tromero/BayerMatrix/blob/master/MakeBayer.py), and actual conceptualization was done with the help of [this webpage](https://www.visgraf.impa.br/Courses/ip00/proj/Dithering1/ordered_dithering.html). Without these two links, I would have struggled immensely with how to implement and work with an ordered dithering algorithm.
