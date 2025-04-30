🇺🇸 US Visa Appointment Bot
Supports: UAE, Armenia, Turkey, Canada

🧠 What Does This Program Do?
This program automates the process of checking and scheduling US visa appointment availability for selected embassies in:

United Arab Emirates (UAE)

Armenia

Turkey

Canada

It saves users the hassle of manually checking for open appointment slots by continuously monitoring the visa website and alerting the user when availability is detected.

recent updates:
after executing the file make an imputs as 0 for applicants if the checkboxes are already selected on the web page.
Select applicant 1? (yes = 1, no = 0): 0
Select applicant 2? (yes = 1, no = 0): 0
Select applicant 3? (yes = 1, no = 0): 0

🖥️ System Requirements
Supported Browser: Google Chrome

Operating Systems: Windows (Recommended), macOS (with adjustments)

ChromeDriver Required:
Download the matching version for your Chrome browser here:
👉 https://chromedriver.chromium.org/downloads

Once downloaded:

Extract the chromedriver.exe file.

Place it in the same folder as the visa_bot.exe file.

🚀 How to Use
navigate to "dist" folder->"visa_bot" folder-> run visa_bot.exe 
sometimes visa_bot.exe and chromedriver.exe must be in the same folder(just put a chromedriver there if missing).

Double-click on visa_bot.exe.

Follow the prompts on screen to select your country, city, and login credentials.

⚠️ Privacy Notice:
Your email and password are stored only in memory during runtime and are automatically discarded once the program is closed.

🛠️ Want to Modify the Source Code?
Make sure you have Python installed (preferably Python 3.10–3.13), then install the required libraries:

pip install selenium
pip install pyautogui
pip install pyinstaller

To run the script as a .py file:

python visa_bot.py
🏗️ Generate an Executable (.exe) from the Script
Navigate to the folder containing visa_bot.py.

Right-click in the folder background → "Open in Terminal".

In the terminal, run:

pyinstaller --onefile visa_bot.py
This creates a dist folder containing visa_bot.exe.

⚙️ Optional: Modify the .spec File
If you want to customize the PyInstaller build (e.g., hide the console window), modify the generated visa_bot.spec file.

After editing, recompile using:

pyinstaller visa_bot.spec

Go to the "dist" folder.
run visa_bot.exe and follow the prompts on the screen

inspiration for the build: https://github.com/mahdiaredraki/Automated-US-Visa-Appointment-Finder.git
