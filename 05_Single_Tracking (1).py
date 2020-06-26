#!/usr/bin/env python
# coding: utf-8

# ### Import Libraries

# In[1]:


import cv2


# ### Define our tracker

# In[2]:


def ask_for_tracker():
    print('Hi, ! What tracker API would you like to use?')
    print('Enter 0 for Boosting: ')
    print('Enter 1 for MIL: ')
    print('Enter 2 for KCF: ')
    print('print 3 for TLD: ')
    print('Enter 4 for MEDIANFLOW: ')
    print('Enter 5 for GOTURN: ')
    print('Enter 6 for MOSSE: ')
    print('Enter 7 for CSRT: ')
    
    choice = input('Please select your tracker: ')
    if choice == '0':
        trackerchoice = cv2.TrackerBoosting_create()
    if choice == '1':
        trackerchoice = cv2.TrackerMIL_create()
    if choice == '2':
        trackerchoice = cv2.TrackerKCF_create()
    if choice == '3':
        trackerchoice = cv2.TrackerTLD_create()
    if choice == '4':
        trackerchoice = cv2.TrackerMedianFlow_create()
    if choice == '5':
        trackerchoice = cv2.TrackerGOTURN_create()
    if choice == '6':
        trackerchoice = cv2.TrackerMOSSE_create()
    if choice == '7':
        trackerchoice = cv2.TrackerCSRT_create()
        
    return trackerchoice


# ### It's a Kind of Magic

# In[3]:


# Tracker
tracker = ask_for_tracker()

# Tracker name
tracker_name = str(tracker).split()[0][1:]

# Capture the Video
cap = cv2.VideoCapture('run.mp4')

# Read the first frame
ret, frame = cap.read()

# Select our ROI
Roi = cv2.selectROI(frame, False)

# Initialize tracker
ret = tracker.init(frame, Roi)


# while Loop
while True:

    # Read the capture
    ret, frame = cap.read()
    
    # update tracker
    success, roi = tracker.update(frame)
    
    # roi -> from tuple to int
    (x,y,w,h) = tuple(map(int, roi))
    
    # Draw rects as tracker moves
    if success:
        
        # Sucess on tracking
        pts1 = (x,y)
        pts2 = (x +w, y+h)
        cv2.rectangle(frame, pts1, pts2, (255,125,25), 3)
    # else
    else:
        
    
        # Failure on tracking
        cv2.putText(frame, 'Fail to track the object', (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (25,125,255), 3)
        
    # Display Tracker
    cv2.putText(frame, tracker_name, (20,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 3)
    
    # Display result
    cv2.imshow(tracker_name, frame)
        
    # Exit with Esc button
    if cv2.waitKey(50) & 0xFF == 27:
        break
    
    
# Release the Capture & Destroy All Windows
cap.release()
cv2.destroyALLWindows()



