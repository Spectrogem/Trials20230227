import cv2
from vimba import *


def run_frame():
    with Vimba.get_instance() as vimba:
        cams = vimba.get_all_cameras()
        with cams[0] as cam:
            frame = cam.get_frame()
            frame.convert_pixel_format(PixelFormat.Mono8)
            cv2.imwrite('frame.jpg', frame.as_opencv_image())


def run_interface():
    with Vimba.get_instance() as vimba:
        inters = vimba.get_all_interfaces()
        with inters[0] as interface:
            for feat in interface.get_all_features():
                print(feat)


if __name__ == '__main__':
    # run_frame()
    # run_interface()

