# Sparth-A-utiltity-to-take-your-sparx-screenshots-to-gauth-

A Python automation script that switches between Sparx Learning and the Gauth website, captures a screenshot, and performs a sequence of keyboard and mouse actions.

## Requirements

- Windows
- Python 3
- A browser with Sparx Learning and the Gauth website available
- The Gauth website, with `/` configured to open its search interface
- The Python packages `pyautogui`, `pyperclip`, and `keyboard`

## Installation

Install the required Python packages:

```bash
py -m pip install pyautogui pyperclip keyboard
```

Save the original script as `sparx_helper.py` or another `.py` filename.

## Setup

1. Open your browser and sign in to Sparx Learning.
2. Make sure a browser tab has a URL beginning with `https://maths.sparx-learning.com/student/`.
3. Keep the Sparx Learning and Gauth website tabs open, if possible.
4. Run the script:

   ```bash
   py sparx_helper.py
   ```

5. A new blank window opens, and the script prints:

   ```text
   Ready. CTRL+SHIFT+U to run, F8 to stop.
   ```

6. Press `Ctrl+Shift+U` to start the automation.

## Keyboard shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+Shift+U` | Starts the automation sequence. |
| `F8` | Requests that the current sequence stop. |
| `/` | Opens the search interface on the Gauth website when the correct page is focused. |
| PyAutoGUI failsafe | Move the mouse to the top-left corner of the screen to trigger PyAutoGUI's failsafe. |

## What the script does

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
10. Presses `/` to open the search interface on the Gauth website.
11. Pastes the current clipboard contents.
12. Presses `F11` again.

The exact result depends on the active browser tab, page layout, screen size, and browser keyboard behaviour.

## Configuration

At the top of the script:

- `SOURCE_URL_PREFIX` identifies the Sparx Learning student page.
- `TARGET_URL` is the Gauth website opened if no matching tab is found.
- `TARGET_URL_PREFIX` identifies the Gauth website tab.
- `pyautogui.PAUSE` and the minimum duration/sleep settings control how quickly mouse and keyboard actions run.
- `max_tabs=20` limits how many tabs the script checks when looking for a matching URL.

## Important notes

- The script is designed to work with the Gauth website.
- Make sure `/` opens the search interface on the Gauth website.
- The script uses screen coordinates, so changing display resolution, browser layout, or zoom may affect where it clicks.
- The script reads the browser's current URL by copying it to the clipboard. This temporarily uses the clipboard.
- `Win+PrintScreen` normally saves a screenshot through Windows. The script does not verify that the screenshot was successfully saved.
- The `F8` shortcut sets a stop flag. The script checks that flag while searching through tabs, but it does not interrupt every action immediately.
- The script assumes the relevant browser tabs are already open or can be opened successfully.
- The script does not check whether the Gauth search interface successfully opened before pasting.
- Use automation in accordance with your school's rules and the services' terms.

## Troubleshooting

### It cannot find Sparx Learning

- Check that you are signed in.
- Make sure the tab URL begins with the configured `SOURCE_URL_PREFIX`.
- Make sure the browser is focused and the tab is accessible.

### It opens another Gauth tab

- Check whether the existing Gauth tab's URL begins with `https://www.gauthmath.com/`.
- Keep the relevant tabs open before running the script.

### The search interface does not open

- Confirm that `/` opens the search interface on the Gauth website.
- Make sure the browser has focus and the script clicks in the correct location.

### It clicks the wrong place

- Check your display resolution, browser zoom, and window layout.
- The script relies on fixed screen positions.

### A keyboard shortcut behaves unexpectedly

- Make sure the browser has focus.
- Check whether another application is intercepting the shortcut.
- Confirm that the browser is on the expected tab before running the script.

## Stopping the script

Press `F8` to request that the current run stop. To exit the program entirely, focus the terminal running the script and press `Ctrl+C`.
