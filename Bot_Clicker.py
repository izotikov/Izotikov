import pyautogui as auto
import keyboard as key
from keyboard import press
import time

start_key = input("Клавиша запуска:")
stop_key = input("Клавиша остановки:")
count = 0
while True:
    if key.is_pressed(start_key):
        count += 1
    elif key.is_pressed(stop_key):
        break
    elif count >= 1:
        auto.tripleClick()
        time.sleep(0.1)
        press('enter')
        time.sleep(0.1)
