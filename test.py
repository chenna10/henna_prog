'''
Created on Jun 22, 2017

@author: che
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from compiler.pycodegen import EXCEPT
 


path_to_chromedriver = 'C:\Users\che\Desktop\chromedriver\chromedriver.exe'
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.image": 2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=chromeOptions)
url = 'https://preview.panduit.com/content/panduit/en/home.html'
driver.implicitly_wait(50)
driver.set_window_size(1680, 1050)
driver.set_window_position(0, 0)
driver.get(url)
driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")

    
    
    
    

