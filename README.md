# Cloudflare-Verification-Bypassing

There is plenty of information online about bypassing Cloudflare verification in Python; however, I couldn't find a comprehensive source where everything works seamlessly out-of-the-box. That's why I decided to save the step-by-step solution here.
So here are the steps:

1. Check the Chrome version currently installed.
2. Find the appropriate chromedriver matching your Chrome version:
    https://sites.google.com/chromium.org/driver/downloads
3. Download and unpack it, then(in case of Linux) move the 'chromedriver' file to /usr/local/bin/
   ```
    sudo mv chromedriver /usr/local/bin/
   ```
5. Create a python virtual environment, eg, venv_scraping:
   ```
    python -m venv ~/venv_scraping
   ```
6. Activate it
   ```
    source ~/venv_scraping/bin/activate
   ```
8. Install these python packages:
   - selenium
   - seleniumbase
   - undetected-chromedriver
     
   Additionally PyAutoGUI might be installed. It's useful for simulating keyboard and mouse actions, as well as managing application windows (especially on Linux).
   In order to simplify this installation the file 'requirements.txt' is added, so they can be installed just like this:
   ```
     pip install -r ~/requirements.txt
   ```
    The hardcoded versions in the file rather could/must be unversioned/adjusted according to your setup
9. Bypass successfully the Cloudflare verification by launching a sample python file:
   ```
    python cloud-flare.py
   ```
    the 'domain' url inside the cloud-flare.py file should contain any webpage(from this domain) that contains Cloudflare verification.
    
P.S. Keep in mind that pip/python and pip3/python3 rather refer to different subsets of virtual environments. In other words, always use the same pair consistently.

______________________________

The following environment was successfully used:
   - Chrome 134.0.6998.88
   - Python 3.12
   - Pythons packages:
     - PyAutoGUI==0.9.54
     - selenium==4.29.0
     - seleniumbase==4.35.6
     - undetected-chromedriver==3.5.5

## Demonstration

https://github.com/user-attachments/assets/5f78d6b4-24b9-476e-a537-1fd4bd40eda8






