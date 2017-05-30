import numpy as np
from PIL import ImageGrab
import cv2
import time


def process_img(image):
    processed_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img,threshold1=200,threshold2=300)
    return processed_img


def scrape_screen():
    last_time = time.time()
    while (True):
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
        new_screen = process_img(screen)
        # cv2.imshow('window', cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
        # cv2.imshow('window', cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY))
        cv2.imshow('window', new_screen )
        if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        print('Lopp took %f seconds' % (time.time() - last_time))
        last_time = time.time()
        # time.sleep(1)


if __name__ == '__main__':
    scrape_screen()
