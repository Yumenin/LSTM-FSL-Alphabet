import os
import cv2
import string



DATASET_DIR = './data'

#if not os.path.exists(DATASET_DIR):
#    os.makedirs(DATASET_DIR)

#CLASSES = list(string.ascii_uppercase) # 26 alphabets
#DATASET_SIZE = 300


# for alphabet in CLASSES:
#    if not os.path.exists(os.path.join(DATASET_DIR, alphabet)):
#        os.makedirs(os.path.join(DATASET_DIR, alphabet))
#
#    print(f'Collecting data for class {alphabet}')


#    isComplete = False
#    cap = cv2.VideoCapture(0)
#    while True:
#        ret, frame = cap.read()
#        cv2.putText(frame, 'If ready to record, Press "Q"', (100,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 3, cv2.LINE_AA)
#        cv2.imshow('frame', frame)
#        if cv2.waitKey(25) == ord('q'):
#            break
#    
#    counter = 0
#
#    while counter < DATASET_SIZE:
#        ret,frame = cap.read()
#        cv2.imshow('frame', frame)
#        cv2.waitKey(25)
#        cv2.imwrite(os.path.join(DATASET_DIR, alphabet, f'{counter}.jpg'), frame)
#        counter+=1

#cap.release()
#cv2.destroyAllWindows()