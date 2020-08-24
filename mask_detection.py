import cv2
import argparse
import orien_lines
import datetime
from imutils.video import VideoStream
from utils import detector_utils as detector_utils
import pandas as pd
from datetime import date
import xlrd
from xlwt import Workbook
from xlutils.copy import copy 
import numpy as np
import imutils
from PIL import Image
from matplotlib import cm



ap = argparse.ArgumentParser()
ap.add_argument('-d', '--display', dest='display', type=int,
                        default=1, help='Display the detected images using OpenCV. This reduces FPS')
args = vars(ap.parse_args())

detection_graph, sess = detector_utils.load_inference_graph()



if __name__ == '__main__':
    # Detection confidence threshold to draw bounding box
    score_thresh = 0.70
    
    #vs = cv2.VideoCapture('rtsp://192.168.1.64')
    vs = VideoStream(0).start()
    #Oriendtation of machine    
    Orientation= 'bt'

    num_of_face_detect = 2

    # Used to calculate fps
    start_time = datetime.datetime.now()
    num_frames = 0

    im_height, im_width = (None, None)
    cv2.namedWindow('Detection', cv2.WINDOW_NORMAL)

    try:
        while True:
            frame = vs.read()

            frame = np.array(frame)


            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
            if im_height == None:

                im_height, im_width = frame.shape[:2]

            # Convert image to rgb since opencv loads images in bgr, if not accuracy will decrease
            try:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            except:
                print("Error converting to RGB")

            boxes, scores, classes = detector_utils.detect_objects(frame, detection_graph, sess)




            #Line_Position2=orien_lines.drawsafelines(frame,Orientation,Line_Perc1,Line_Perc2)
            # Draw bounding boxeses and text
            a, b,g = detector_utils.draw_box_on_image(num_of_face_detect, score_thresh, scores, boxes, classes, im_width, im_height, frame,Orientation)
            f = cv2.cvtColor(g, cv2.COLOR_BGR2RGB)



            box_height, box_width = (None,None)
            #


            if box_height == None:
                box_height, box_width = f.shape[:2]

            try:
                f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
            except:
                print("Error converting to RGB")


            f_boxes,f_score,f_classes = detector_utils.detect_objects_1(f, detection_graph, sess)

            detector_utils.draw_box_on_image_1(num_of_face_detect, score_thresh,f_score, f_boxes, f_classes,box_width, box_height,f,Orientation)

            num_frames += 1
            elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
            fps = num_frames / elapsed_time



            if args['display']:
                # Display FPS on frame
                detector_utils.draw_text_on_image("FPS : " + str("{0:.2f}".format(fps)), frame)
                cv2.imshow('Detection', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                detector_utils.draw_text_on_image_1("FPS : " + str("{0:.2f}".format(fps)), f)
                cv2.imshow('Detection', cv2.cvtColor(f, cv2.COLOR_RGB2BGRA))
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    vs.stop()
                    break
        print("Average FPS: ", str("{0:.2f}".format(fps)))
        
    except KeyboardInterrupt: 

        today = date.today()
        print("Average FPS: ", str("{0:.2f}".format(fps)))