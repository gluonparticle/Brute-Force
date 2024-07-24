import requests
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
    i=0
    while 1: 
        test_url =  "https://se.printo.in/g/" + ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(12))

        if check_url(page,test_url):
            print(f"Potential valid URL found: {test_url}")
        tab_count += 1 
        i+=1
        print(f"Counter: {i}")
        if tab_count < 20:
            page = browser.new_page() 
        else: 
            browser.close()      
            browser = p.chromium.launch() 
            page = browser.new_page()
            tab_count = 1    