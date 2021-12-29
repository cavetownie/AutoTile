import pyautogui as pg
from ScreenToData import winInteract
from DataToDetect import cvClick



"""
To DO:

1. Fix positioning, so it's automatic
2. Test cases where you take a picture
of white with some black rectangles on it
you want your CV model to see these and 
return you the points. When you have
the code that does this, incorporate it 
into the DataToDetect class. Hopefully
then it'll work alway. 

3. Make it able to distinguish between
holding and clicking

4. Comment all the opencv code

"""


game = "Magic Music Tiles - Guitar & Piano Games"


def main():
    screenHandler = winInteract(game)
    cvHandler = cvClick("Capture.png")

    while True:
        tileData = screenHandler.liveScreen()
        a = cvHandler.locateTiles(tileData)

        try:
            pos = a[0][0]+620, a[0][1]
            print(pos)
            A = 699
            S = 833
            D = 967
            F = 1101

            if pos[0] == A:
               pg.press("A") 
            if pos[0] == S:
               pg.press("S") 
            if pos[0] == D:
               pg.press("D") 
            if pos[0] == F:
               pg.press("F")
            print(pos)

        except:
            pass

if __name__ == "__main__":
    main()
