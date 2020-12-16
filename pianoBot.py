import win32api, win32con
import time
import pyautogui as gui
import keyboard

xPositions = (
  (415, 's'),
  (600, 'd'),
  (790, 'f'),
  (980, 'space'),
  (1160, 'j'),
  (1350, 'k'),
  (1545, 'l')
)

y = 933
gui.PAUSE = 0.007 # Delay between gui commands (e.g keyDown/keyUp, press, ...)
print('Piano Bot starting...')
time.sleep(1)

# Can be used to use mouse to press the notes instead of keyboard (slower)
def clickPos(x, y):
  win32api.SetCursorPos((x, y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0 , 0)
  time.sleep(0.01)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0 , 0)

def pressKey(key):
    gui.keyDown(key)
    gui.keyUp(key)

def shouldClickPos(x, y):
  threshold = 150
  red, green, blue = gui.pixel(x, y)
  return red >= threshold or blue >= threshold or green >= threshold 

while keyboard.is_pressed('x') == False:
  if shouldClickPos(xPositions[0][0], y):
    pressKey(xPositions[0][1])

  if shouldClickPos(xPositions[1][0], y):
    pressKey(xPositions[1][1])

  if shouldClickPos(xPositions[2][0], y):
    pressKey(xPositions[2][1])

  if shouldClickPos(xPositions[3][0], y):
    pressKey(xPositions[3][1])

  if shouldClickPos(xPositions[4][0], y):
    pressKey(xPositions[4][1])

  if shouldClickPos(xPositions[5][0], y):
    pressKey(xPositions[5][1])

  if shouldClickPos(xPositions[6][0], y):
    pressKey(xPositions[6][1])

print('Piano Bot terminated.')

