import os 
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt
import pickle

DATASET_DIR = './data-2/train'
DATASET_DIR = './data'

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

data = []
labels = []

for dir in os.listdir(DATASET_DIR):
    for img_path in os.listdir(os.path.join(DATASET_DIR, dir)):
        data_out = []
        img = cv2.imread(os.path.join(DATASET_DIR, dir, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                #mp_drawing.draw_landmarks(
                #    img_rgb, # image to draw on
                #    hand_landmarks, # output
                #    mp_hands.HAND_CONNECTIONS, # draw hand connections
                #    mp_drawing_styles.get_default_hand_landmarks_style(),
                #    mp_drawing_styles.get_default_hand_connections_style()
                #)
                print(hand_landmarks)
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_out.append(x)
                    data_out.append(y)

            data.append(data_out)
            labels.append(dir)

        #plt.figure()
        #plt.imshow(img_rgb)
else:
    print("Finished extracting features from Class {dir}")

#plt.show()
f = open('alphabet.pickle', 'wb') # write as bytes
pickle.dump({'data': data, 'labels': labels}, f)
f.close()