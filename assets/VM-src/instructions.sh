mkdir project 
cd project 
sudo apt update 
sudo apt install -y python3-pip python3 virtualenv neofetch htop

virtualenv - p python3 venv
source venv/bin/activate

pip install playwright requests
sudo /home/sargunsingh20062017/project/venv/bin/playwright install-deps 
sudo /home/sargunsingh20062017/project/venv/bin/pip install playwright
playwright install

echo '''import requests
import random
import time
from playwright.sync_api import sync_playwright

def check_url(page, url): 
    page.goto(url)
    page.wait_for_load_state('networkidle') 
    html_content = page.content()
    line_count = html_content.count('\n')
    if line_count <= 2:  
        return False
    else: 
        return True 


with sync_playwright() as p:
    browser = p.chromium.launch()  
    page = browser.new_page()     
    tab_count = 1                 

    while 1: 
        test_url =  "https://se.printo.in/g/" + ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(12))
        if check_url(page,test_url):
            print(f"Potential valid URL found: {test_url}")
        tab_count += 1 
        if tab_count < 25:
            page = browser.new_page() 
        else: 
            browser.close()      
            browser = p.chromium.launch() 
            page = browser.new_page()
            tab_count = 1    


''' > test.py