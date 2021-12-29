import pyautogui as pg
from ScreenToData import winInteract
from DataToDetect import cvClick


def main():
   screenHandler = winInteract(game)
   cvHandlerLong = cvClick("Capture.png")
   cvHandlerTile = cvClick("temp.png")

   while 1:
      tileData = screenHandler.liveScreen()

      # Save the X- and Y-coordinates for the tiles
      joinedCoords = cvHandlerLong.locateTiles(tileData) + cvHandlerTile.locateTiles(tileData)

      if len(joinedCoords):
         clickStack = sorted(joinedCoords,key=lambda x: x[1], reverse=True) 
         pos = clickStack[0][0]

         if 30 < pos and pos < 150:
            pg.press("A")
         if 160 < pos and pos < 300:
            pg.press("S")
         if 310 < pos and pos < 400:
            pg.press("D")
         if 410 < pos and pos < 600:
            pg.press("F")

if __name__ == "__main__":
   game = "Magic Music Tiles - Guitar & Piano Games"
   main()
