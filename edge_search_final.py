import pyautogui
import time

def get_input():
    user_input = input("Enter up to 30 words (separated by space): ").strip()
    words = user_input.split()
    if len(words) > 30:
        print("Limit exceeded! Only the first 30 words will be used.")
        words = words[:30]
    return words

def search_in_same_tab(words):
    print("Place your mouse cursor inside the search box of Microsoft Edge tab and leave it there.")
    input("Press Enter once ready...")

    for word in words:
        # Click at current mouse location (search bar)
        pyautogui.click()
        time.sleep(0.3)

        # Clear previous input
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        time.sleep(0.3)

        # Type and search the word
        pyautogui.write(word, interval=0.05)
        pyautogui.press("enter")
        print(f"Searched: {word}")
        time.sleep(5)

if __name__ == "__main__":
    word_list = get_input()
    search_in_same_tab(word_list)
