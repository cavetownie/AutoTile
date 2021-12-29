import cv2
import numpy as np

class cvClick:
    imageW = 0
    imageH = 0

    def __init__(self, imagePath=None, method=cv2.TM_CCOEFF_NORMED):

        self.needle_img = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)

        """
        Following code once again makes sure
        that the image is ready for parsing by
        cv2's match template
        """
        self.needle_img = self.needle_img[...,:3]
        self.needle_img = np.ascontiguousarray(self.needle_img)

        self.imageW = self.needle_img.shape[1]
        self.imageH = self.needle_img.shape[0]

        self.method = method
        self.threshold = 0.7

    def locateTiles(self, dataWinCap, debug_mode=None):
        result = cv2.matchTemplate(dataWinCap, self.needle_img, self.method)

        locations = np.where(result >= self.threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.imageW, self.imageH]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=5, eps=0.5)
        #print(rectangles)

        points = []
        if len(rectangles):
            #print('Found needle.')

            line_color = (0, 255, 0)
            line_type = cv2.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv2.MARKER_CROSS

            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:

                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                # Save the points
                points.append((center_x, center_y))


        return points