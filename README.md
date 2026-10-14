# Sparth-A-utiltity-to-take-your-sparx-screenshots-to-gauth-

A Python automation script that switches between Sparx Learning and the Gauth website, captures a screenshot, and performs a sequence of keyboard and mouse actions.

## Requirements

- Windows
- Python 3
- A browser with Sparx Learning and the Gauth website available
- The Slash to Search browser extension installed and configured to open the Gauth search interface when `/` is pressed
- The Python packages `pyautogui`, `pyperclip`, and `keyboard`

## Installation

Install the required Python packages:

```bash
py -m pip install pyautogui pyperclip keyboard
```

Save the script as `sparx_helper.py` or another `.py` filename.

## Extension Setup

Before running the script, install the Slash to Search browser extension.

1. Open your browser's extension store and search for Slash to Search.
2. Install the extension and enable it.
3. Configure it so that pressing `/` opens the search interface on the Gauth website.
4. Open the Gauth website and test that pressing `/` activates the search interface.

If you downloaded the extension as a ZIP file instead, follow the instructions in the next section.

The script relies on this extension to open the search interface. Without it, pressing `/` may not produce the expected result.

## Recommended Additional Extension

You may also want to check out Cookie-clear, another project I made a while ago on an account I lost:

https://github.com/AlphaKennyBody12/Cookie-clear-Can-be-used-to-bypass-Gauth-limited-uses-

### Should You Install It?

If you want to try the project:

### Step 1: Download and Extract the ZIP

1. Download the extension's ZIP file from https://github.com/AlphaKennyBody12/Cookie-clear-Can-be-used-to-bypass-Gauth-limited-uses-.
2. Open your Downloads folder.
3. Right-click the ZIP file and select `Extract All...`.
4. Choose a location and extract the files.
5. Open the extracted folder and check that it contains a `manifest.json` file.

Important: If `manifest.json` is inside another folder, select that inner folder when loading the extension, rather than its parent folder.

### Step 2: Open Your Browser's Extensions Page

For Google Chrome or any other Chromium Browser:

1. Enter `broswer name://extensions` in the address bar.
2. Press Enter.
3. Turn on Developer mode using the toggle in the top-right corner.

For Microsoft Edge:

1. Enter `edge://extensions` in the address bar.
2. Press Enter.
3. Enable Developer mode.

### Step 3: Load the Extension

1. Click `Load unpacked`.
2. Navigate to the folder containing the extracted extension files.
3. Select that folder and click `Select Folder`.
4. The extension should appear in your extensions list.
5. If you want to change the shortcut for activating the extension, go to keyboard shortcuts on the left side and scroll down until you find the extension's section, and change the shortcut.
### Step 4: Check That It Works

1. Make sure the extension is enabled.
2. Open the Gauth website.
3. Press the shortcut that you have assigned to activate the extension.

If the repository provides a ZIP containing source code rather than a browser extension, the files may need a different installation process. Check the repository's README before proceeding.

Cookie-clear is a separate project and is not required for Sparth to run. Review its source code and permissions before installing it.

## Setup

1. Open your browser and sign in to Sparx Learning.
2. Make sure a browser tab has a URL beginning with `https://maths.sparx-learning.com/student/`.
3. Open the Gauth website in the next tab.
4. Make sure the Slash to Search extension is installed and working.
5. Keep both tabs open next to each other, in their own window.
6. Run the script:

   ```bash
   py sparx_helper.py
   ```

7. A new blank window opens, and the script prints:

   ```text
   Ready. CTRL+SHIFT+U to run, F8 to stop.
   ```

