# Web Search Automation (Python)

This Python script automates searching up to 30 words in a browser using a **single tab**, with a 5-second delay between each search.

## 📌 Features

- Accepts up to 30 words from the user
- Uses a single browser tab (no tab switching)
- Waits 5 seconds between each search
- You manually position the cursor in the search bar before the script runs
- Lightweight and easy to run using Python and `pyautogui`

## 🚀 How It Works

1. Run the script
2. Enter up to 30 words when prompted
3. A 5-second countdown will begin
4. You place the **mouse cursor in the search bar** of any browser
5. The script will type each word, press Enter, wait 5 seconds, then move on to the next word

## 🖥 Requirements

- Python 3.x
- A web browser (Chrome, Firefox, Edge, Brave, etc.)
- `pyautogui` library

## 🔧 Setup Instructions

1. Install the required library:

   ```bash
   pip install pyautogui

   
2. bash
 git clone https://github.com/yourusername/web-search-automation.git
cd web-search-automation

3.python edge_search_final.py


📁 Example Input
text
Copy
Edit
lantern
whisper
prism
echo
t noodle
misty
❗ Notes
This script relies on mouse/keyboard automation. Avoid moving the mouse or typing while it runs.

You must manually place the cursor in the browser’s search bar before the script begins.

Works only on desktop/laptop devices (not supported on mobile).

🛡 License
This project is open-source and free to use under the MIT License.

🤝 Contributions
Pull requests and suggestions are welcome!


