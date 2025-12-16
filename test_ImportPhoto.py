import cv2
import numpy as np
import pytest
from ImageClass import image

def test_dimensions(tmp_path): # defines pytest function with temporary path as input. This way we're keeping our actual directory out of pytest
  """This test checks if our class correctly resizes images passed into it"""
  test_image = tmp_path / "test.jpg" 

  blank_test = np.zeros((100, 100, 3), dtype = np.uint8)
  cv2.imwrite(str(test_image), blank_test)

  resized_test = image(str(test_image)) # this is what pytest is testing, will passing the test through our path size it to 500 x 500

  assert resized_test.shape == (500, 500, 3)

def test_missing():
  """This test checks if the program will correctly fail to pass the test through our image class"""
  missing_file = "no_file_here.jpg" ## returns none 
  with pytest.raises(ValueError):
    image(missing_file)