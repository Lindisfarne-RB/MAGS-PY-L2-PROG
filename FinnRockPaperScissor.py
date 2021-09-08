import os
import cv2
#sudo pip3 install opencv-python

import numpy as np
import matplotlib.pyplot as plt
import time
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Dense, MaxPool2D, Dropout, Flatten, Conv2D, GlobalAveragePooling2D, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from random import choice, shuffle

from scipy import stats as st

from collections import deque

cap = cv2.VideoCapture(0)
box_size = 234
width = int(cap.get(3))

# Specify the number of attempts you want. This means best of 5.
attempts = 5

# Initially the moves will be `nothing`
computer_move_name = "nothing"
final_user_move = "nothing"

label_names = ['nothing', 'paper', 'rock', 'scissor']

# All scores are 0 at the start.
computer_score, user_score = 0, 0

# The default color of bounding box is Blue
rect_color = (255, 0, 0)

# This variable remembers if the hand is inside the box or not.
hand_inside = False

# At each iteration we will decrease the total_attempts value by 1
total_attempts = attempts

# We will only consider predictions having confidence above this threshold.
confidence_threshold = 0.70

# Instead of working on a single prediction, we will take the mode of 5 predictions by using a deque object
# This way even if we face a false positive, we would easily ignore it
smooth_factor = 5

# Our initial deque list will have 'nothing' repeated 5 times.
de = deque(['nothing'] * 5, maxlen=smooth_factor)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.namedWindow("Rock Paper Scissors", cv2.WINDOW_NORMAL)

    # extract the region of image within the user rectangle
    roi = frame[5: box_size - 5, width - box_size + 5: width - 5]

    roi = np.array([roi]).astype('float64') / 255.0

    # Predict the move made
    pred = model.predict(roi)

    # Get the index of the predicted class
    move_code = np.argmax(pred[0])

    # Get the class name of the predicted class
    user_move = label_names[move_code]

    # Get the confidence of the predicted class
    prob = np.max(pred[0])

    # Make sure the probability is above our defined threshold
    if prob >= confidence_threshold:

        # Now add the move to deque list from left
        de.appendleft(user_move)

        # Get the mode i.e. which class has occured more frequently in the last 5 moves.
        try:
            final_user_move = st.mode(de)[0][0]

        except StatisticsError:
            print('Stats error')
            continue

        # If nothing is not true and hand_inside is False then proceed.
        # Basically the hand_inside variable is helping us to not repeatedly predict during the loop
        # So now the user has to take his hands out of the box for every new prediction.

        if final_user_move != "nothing" and hand_inside == False:

            # Set hand inside to True
            hand_inside = True

            # Get Computer's move and then get the winner.
            computer_move_name = choice(['rock', 'paper', 'scissor'])
            winner = findout_winner(final_user_move, computer_move_name)

            # Display the computer's move
            display_computer_move(computer_move_name, frame)

            # Subtract one attempt
            total_attempts -= 1

            # If winner is computer then it gets points and vice versa.
            # We're also changing the color of rectangle based on who wins the round.

            if winner == "Computer":
                computer_score += 1
                rect_color = (0, 0, 255)

            elif winner == "User":
                user_score += 1;
                rect_color = (0, 250, 0)

            elif winner == "Tie":
                rect_color = (255, 250, 255)

            # If all the attempts are up then find our the winner
            if total_attempts == 0:

                play_again = show_winner(user_score, computer_score)

                # If the user pressed Enter then restart the game by re initializing all variables
                if play_again:
                    user_score, computer_score, total_attempts = 0, 0, attempts

                # Otherwise quit the program.
                else:
                    break

        # Display images when the hand is inside the box even when hand_inside variable is True.
        elif final_user_move != "nothing" and hand_inside == True:
            display_computer_move(computer_move_name, frame)

        # If class is nothing then hand_inside becomes False
        elif final_user_move == 'nothing':
            hand_inside = False
            rect_color = (255, 0, 0)

            # This is where all annotation is happening.

    cv2.putText(frame, "Your Move: " + final_user_move,
                (420, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, "Computer's Move: " + computer_move_name,
                (2, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, "Your Score: " + str(user_score),
                (420, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, "Computer Score: " + str(computer_score),
                (2, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, "Attempts left: {}".format(total_attempts), (190, 400), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                (100, 2, 255), 1, cv2.LINE_AA)

    cv2.rectangle(frame, (width - box_size, 0), (width, box_size), rect_color, 2)

    # Display the image
    cv2.imshow("Rock Paper Scissors", frame)

    # Exit if 'q' is pressed
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

# Relase the camera and destroy all windows.
cap.release()
cv2.destroyAllWindows()