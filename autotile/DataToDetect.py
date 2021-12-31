import cv2
import numpy as np

class cvClick:
    imageW = 0
    imageH = 0
    needle_img = None

    def __init__(self, imagePath=None, threshold=0.165, method=cv2.TM_SQDIFF_NORMED):
        self.needle_img = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)

        """
        Following code once again makes sure
        that the image is ready for parsing by
        cv2's match template
        """
        self.needle_img = self.needle_img[...,:3]

        self.imageW = self.needle_img.shape[1]
        self.imageH = self.needle_img.shape[0]

        self.threshold = threshold
        self.method = method

    def locateTiles(self, dataWinCap, debug_mode=None):
        result = cv2.matchTemplate(dataWinCap, self.needle_img, self.method)

        # Create a list of locations
        locations = np.where(result <= self.threshold) 
        locations = zip(*locations[::-1])

        """
        Determine rectangles based
        on the locations
        """
        rectangles = [(int(loc[0]), int(loc[1]), self.imageW, self.imageH) for loc in locations]

        """
        Return points to the center
        of those rectangles
        """
        if len(rectangles):
            points = [(x+int(w/2), y+int(h/2)) for (x,y,w,h) in rectangles]
            return points
        else:
            return []
