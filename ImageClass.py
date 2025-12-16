import cv2
import numpy as np
import matplotlib.pyplot as plt

class image:
  """This class will allow you to hold all of the image's information in a more concise way then always using the OpenCv functions."""
  def __init__(self, filepath):

    # Set the name equal to the path
    self.filepath = filepath

    # Load in image and resize it to 500 X 500 pixels to make the program consistent
    img = cv2.imread(filepath)
    
    # Check if image is loaded successfully
    if img is None:
        raise ValueError(f"Could not load image from {filepath}")
    self.color_image = cv2.resize(img, (500, 500))

    # Add a grayscale element that can be used later for the edge detection
    self.grayscale_image = cv2.cvtColor(self.color_image, cv2.COLOR_BGR2GRAY)

    # Getting the datatype
    self.datatype = self.color_image.dtype

    # Getting the shape of the image
    self.shape = self.color_image.shape

    # Getting the size of the image
    self.size = self.color_image.size

    # Using composition to get the edges of the image and storing them here
    self.edge = edge(self.grayscale_image)

    # Finally performing the actual combination of the edges and orginal image
    # Since the images are the same size and the same vector size you can add them and change the edges to red
    self.detectedimage = cv2.add(self.color_image, self.edge.colored_edges)



  def show_image(self, display_tag = "c"):
    """Shows image in a new window
        c = color
        g = grayscale
        e = edges of image
        d = detected edges combined """
    #defaults to the c tag
    if display_tag == "c":
      plt.imshow(cv2.cvtColor(self.color_image, cv2.COLOR_BGR2RGB))
    elif display_tag == "g":
      plt.imshow(self.grayscale_image, cmap='gray')
    elif display_tag == "e":
      plt.imshow(self.edge.colored_edges, cmap='gray')
    elif display_tag == "d":
      plt.imshow(cv2.cvtColor(self.detectedimage, cv2.COLOR_BGR2RGB))
    else:
      plt.imshow(cv2.cvtColor(self.color_image, cv2.COLOR_BGR2RGB))
    # removes the axis
    plt.axis('off')
    plt.show()
    return

  def change_color(self, color = "r"):
    """Changes the color of the edges
    r = red
    b = blue
    g = green
    y = yellow
    """
    color_code = (0, 0, 0)
    if color == "r":
      color_code = (0, 0, 255)
    elif color == "b":
      color_code = (255, 0, 0)
    elif color == "g":
      color_code = (0, 255, 0)
    elif color == "y":
      color_code = (0, 255, 255)
    #change all non black edges to the color
    self.edge.colored_edges[self.edge.edges != 0] = color_code
    #recreate the detected image with new colored edges and make them more transparent
    self.detectedimage = cv2.addWeighted(self.color_image, .3, self.edge.colored_edges, .7, 0)
    return

  def __str__(self):
    """Will allow us to print the image infomation to the screen without matlab"""
    self.show_image()
    return f"File Path: {self.filepath}\nShape: {self.shape}\nSize: {self.size}\nDatatype: {self.datatype}"

  def __repr__(self):
    return f"File Path: {self.filepath}\nShape: {self.shape}\nSize: {self.size}\nDatatype: {self.datatype}"

  def __eq__(self, other):
    return self.filepath == other.filepath

class edge:
  """This class is where we will be performing the edge detection on the image and showcasing the composition"""
  def __init__(self, grayscale_image):
    # First we need to blur the image slightly to enhance the edge detection we will use the gaussian blur built in
    self.blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    # Using composition to get the edges of the image and storing them here
    self.edges = cv2.Canny(self.blurred_image, 100, 200)

    # To make the edges more noticable we will make them bright red
    self.colored_edges = cv2.cvtColor(self.edges, cv2.COLOR_GRAY2BGR)
