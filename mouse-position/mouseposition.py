import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})")  
        time.sleep(0.1)  # Sleep for a short amount of time to make the output readable
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
