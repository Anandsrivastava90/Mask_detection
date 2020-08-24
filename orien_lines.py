import math
from itertools import combinations

import cv2

def drawsafelines(image_np,Orientation,Line_Perc1,Line_Perc2):
    
    posii = int(image_np.shape[1]-(image_np.shape[1]/3))
    cv2.putText(image_np,'Blue Line : Machine Border Line',
                        (posii,20),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0,0,255), 1, cv2.LINE_AA)
    cv2.putText(image_np, 'Red Line : Safety Border Line',
                        (posii,40),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255,0,0), 1, cv2.LINE_AA)
    
    if(Orientation=="bt"):
        
        Line_Position1 = int(image_np.shape[0]*(Line_Perc1/100))
        print("The line position1", Line_Position1)
        
        Line_Position2=int(image_np.shape[0]*(Line_Perc2/100))
        print("The line position2", Line_Position2)

        cv2.line(img=image_np, pt1=(0, Line_Position1), pt2=(image_np.shape[1], Line_Position1), color=(0, 0, 255), thickness=2, lineType=8, shift=0)
                
        cv2.line(img=image_np, pt1=(0, Line_Position2), pt2=(image_np.shape[1], Line_Position2), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        
        return Line_Position2;
        
    elif(Orientation=="tb"):
       
        Line_Position1=int(image_np.shape[0]-(image_np.shape[0]*(Line_Perc1/100)))
        
        Line_Position2=int(image_np.shape[0]-(image_np.shape[0]*(Line_Perc2/100)))
        
        cv2.line(img=image_np, pt1=(0, Line_Position1), pt2=(image_np.shape[1], Line_Position1), color=(0, 0, 255), thickness=2, lineType=8, shift=0)
                 
        cv2.line(img=image_np, pt1=(0, Line_Position2), pt2=(image_np.shape[1], Line_Position2), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        
        return Line_Position2;
    
    elif(Orientation=="lr"):
        
        
        Line_Position1=int(image_np.shape[1]-(image_np.shape[1]*(Line_Perc1/100)))
        
        Line_Position2=int(image_np.shape[1]-(image_np.shape[1]*(Line_Perc2/100)))
        
        cv2.line(img=image_np, pt1=(Line_Position1, 0), pt2=(Line_Position1,image_np.shape[0]), color=(0, 0, 255), thickness=2, lineType=8, shift=0)
                
        cv2.line(img=image_np, pt1=(Line_Position2, 0), pt2=(Line_Position2,image_np.shape[0]), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
           
        return Line_Position2;
        
        
    elif(Orientation=="rl"):
        
        Line_Position1=int(image_np.shape[1]*(Line_Perc1/100))
        
        Line_Position2=int(image_np.shape[1]*(Line_Perc2/100))
        
        cv2.line(img=image_np, pt1=(Line_Position1, 0), pt2=(Line_Position1,image_np.shape[0]), color=(0, 0, 255), thickness=2, lineType=8, shift=0)
                
        cv2.line(img=image_np, pt1=(Line_Position2, 0), pt2=(Line_Position2,image_np.shape[0]), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        
        return Line_Position2;

def draw_safeline(image_np,boxes,im_width,im_height):
    no_of_boxes = []
    for i in range(0,2):
        (left, right, top, bottom) = (boxes[i][1] * im_width, boxes[i][3] * im_width,boxes[i][0] * im_height, boxes[i][2] * im_height)
        p1 = (int(left), int(top))
        p2 = (int(right), int(bottom))
        start_point = (int((p1[0]+p2[0])/2),int((p1[1] + p2[1])/2))
        no_of_boxes.append(start_point)

        #social_dist_1 = (int(p2[0]),int((p1[1] + p2[1]) / 2))
        #(left_1, right_1, top_1, bottom_1) = (boxes[1][1] * im_width, boxes[1][3] * im_width, boxes[1][0] * im_height, boxes[1][2] * im_height)
        #p1_1 = (int(left_1), int(top_1))
        #p2_2 = (int(right_1), int(bottom_1))
        #social_dist_2 = (int(p1_1[0]),int((p1_1[1] + p2_2[1]) / 2))
        #dx = social_dist_1[0] - social_dist_2[0]
        #dy = social_dist_1[1] - social_dist_2[1]

        #line_position = int(image_np.shape[0]*(float(60)/100))

    return no_of_boxes












