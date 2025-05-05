import cv2
import numpy as np

# Note the values to pass in here are not images, but the cv2.read result matrix grey scale
def Find_template(source, template,threshold=0.1):
    method = cv2.TM_SQDIFF_NORMED #Note for SQDIFF method, the lowest value in result matrix gives the best match

    result = cv2.matchTemplate(source, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if min_val <= threshold:
        return True
    else:
        return False
    return
