import cv2
import numpy as np

class cvClick:
    imageW = 0
    imageH = 0
    needle_img = None

    def __init__(self, imagePath=None, method=cv2.TM_CCOEFF_NORMED):
        self.needle_img = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)


        """
        Following code once again makes sure
        that the image is ready for parsing by
        cv2's match template
        """
        self.needle_img = self.needle_img[...,:3]

        self.imageW = self.needle_img.shape[1]
        self.imageH = self.needle_img.shape[0]


        self.method = cv2.TM_SQDIFF_NORMED 
        self.threshold = 0.125


    def locateTiles(self, dataWinCap, debug_mode=None):

        result = cv2.matchTemplate(dataWinCap, self.needle_img, self.method)

        locations = np.where(result <= self.threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.imageW, self.imageH]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)

        points = []
        if len(rectangles):
            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:

                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)

                # Save the points
                points.append((center_x, center_y))

        return points