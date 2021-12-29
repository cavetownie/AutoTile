import win32gui, win32ui, win32con
import numpy as np

class winInteract:
    def __init__(self, name=None):
        self.name = name
        """
        Find the process handler for the winHwnd using the name
        specified by user in main. 
        """
        self.winHwnd = win32gui.FindWindowEx(None,None,None,self.name)
        if not self.winHwnd:
            raise ValueError("Window not found!")
            exit(-1)
         
        """
        Gets the size of the winHwnd based on the handler
        using the GetWindowRect api call. Use this for the
        width and size of the image
        """
        self.pos = win32gui.GetWindowRect(self.winHwnd)
        self.height = self.pos[3] - self.pos[1]
        self.width = self.pos[2] - self.pos[0]

        self.left, self.top, self.right, self.bot = self.pos

        """
        Set the process as the foreground window to ensure
        the screenshots are taken correctly.
        """
        win32gui.SetForegroundWindow(self.winHwnd)

    def liveScreen(self):
        hdesktop = win32gui.GetDesktopWindow()
        hwndDC = win32gui.GetWindowDC(hdesktop)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(mfcDC, self.width, self.height)

        saveDC.SelectObject(dataBitMap)
        saveDC.BitBlt((0, 0), (self.width, self.height), mfcDC, (self.left, self.top), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)

        """
        Shape the image based on its proportions
        """
        img = np.fromstring(signedIntsArray, dtype="uint8")
        img.shape = (self.height, self.width, 4)

        """
        Free ressources not used anymore
        """
        win32gui.DeleteObject(dataBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hdesktop, hwndDC)

        """
        Drops the alpha channel (R,G,B,A) => (R,G,B)
        Otherwise OpenCV will throw errors
        """
        img = img[...,:3]

        """
        Match template in OpenCV wants integers, but as of now
        we're returning tuples, the next line is meant to deal
        with this. For more information see the discussion here:
        https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        """
        img = np.ascontiguousarray(img)

        return img