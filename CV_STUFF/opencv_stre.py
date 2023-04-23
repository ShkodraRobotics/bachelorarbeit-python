import cv2 as cv
import numpy
class Vid:
    def __init__(self,win,wid,hei):

        self.cap = cv.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, wid)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hei)







    def update_frame(self):
        # Read the next frame from the video stream
        _, frame = self.cap.read()

        # Convert the frame to a PhotoImage object
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        '''image = tk.PhotoImage(image=frame)

        # Update the label with the new image
        self.label.config(image=image)
        self.label.image = image

        # Schedule the next update
        self.frame.after(10, self.update_frame)'''
        return frame























