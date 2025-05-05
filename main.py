from Connections import *
from Screenshot import *
from Find_template import *
import cv2
import time
import os

def main():
    """
    1600x900 分辨率
    x:720-900
    y:750-805
    """
    x_max = 900
    x_min = 720
    y_max = 805
    y_min = 750

    #connect_adb()

    leave_template_path = os.path.join(os.path.dirname(__file__), r"Templates\Leave_template.png")
    leave_template = cv2.imread(leave_template_path)
    try:
        while True:
            screen = Screenshot()
            leave_part = screen[y_min:y_max, x_min:x_max]

            find_result = Find_template(leave_part, leave_template)
            print(find_result)

            time.sleep(2)

    except KeyboardInterrupt:
        print('interrupted!')

    #disconnect_adb()

if __name__ == "__main__":
    main()
