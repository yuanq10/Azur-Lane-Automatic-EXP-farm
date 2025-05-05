import os
import cv2
import time

screenshot_path = os.path.join(os.path.dirname(__file__), r"Screenshots\screen_capture.png")

def Screenshot():
    os.system(f"adb exec-out screencap -p > \"{screenshot_path}\"")
    time.sleep(1)
    screen = cv2.imread(screenshot_path)
    if screen is None:
        raise ValueError("Screenshot unsuccessful")
    else:
        print(f"the screenshot has been saved to {screenshot_path}")
    
    return screen