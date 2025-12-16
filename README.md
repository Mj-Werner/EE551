# README: Coastal Edge Detector

Matthew Werner (mwerner3@stevens.edu)

Sam Bernhardt (sbernhar@stevens.edu)

This program is designed to help coastal engineers identify coastline locations from imagery of sites of interest. 

## Problem description:
Erosion and accretion processes are constantly shaping and reshaping coastlines. Coastal engineers can use this program to track these changes over a given period of time by taking orthographic imagery and processing it to identify the coastal edge.

## How to use the program:
To install the required packages, run the program  
`Required Package Install`
```sh
pip install opencv-python matplotlib numpy pytest
```

Usage is straightforward. Users will drop relevant image files into the “Input_Images” folder in the Python working directory. Once all the images are uploaded to the input folder, run the "main.py" file to process the images. The program processes each image file, “finding” the coastal edge, and saves the output image and its detected edges into a folder in the working directory. We have included a sample set of files in the input folder. Make sure to delete the test images from the premade folders before beginning.

## Program structure:

You will find we’ve already created an import folder to drop your images into, and an output folder where processed images will be dropped.

The program takes all files in the input folder and recursively passes them to the image class using a “for” loop. We have built in a try/except workflow that will flag either errors related to cv2, or more general errors. 

We have also included a pytest module. The module creates a temporary image with which to run a pytest, ensuring that inputted images are in fact resized to 500 x 500\. The module also includes a pytest to ensure the program will correctly fail to pass the test through our image class in case of a faulty file path.

Most of the work is done through the two main classes defined in the program. Our image class resizes the image to 500 x 500 pixels to make the program consistent, then adds a grayscale element (helpful for edge detection). 

Our edge class further optimizes the image for edge detection, then highlights the identified edges in bright red.

## Main Contribution of each teammate:
Matthew was responsible for building the image and edge classes. He also turned the code into modules, created the main module, and uploaded the modules to GitHub.

Sam was responsible for passing the images to the image class. He also wrote the try/except workflow and the pytest module. Lastly, he wrote the initial README draft.

Sam brought the problem to the group; Matthew identified OpenCV as a potential solution to that problem. We were a great team!

## Author’s info:  
Matthew Werner and Sam Bernhardt are students at Stevens Institute of Technology in Hoboken, New Jersey.

## Code References Used:

1) [OpenCv Training video](https://www.bing.com/videos/riverview/relatedvideo?q=using+OpenCV+to+highlight+coastlines+and+pictures&mid=732A55723526908E421B732A55723526908E421B&FORM=VIRE)

2) [OpenCv Cheat Sheet](https://www.geeksforgeeks.org/python/python-opencv-cheat-sheet/)

3) [OpenCv Documentation](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)

4) [OpenCv Addweighted Documentation](https://pytutorial.com/python-opencv-cv2addweighted-guide/)