8. Press `Ctrl+Shift+U` to start the automation.

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+Shift+U` | Starts the automation sequence. |
| `F8` | Requests that the current sequence stop. |
| `/` | Opens the Gauth search interface through the Slash to Search extension when the correct page is focused. |
| PyAutoGUI failsafe | Move the mouse to the top-left corner of the screen to trigger PyAutoGUI's failsafe. |

## What the Script Does

When you press `Ctrl+Shift+U`, the script:

1. Resets its DevTools-related keyboard state.
2. Clicks near the top-centre of the screen to focus the browser.
3. Cycles through browser tabs, checking their URLs for the Sparx Learning student page.
4. Searches for a Gauth website tab. If one is not found, it opens Gauth in the browser.
5. Switches to the adjacent tab and presses `F11`.
6. Takes a Windows screenshot using `Win+PrintScreen`.
7. Clicks near the top-centre of the screen and presses `Enter`.
8. Switches to the next browser tab.
9. Clicks the middle of the screen.
10. Presses `/` to open the Gauth search interface using the Slash to Search extension.
11. Pastes the current clipboard contents.
12. Presses `F11` again.

The exact result depends on the active browser tab, page layout, screen size, browser keyboard behaviour, and extension configuration.

## Configuration

At the top of the script:

- `SOURCE_URL_PREFIX` identifies the Sparx Learning student page.
- `TARGET_URL` is the Gauth website opened if no matching tab is found.
- `TARGET_URL_PREFIX` identifies the Gauth website tab.
- `pyautogui.PAUSE` and the minimum duration/sleep settings control how quickly mouse and keyboard actions run.
- `max_tabs=20` limits how many tabs the script checks when looking for a matching URL.

## Bookwork Checks

For bookwork checks, you may need to locate the screenshots saved by Windows and review them separately.

1. Open your user's Pictures folder and navigate to the `Screenshots` folder.
2. Look for the screenshots containing the relevant questions.
3. Open the screenshots to identify the questions you need to review.
4. If you need to refer to a question again for a bookwork check, upload the relevant screenshot to the Gauth website,.

Note: The script does not automatically organise screenshots by question or verify that a screenshot contains the correct information. Screenshot locations may vary depending on your Windows settings.

## Important Notes

- The script is designed to work with the Gauth website.
- You must install and configure the Slash to Search browser extension for the `/` shortcut to work as expected.
- Make sure the Gauth website is focused before testing the `/` shortcut.
- The script uses screen coordinates, so changing display resolution, browser layout, or zoom may affect where it clicks.
- The script reads the browser's current URL by copying it to the clipboard. This temporarily uses the clipboard.
- `Win+PrintScreen` normally saves a screenshot through Windows. The script does not verify that the screenshot was successfully saved.
- The `F8` shortcut sets a stop flag. The script checks that flag while searching through tabs, but it does not interrupt every action immediately.
- The script assumes the relevant browser tabs are already open or can be opened successfully.
- The script does not check whether the Gauth search interface successfully opened before pasting.
- Browser shortcuts or other extensions may interfere with the `/` key.
- Use extensions only from sources you trust.
- Use automation in accordance with your school's rules and the services' terms.

## Troubleshooting

### It Cannot Find Sparx Learning

- Check that you are signed in.
- Make sure the tab URL begins with the configured `SOURCE_URL_PREFIX`.
- Make sure the browser is focused and the tab is accessible.

### It Opens Another Gauth Tab

- Check whether the existing Gauth tab's URL begins with `https://www.gauthmath.com/`.
- Keep the relevant tabs open before running the script.

### The Search Interface Does Not Open

- Make sure the Slash to Search extension is installed and enabled.
- Check that the extension is configured to open the search interface when `/` is pressed.
- Confirm that the Gauth website is focused.
- Test the shortcut manually before running the automation.
- Check whether another extension or website is intercepting the `/` key.

### The Extension ZIP Will Not Install

- Make sure you extracted the ZIP file first.
- Confirm that the selected folder directly contains `manifest.json`.
- Enable Developer mode on the browser's extensions page.
- Check the extension's README for extra installation requirements.
- If the extension reports an error, inspect the error message shown on the extensions page.

### It Clicks the Wrong Place

- Check your display resolution, browser zoom, and window layout.
- The script relies on fixed screen positions.

### A Keyboard Shortcut Behaves Unexpectedly

- Make sure the browser has focus.
- Check whether another application or extension is intercepting the shortcut.
- Confirm that the browser is on the expected tab before running the script.

## Stopping the Script

Press `F8` to request that the current run stop.

To exit the program entirely, focus the terminal running the script and press `Ctrl+C`.
