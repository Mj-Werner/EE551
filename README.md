# README: Coastal Edge Detector

This program is designed to help coastal engineers identify coastline locations from imagery of sites of interest. Erosion and accretion processes are constantly shaping and reshaping coastlines. Coastal engineers can use this program to track this change over a given period of time.

## Execution and usage:
To install the required packages, run the program  
`Required Package Install`
```sh
pip install opencv-python matplotlib numpy pytest
```

Usage is straightforward. Users will drop relevant image files into the “Input_Images” folder in the Python working directory. Once all the images are uploaded to the input folder, run the "main.py" file to process the images. The program processes each image file, “finding” the coastal edge, and saves the output image and its detected edges into a folder in the working directory. We have included a sample set of files in the input folder. Make sure to delete the test images from the premade folders before beginning.

## Current features:

You will find we’ve already created an import folder to drop your images into, and an output folder where processed images will be dropped.

The program takes all files in the input folder and recursively passes them to the image class using a “for” loop. We have built in a try/except workflow that will flag either errors related to cv2, or more general errors. 

We have also included a pytest module. The module creates a temporary image with which to run a pytest, ensuring that inputted images are in fact resized to 500 x 500\. The module also includes a pytest to ensure the program will correctly fail to pass the test through our image class in case of a faulty file path.

Most of the work is done through the two main classes defined in the program. Our image class resizes the image to 500 x 500 pixels to make the program consistent, then adds a grayscale element (helpful for edge detection). 

Our edge class further optimizes the image for edge detection, then highlights the identified edges in bright red.

## Author’s info:  
Matthew Werner and Sam Bernhardt are students at Stevens Institute of Technology in Hoboken, New Jersey.
