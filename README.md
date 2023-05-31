
1. First, clone this project using the git command.
   `$ git clone https://github.com/ganesanluna/google_dictionary.git`

2. Change the directory to google_dictionary. 
   `$ cd google_dictionary`

3. In this project, everything runs on the Firefox web browser based on Selenium and WebDriver. Now I use the Firefox webdriver.
   Install the Firefox browser and WebDriver. 

4. Run this requirement.txt file using pip.
   `$ pip install -r requirements.txt`

5. Test with a sample selenium code. If you successfully opened Firefox, continue with the below steps. 
   Otherwise find and resolve.

6. Add your vocabulary one by one to dictionary.txt.

7. Finally, run this google_dictionary.py.
   `$ python3 google_dictionary.py`

8. Once that terminal shows "All keywords are searched," that time
   new_dictionary.txt and dictionary.xlsx files are generated.

9. Almost 500 words are created in default_dictionary.txt.
   Just try this one: rename default_dictionary.txt to dictionary.txt.
   
10. If you use chrome browser and chrome webdriver follow this link 
    https://ganesanluna.wordpress.com/2023/01/02/selenium-running-or-testing-with-chrome-in-ubuntu/
    Kindly change main.py file. The search Firefox instead of chrome.
