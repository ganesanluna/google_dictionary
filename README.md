
1. First, clone this project using the git command.
   `$ git clone https://github.com/ganesanluna/google_dictionary.git`

2. Change the directory to google_dictionary. 
   `$ cd google_dictionary`

3. In this project, everything runs on the Firefox web browser based on Selenium and WebDriver. Now I use the Firefox webdriver.
   Install the Firefox browser and WebDriver. Download and install them using the below steps:
      - Go to https://github.com/mozilla/geckodriver/releases and download your compatible Firefox webdriver.
      - `$ tar -C /usr/local/bin/ -xvzf geckodriver-v0.33.0-linux64.tar.gz`

4. Run this requirement.txt file using pip.
   `$ pip install -r requirements.txt`

5. Add your vocabulary one by one to dictionary.txt.

6. Finally, run this google_dictionary.py.
   `$ python3 google_dictionary.py`

7. Once that terminal shows "All keywords are searched," that time
   new_dictionary.txt and dictionary.xlsx files are generated.

8. Almost 500 words are created in default_dictionary.txt.
   Just try this one: rename default_dictionary.txt to dictionary.txt.
