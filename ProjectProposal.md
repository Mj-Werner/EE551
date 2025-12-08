# EE551 Introduction to Python  
## Project Proposal

<img width="577" height="707" alt="image" src="https://github.com/user-attachments/assets/26398905-7b4b-4d32-899f-f85b306ea015" />  




**Project Developed by Samuel Bernhardt and Matthew Werner**

*“I pledge my honor that I have abided by the Stevens Honor System”*  
**Samuel Bernhardt and Matthew Werner**

---

## Background

Coastal erosion presents a serious problem for much of New Jersey’s coastal areas. Climate change is fueling increasingly stronger storms, which can erode coastal land masses at much higher rates. Erosion of beaches, islands, and sedges can endanger waterfront communities, reduce animal habitat, and impact recreational and commercial boating. Coastal engineers have a range of tactics to be able to respond to erosion threats, for example beach replenishment, living shoreline methods, and seawalls.

However, coastal engineers lack access to robust datasets from which to understand where erosion is occurring. Previous methodologies involve manually tracing out shoreline position based on aerial images found in Google Earth. Not only is this painstaking, but it also creates a separate, parallel workflow to the rest of the site characterization process. A more robust approach is needed, wherein shoreline lines or polygons can be generated from available aerial images.

---

## Scope

The scope for our project is to design a Python program that will use a set of orthographic photo files, process the image using computer vision libraries, and highlight the shorelines of the picture. From there, further processing can be done to determine what parts of the shore are at most risk for shore erosion; however, this part is not in the scope of our project.

---

## Our Project

Our project will make use of computer vision libraries such as OpenCV to preprocess the orthographic image and highlight the shorelines of the photo file. This new shoreline can then be overlaid on top of the original image to show the outline of the shore on the photo. Ideally, the program can process a folder of images at once and not have to reload the program.

The project will follow the following steps: each step will be separated into functions to allow for parallel development:

1. Load image from folder  
2. Process the image  
3. Grayscale the image to avoid inconsistency  
4. Scale photo to ensure correct detection  
5. Smooth photo to reduce granularity  
6. Detect the shorelines with edge detection (built into OpenCV)  
7. Highlight with a separate color  
8. Smooth sharp edges to reflect more realistic shoreline  
9. Display the processed edge detection on top of the original image  
10. Optional calculation of shoreline length if needed  
11. Move onto next image  

