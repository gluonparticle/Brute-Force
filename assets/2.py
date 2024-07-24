import requests
import random
import time
from playwright.sync_api import sync_playwright
import threading 

def check_url(page, url): 

    page.set_extra_http_headers({"Cache-Control": "no-store"})
    page.goto(url)
    page.wait_for_load_state('networkidle') 
    # Inside your `check_url()` function
    page.wait_for_load_state('networkidle', timeout=5000)  
    html_content = page.content()
    line_count = html_content.count('\n')
    if line_count <= 2:  
        return False
    else: 
        return True 

def run_playwright():
  """Executes the Playwright operations within a separate thread."""
  with sync_playwright() as p:
      browser = p.chromium.launch()  
      page = browser.new_page()     
      tab_count = 1                 

      while 1: 
          test_url =  "https://se.printo.in/g/" + ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(12))
          test_url = "https://se.printo.in/g/6KsCsuAS34Ft"
          if check_url(page,test_url):
              print(f"Potential valid URL found: {test_url}")
          print(test_url)
          tab_count += 1 
          if tab_count < 25:
              page = browser.new_page() 
          else: 
              browser.close()      
              browser = p.chromium.launch() 
              page = browser.new_page()
              tab_count = 1    

# Start the Playwright operations in a new thread  
playwright_thread = threading.Thread(target=run_playwright)
playwright_thread.start()

input("Playwright running in separate thread. Press Enter to stop...")