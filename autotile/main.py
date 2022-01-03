import pyautogui as pg
import os

# Custom imports
from ScreenToData import winInteract
from DataToDetect import cvClick

"""
The driver code ensures that
the results returned by opencv
is acted upon. As of now there's
just keybindings used for the current
game. Some games might require mouse
clicks instead. So the driver code would
be replaced.
"""
def driver(clickData):
      # Save the X-coordinate to determine what to press
      pos = clickData[0][0]

      if 30 < pos and pos < 180:
         pg.press("A")
         print("[A] was pressed")
      elif 180 < pos and pos < 300:
         pg.press("S")
         print("[S] was pressed")
      elif 300 < pos and pos < 420:
         pg.press("D")
         print("[D] was pressed")
      elif 430 < pos and pos < 600:
         pg.press("F")
         print("[F] was pressed")
   

def main():
   screenHandler = winInteract(game, cutoff=1.75)

   """
   Use two clicks to openCV as there's
   two different clicks. Long and short
   """
   longPath = os.path.join(srcPath, "..\\images", "Capture.png")
   tilePath = os.path.join(srcPath, "..\\images", "522.png")

   cvHandlerLong = cvClick(longPath) # Initializes needle image
   cvHandlerTile = cvClick(tilePath) 

   # Faster than while-True
   while 1:
      tileData = screenHandler.liveScreen()

      # Save the X- and Y-coordinates for the tiles
      joinedCoords = cvHandlerLong.locateTiles(tileData) + cvHandlerTile.locateTiles(tileData)

      if len(joinedCoords):
         clickStack = sorted(joinedCoords,key=lambda x: x[1], reverse=True) 
         driver(clickStack)


if __name__ == "__main__":
   game = "Magic Music Tiles - Guitar & Piano Games"
   __file__ = "main.py"
   srcPath = os.path.dirname(os.path.realpath(__file__))

   main()
