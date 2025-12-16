#import necessary modules
from Pass_Image import pass_image
from Pass_Image import pass_edge


input_folder = 'Input_Images/*.jpg' # Replace with your input folder path, e.g., './Input_Images/*.jpg'
output_image_folder = 'Output_Images/' # Replace with your desired output folder path, e.g., './Output_Images/'
output_edge_folder = 'Output_Edges/' # Replace with your desired output folder path, e.g., './Output_Edges/'


#complete the program by calling the function!
def main():
    """Main orchestrates the image processing workflow. Can add more functionality here later."""
    if (pass_image(input_folder,output_image_folder)):
        print("Image Processing completed successfully.")
    else:
        print("Processing encountered errors in pass_image.py.")
    if (pass_edge(input_folder,output_edge_folder)):
        print("Edge Processing completed successfully.")
    else:
        print("Processing encountered errors in pass_image.py.")


#call main function

main()