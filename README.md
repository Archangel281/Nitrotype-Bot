# NitroType-Bot
This program is able to perform >7000 wpm in a Nitro Type Race.


## Requirements
### Operating System
- Windows (other operating systems might work as well, though the program probably needs to be adapted)

### Browser
- Chromium based browser (<a href="https://www.google.com/intl/en/chrome/">Google Chrome</a> recommended)
- <a href="https://chrome.google.com/webstore/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle?hl=en-GB">SingeFile</a> Chrome Extension

### Python Packages
- beautifulsoup4
- PyAutoGUI
- pynput
- pywin32


## Setting up SingleFile
### Configure Settings
1. In the Chrome browser click on the three dots in the top right corner
2. Click on "Settings"
3. On the left-hand-side click on "Extensions"
4. Click on "Details" of the SingeFile extension
5. Click on "Extension options"
6. Import the <a href="https://github.com/LevinHinder/Nitrotype-Bot/blob/main/singlefile-settings.json">SingleFile settings</a>

### Add Shortcut
1. In the Chrome browser click the three dots in the top right corner
2. Click on "Settings"
3. On the left-hand-side click on "Extensions"
4. Click on the burger menu in the top left corner
5. Click on "Keyboard shortcuts"
6. Add the <code>Ctrl + Shift + B</code> shortcut to "Activate extension" of the SingleFile extension


## Run the Script
1. Install <a href="https://www.python.org/downloads/">Python</a>
2. Install all necessary packages. If you don't know how, follow this <a href="https://packaging.python.org/en/latest/tutorials/installing-packages/">this Tutorial</a>.
3. Inside the <code>main.py</code> script configure following settings:<br>
    a. <code>WPM</code>: the speed in words per minute [0-∞]<br>
    b. <code>ACCURACY</code>: the accuracy of the typing [0-1]. 0 meaning 0% and 1 meaning 100%<br>
    c. <code>NUMBER_OF_RACES</code>: the number of races before the program stops [1-∞]
4. Log into your <a href="https://www.nitrotype.com/">Nitro Type Account</a> or create a new one
5. Put your browser with the Nitro Type window on one side of the screen and the terminal on the other side
6. Click on "Race Now"
7. Run the script
8. You have now 2 seconds time to click inside the Nitro Type window
9. Watch how the magic unfolds


## Attention
Setting the typing speed above ~215 wpm will get you banned! The world record is 256 wpm
