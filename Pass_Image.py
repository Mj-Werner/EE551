import glob
import cv2
import os
from ImageClass import image



def pass_image(input_folder,output_folder):
    """Processes images from the input folder, applies edge detection, and saves them to the output folder."""
    
    files_list = glob.glob(input_folder) # using glob to access all the files in the input directory
  
    for i in files_list: # for loop runs through all files in input_folder
        try:               # first piece of the try/except workflow
            print(f"Processing: {i}!")
            target_image = image(i) # pass each item 'i' to the image class we created
            target_image.change_color("r") # change the color of the edges to red
            output_file = target_image.detectedimage # defines detected image attribute as our output file
            original = os.path.basename(i) # get the original file name from the path
            new_saved_file = os.path.join(output_folder, "output_" + original) # new file name for output file

            cv2.imwrite(new_saved_file, output_file) # writes the new image to the output folder

        except cv2.error as e: # catches exceptions specifically related to cv2 module
            print(f"OpenCV Error: {e}")

        except Exception as e: # catches general exceptions
            print(f"Error: {e}")
    # Return True if processing is completed without unhandled exceptions
    return True

def pass_edge(input_folder, output_folder):
    """Processes images from the input folder, applies edge detection, and saves the edges to the output folder."""

    files_list = glob.glob(input_folder) # using glob to access all the files in the input directory
  
    for i in files_list: # for loop runs through all files in input_folder
        try:               # first piece of the try/except workflow
            print(f"Processing: {i}!")
            target_image = image(i) # pass each item 'i' to the image class we created
            output_file = target_image.edge.edges # gets the edges of the image as output file
            original = os.path.basename(i) # get the original file name from the path
            new_saved_file = os.path.join(output_folder, "output_edges_" + original) # new file name for output file

            cv2.imwrite(new_saved_file, output_file) # writes the new image to the output folder

        except cv2.error as e: # catches exceptions specifically related to cv2 module
            print(f"OpenCV Error: {e}")

        except Exception as e: # catches general exceptions
            print(f"Error: {e}")
    # Return True if processing is completed without unhandled exceptions
    return True