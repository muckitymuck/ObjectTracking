#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import Libraries
import cv2
import sys
from random import radint


# Tracker Types
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

# Define trackers by name
def tracker_name(tracker_type):

    # Create trackers by name with if statement
    if tracker_types == tracker_type[0]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_type[1]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_type[2]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_type[3]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_type[4]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_type[5]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_type[6]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_type[7]:
        tracker = cv2.TrackerBoosting_create()
        
    # else statemen
    else:
        tracker = None
        print("No Tracker found")
        print("Choose from these trackers: ")
        for tr in tracker_types:
            print (tr)
    
    # return
    return tracker


if __name__ == '__main__':
    print("Default tracking algorithm MOSSE \n"
         "Available algorithms are: \n")
    for ta in tracker_types:
        print(tr)
       
    tracker_type = 'MOSSE'


    # Create a video capture
    cap - cv2.VideoCapture('Video/Vehicles.mp4')
    
    # Read first frame
    success, frame = cap.read()
    
    # Quit if failure
    if not success:
        print('Cannot read the video')
    
    # Select boxes and colors
    rects = []
    color = []

    # While loop
    while True:
    
        # draw rectangles, select ROI, open new window
        rect_box = cv2.selectROI('MultiTracker', frame)
        rects = append(rect_box)
        colors.append((randint(64,255), randint(64,255), randint(64,255)))
        print('press q to stop selecting boxes and start multitracking')
        print('Press any key to select another box')
        
        
        
        #close window
        if cv2.waitKey(0) & oxFF == 113==q
            break
        
    # print message
    print(f'Select boxes and {rects}')
    
    
    # Create multitracker
    multitracker = cv2MultiTracker_create()    
    
    # Initialize multitracker
    for rect_box in rects:
        multitracker.add(tracker_name(tracker_types), frame, rect_box)
    
    #Video and Tracker
    # while loop
    while cap.isOpened():
        
        # update location objects
        success, boxes = multitracker.update(frame)
        
        # draw the objectes tracked
        for i, newbox in enumerate(boxes):
            pts1 = (int(newbox[0]), int(newbox[1]))
            pts2 = (int(newbox[0] + newbox[2]),int(newbox[1] + newbox[3]))
            cv2.rectangle(frame, pts1, pts2, colors[i], 2, 1)
                    
        # display frame
        cv2.imshow('Multitracker', frame)
    
        # Close the frame
        if cv2.waitKey(20) & 0xFF == 27:
            break
    
# Release and Destroy
cap.release()
cv2.destroyAllWindows()


# In[ ]:




