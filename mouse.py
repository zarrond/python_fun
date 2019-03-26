import win32api
import win32con
from debug_tools2 import dprint as d
# .cpython-37

def click(x,y):
    win32api.SetCursorPos((x,y))
    
    
    d(win32con.MOUSEEVENTF_LEFTDOWN)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
d(10)    
click(10,100)