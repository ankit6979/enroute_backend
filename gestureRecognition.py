import cv2
import imutils
import numpy as np

bg = None

def run_avg(image, accumWeight):
    global bg
    if bg is None:
        bg = image.copy().astype("float")
        return
    cv2.accumulateWeighted(image, bg, accumWeight)

def segment(image):
    global bg
    diff = cv2.absdiff(bg.astype("uint8"), image)
    return diff
    #thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
    #(cnts, _) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #if len(cnts) == 0:
        #return
    #else:
        #segmented = max(cnts, key=cv2.contourArea)
        #return (thresholded, segmented)

if __name__ == "__main__":
    accumWeight = 0.5
    cap = cv2.VideoCapture(0)
    num_frames = 0
    while(True):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([0, 70, 50])
        upper_hsv = np.array([30,255,255])
        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
        blur = cv2.medianBlur(mask,5)
        cv2.imshow("mask", mask)
        if num_frames < 30:
            run_avg(frame, accumWeight)
        else:
            diff = segment(frame)
            cv2.imshow("image", diff)
        num_frames += 1
        #cv2.imshow("Video Feed", clone)
        keypress = cv2.waitKey(1) & 0xFF
        if keypress == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
