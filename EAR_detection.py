from scipy.spatial import distance as dist
from imutils import face_utils
import imutils
import time
import dlib
import cv2

thresh = 0.24
consecutive_frames = 10
counter = 0
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("eye_predictor.dat")

def eye_aspect_ratio(eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

def sleep_prediction(frame):
        global counter
        global consecutive_frames
        global thresh
        rects = detector(frame, 0)
        for rect in rects:
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)
                leftEye = shape[0:6]
                rightEye = shape[6:12]
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)
                ear = (leftEAR + rightEAR) / 2.0
                if ear < thresh:
                        counter += 1
                else:
                        counter = 0
                if(counter>=consecutive_frames):
                        return True
        return False

if __name__ == main():
        cap = cv2.VideoCapture(0)
        while True:
                ret, frame = cap.read()
                frame =cv2.resize(frame, (640,480), interpolation = cv2.INTER_LINEAR)
                print(sleep_prediction(frame))
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                        break
        cap.release()
        

