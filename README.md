# Sparth-A-utiltity-to-take-your-sparx-screenshots-to-gauth-

A Python automation script that switches between Sparx Learning and GauthMath, takes a screenshot of a Sparx question, and sends it to GauthMath using keyboard and mouse automation.

## Requirements

- Windows
- Python 3
- A supported browser with Sparx Learning and GauthMath
- Slash to Search extension, configured so `/` opens GauthMath search
- Cookie Clear extension, installed and enabled
- The Python packages `pyautogui`, `pyperclip`, and `keyboard`

## Installation

1. Install Python 3 if you haven't already.
2. Download or clone this repository.
3. Open Command Prompt in the project folder.
4. Install the required Python packages:

```bash
py -m pip install pyautogui pyperclip keyboard
```

## Required Extension: Slash to Search

The script uses `/` to open the GauthMath search interface. You must have the Slash to Search extension installed and configured for this to work.

Configure `/` to open GauthMath search before running the script.

## Required Extension: Cookie Clear

Cookie Clear is a required part of this setup.

Repository: https://github.com/AlphaKennyBody12/Cookie-clear-Can-be-used-to-bypass-Gauth-limited-uses-

To install it:

1. Open the repository on GitHub.
2. Click Code, then Download ZIP.
3. Extract the downloaded ZIP file.
4. Find the extracted extension folder and check that it contains `manifest.json`.
5. Open your browser's extensions page:
   - Chrome: `chrome://extensions`
   - Edge: `edge://extensions`
6. Enable Developer mode.
7. Click Load unpacked.
8. Select the extracted extension folder.
9. Check that the extension is enabled.

Cookie Clear must be installed and enabled before running the script. Make sure you use extensions in accordance with the relevant websites' terms and conditions.

## Setup

1. Open Sparx Learning and navigate to the question you want to capture.
2. Open GauthMath in another tab in the same browser window.
3. Keep both tabs open. Sparx should be among the first two tabs for the script's initial search. If GauthMath isn't found, the script opens it and searches up to three tabs.
4. Make sure Slash to Search is configured and Cookie Clear is installed and enabled.
5. Run the Python script.

## Keyboard Shortcuts

- `Ctrl + Shift + U`: Start the automation.
- `F8`: Request that the script stop.
- `F11`: Used by the script to toggle fullscreen.
- `Win + Print Screen`: Takes a screenshot and saves it to the Windows Screenshots folder.
- `/`: Opens GauthMath search through Slash to Search.

## What the Script Does

1. Resets some browser developer-tools state using keyboard shortcuts.
2. Searches the open tabs for Sparx Learning and GauthMath.
3. Opens GauthMath if it cannot find an existing GauthMath tab.
4. Switches to the Sparx tab.
5. Toggles fullscreen and captures a screenshot using `Win + Print Screen`.
6. Switches to the GauthMath tab.
7. Uses `/` to open the search interface and pastes the clipboard contents.
8. Waits eight seconds for the page to respond.
9. Checks the visible page text for certain offer or limit-related phrases. If its conditions are met, it sends `Ctrl + Shift + K`. The result depends on your browser and its settings.

The script relies on screen coordinates, keyboard shortcuts, browser tabs, and clipboard contents. It does not independently verify that every action succeeded.

## Configuration

You can adjust these variables near the top of the Python file:

```python
SOURCE_URL_PREFIX = "https://maths.sparx-learning.com/student/"
TARGET_URL = "https://www.gauthmath.com/"
TARGET_URL_PREFIX = "https://www.gauthmath.com"
```

- `SOURCE_URL_PREFIX`: Identifies the Sparx Learning tab.
- `TARGET_URL`: The page opened if GauthMath is not found.
- `TARGET_URL_PREFIX`: Identifies the GauthMath tab.

You can also adjust the timing settings:

```python
pyautogui.PAUSE = 0.01
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
```

If actions happen too quickly on your computer, increase the pauses or waits in the script.

## Bookwork Checks

Screenshots taken with `Win + Print Screen` are normally saved in:

```text
Pictures\Screenshots
```

To locate a screenshot:

1. Open File Explorer.
2. Go to Pictures, then Screenshots.
3. Find the screenshot of the relevant Sparx question.
4. Open GauthMath and use its image-upload option to upload the screenshot if you need to complete a bookwork check.

You may need to select the correct screenshot manually. The script does not automatically locate and upload screenshots from the Screenshots folder.

## Important Notes

- Keep the browser window visible while the script runs.
- Avoid moving the mouse or typing while automation is in progress.
- The script clicks the middle and top of the screen, so it may interfere with other open applications.
- `F8` requests a stop, but the script may not stop instantly if it is already inside an operation.
- PyAutoGUI's failsafe is enabled. Moving the mouse to the top-left corner of the screen can trigger it.
- Cookie Clear is required by this setup, but the Python script does not directly control its extension interface.
- The script's `Ctrl + Shift + K` shortcut depends on your browser and settings. The code does not confirm that it cleared anything.

## Troubleshooting

### The script says "Sparx tab not found."

- Check that Sparx Learning is open.
- Make sure its URL begins with `https://maths.sparx-learning.com/student/`.
- Keep it among the first two tabs when starting the script.

### The script says "GauthMath tab not found."

- Check that GauthMath is open and that its URL begins with `https://www.gauthmath.com`.
- Make sure the browser allows the site to open.
- The script searches up to three tabs after attempting to open GauthMath.

### The screenshot isn't sent correctly

- Check that Slash to Search is installed and configured to use `/`.
- Make sure the clipboard contains the expected screenshot data.
- Try increasing the pauses if your computer is slow.

### Cookie Clear doesn't work

- Check that the extension folder contains `manifest.json`.
- Make sure you loaded the correct folder using Load unpacked.
- Confirm that the extension is enabled in your browser.

### The script behaves unpredictably

- Keep the browser in the foreground.
- Avoid interacting with the computer while the script runs.
- Increase the sleep durations in the script if needed.

## Stopping the Script

Press `F8` to request a stop. If the script becomes unresponsive, use `Ctrl + C` in the Command Prompt window running it.

## Disclaimer

This project is provided for educational and personal automation purposes. Use it responsibly and follow the terms and conditions of the services and extensions involved.
