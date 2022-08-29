from pynput.keyboard import Controller
from bs4 import BeautifulSoup
import time
import random
import win32clipboard
import pyautogui

WPM = 200
ACCURACY = 0.95
NUMBER_OF_RACES = 1


keyboard = Controller()


def main():
    race_number = 0

    while NUMBER_OF_RACES > race_number:
        time.sleep(2)
        game_has_started = False
        letters = []

        race_number += 1
        print(f"race number {race_number}")

        while not game_has_started:
            pyautogui.mouseDown()
            pyautogui.hotkey('shift', 'alt', 'b')
            pyautogui.mouseUp()

            try:
                win32clipboard.OpenClipboard()
                html = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                soup = BeautifulSoup(html, features="html.parser")
                letters = soup.findAll(class_="dash-letter")

                if letters:
                    game_has_started = "is-correct" in str(letters[0])
                    if not game_has_started:
                        key = letters[0].text
                        keyboard.press(key)
                        keyboard.release(key)
            except:
                pass

        number_of_words = len(
            [letter.text for letter in letters if " " in letter.text]) + 1
        total_time = number_of_words / WPM * 60

        delay = total_time / len(letters) * 10_000
        delay /= (5*(10**(-6)) * (WPM ** 2) - 0.0006 * WPM + 0.9947)
        min_delay = round(delay * 0.7)
        max_delay = round(delay * 1.3)

        letters.pop(0)
        letters.pop(-1)

        for letter in letters:
            correct = random.random()
            if correct >= ACCURACY:
                keyboard.press("$")
                keyboard.release("$")

            wait = random.randint(min_delay, max_delay) / 10_000
            time.sleep(wait)

            key = letter.text
            if key == " ":
                key = " "

            keyboard.press(key)
            keyboard.release(key)

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()

        time.sleep(3)
        pyautogui.press('enter')


if __name__ == '__main__':
    main()
