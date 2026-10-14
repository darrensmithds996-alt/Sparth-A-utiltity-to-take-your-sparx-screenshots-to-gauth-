import pyautogui
import pyperclip
import keyboard
import webbrowser

SOURCE_URL_PREFIX = "https://maths.sparx-learning.com/student/"
TARGET_URL = "https://www.gauthmath.com/"
TARGET_URL_PREFIX = TARGET_URL

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0

stop_flag = False


def stop_script():
    global stop_flag
    stop_flag = True


keyboard.add_hotkey("f8", stop_script)


def reset_devtools():
    pyautogui.hotkey("ctrl", "shift", "c")
    pyautogui.sleep(0.05)
    pyautogui.press("f12")


def get_current_url():
    pyautogui.hotkey("ctrl", "l")
    pyautogui.sleep(0.03)
    pyautogui.hotkey("ctrl", "c")
    pyautogui.sleep(0.03)
    return pyperclip.paste()


def find_tab_with_prefix(prefix, max_tabs=20):
    for _ in range(max_tabs):
        if stop_flag:
            return False

        if get_current_url().startswith(prefix):
            return True

        pyautogui.hotkey("ctrl", "tab")
        pyautogui.sleep(0.05)

    return False


def focus_top():
    w, _ = pyautogui.size()
    pyautogui.moveTo(w // 2, 5)
    pyautogui.click()


def focus_middle():
    w, h = pyautogui.size()
    pyautogui.moveTo(w // 2, h // 2)
    pyautogui.click()


def run_process():
    global stop_flag
    stop_flag = False

    reset_devtools()

    focus_top()

    if not find_tab_with_prefix(SOURCE_URL_PREFIX):
        return

    target_found = find_tab_with_prefix(TARGET_URL_PREFIX)

    if not target_found:
        webbrowser.open(TARGET_URL)
        pyautogui.sleep(1.5)
        find_tab_with_prefix(TARGET_URL_PREFIX)

    if stop_flag:
        return

    pyautogui.hotkey("ctrl", "shift", "tab")
    pyautogui.sleep(0.05)

    pyautogui.press("f11")
    pyautogui.sleep(0.05)

    pyautogui.hotkey("win", "printscreen")
    pyautogui.sleep(0.5)

    focus_top()
    pyautogui.press("enter")

    pyautogui.hotkey("ctrl", "tab")
    pyautogui.sleep(0.05)

    focus_middle()

    pyautogui.press("/")
    pyautogui.sleep(0.03)

    pyautogui.hotkey("ctrl", "v")

    pyautogui.press("f11")
    pyautogui.sleep(0.05)


keyboard.add_hotkey("ctrl+shift+u", run_process)

print("Ready. CTRL+SHIFT+U to run, F8 to stop.")
keyboard.wait()