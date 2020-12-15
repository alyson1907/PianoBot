import win32api, win32con
import win32com.client
import time
from pyautogui import *
import pyautogui as gui
import keyboard
import random
shell = win32com.client.Dispatch("WScript.Shell")
xPositions = [
  [415, 's'],
  [600, 'd'],
  [790, 'f'],
  [980, 'space'],
  [1160, 'j'],
  [1350, 'k'],
  [1545, 'l']
]
# xPositions = [
#   415,
#   600,
#   790,
#   980,
#   1160,
#   1350,
#   1545,
# ]
y = 933
gui.PAUSE = 0.007
print('Piano Bot starting...')
time.sleep(1)

def clickPos(x, y):
  win32api.SetCursorPos((x, y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0 , 0)
  time.sleep(0.05)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0 , 0)

def pressKey(key):
  for k in key:
    gui.keyDown(k)
  for k in key:
    gui.keyUp(k)

def shouldClickPos(x, y):
  threshold = 100
  red, green, blue = gui.pixel(x, y)
  return (red >= threshold and green >= threshold) or (red >= threshold and blue >= threshold) or (green >= threshold and blue >= threshold)

while keyboard.is_pressed('x') == False:
  toPress = []
  for x, key in xPositions:
    if shouldClickPos(x, y):
      toPress.append(key)
  pressKey(toPress)

print('Piano Bot terminated.')

