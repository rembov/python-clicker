import pyautogui


def select(x):
    if x == 1:
        pyautogui.moveTo(3840, 2160)
    if x == 2:
        pyautogui.moveTo(1920, 1080)
    if x == 3:
        pyautogui.moveTo(7280, 720)
    if x == 4:
        pyautogui.moveTo(960, 540)
    if x == 5:
        pyautogui.moveTo(840, 525)
    if x == 6:
        pyautogui.moveTo(668, 384)


# pyautogui.moveTo(960, 580)


def power():
    while True:
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()


if __name__ == "__main__":
    a = int(input(
        "Выберите разрешение: \n 1.7680 x 4320 (8K)\n 2.3840 x 2160 (4K UHD) \n 3.2560 x 1440 (2.5K) \n "
        "4.1920 x 1080 (Full HD) \n 5. 1680 x 1050 (WSXGA+) \n 6.1336 x 768 (WXGA) \n"))
    select(a)
    power()
    