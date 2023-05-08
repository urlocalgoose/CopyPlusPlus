# Copy++

Copy++ is a simple application for Windows that adds the feature of additive copying to your clipboard. With Copy++, you can copy multiple pieces of text and combine them into a single clipboard entry with a customizable separator.

## Features
- Adds the feature of additive copying to Windows
- Customizable separator to separate clipboard entries
- Hotkey support for copying and clearing clipboard

## Installation
1. Ensure you have Python 3.x installed on your Windows machine
2. Install the required libraries by running the following command in the command prompt:
   ```
   pip install pynput pywin32
   ```
3. Download or clone the source code for Copy++
4. Run the application by navigating to the source code directory in the command prompt and executing the following command:
   ```
   python copy++.py
   ```

## Usage
- To copy a piece of text to the clipboard, select the text and press the hotkey for copy command, which is `<ctrl>+c` by default.
- To clear the clipboard, press the hotkey for clear command, which is `<ctrl>+m` by default.
- All copied text will be combined into a single clipboard entry with the separator specified in the code.

## Configuration
You can customize the behavior of Copy++ by modifying the following variables in the code:
- `order`: Determines whether new text is added to the front (1) or back (0) of the clipboard entry.
- `copy_command`: Hotkey for copying text to clipboard.
- `clear_command`: Hotkey for clearing the clipboard.
- `separator`: Customizable separator for separating clipboard entries. 

## Limitations
- Copy++ only supports plain text and cannot copy formatted text or images. 
- Copy++ only supports keyboard hotkeys and does not have a graphical user interface. 

## Credits
Copy++ was created by Joseph Cody and uses the following libraries:
- [pynput](https://pypi.org/project/pynput/)
- [pywin32](https://pypi.org/project/pywin32/)
