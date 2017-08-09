'''
Created on Jul 10, 2017

@author: CHE
'''
'''
Created on Jul 10, 2017

@author: CHE
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementNotVisibleException


path_to_chromedriver = 'C:\Users\che\Desktop\chromedriver\chromedriver.exe'
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.image": 2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=chromeOptions)
url = 'https://preview.panduit.com/content/panduit/en/home.html'
driver.implicitly_wait(20)
driver.set_window_size(1680, 1050)
driver.set_window_position(0, 0)
driver.get(url)
driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")
(driver.page_source).encode('utf-8')

i = 1
j = 1
k = 1

while i != 13 and j != 13 and k != 13:
    try:
        all_products = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/a')
        driver.implicitly_wait(20)
        L1_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
        L1_xpath += str(i)
        L1_xpath += ']'
        element_present_L1 = EC.presence_of_element_located((By.XPATH, L1_xpath))
        WebDriverWait(driver, 20).until(element_present_L1)
        L1_to_hover_over = driver.find_element_by_xpath(L1_xpath)
    except ElementNotVisibleException:
        pass
    try:
        L2_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
        L2_xpath = L2_xpath + str(i)
        L2_xpath += ']/ul/li['
        L2_xpath = L2_xpath + str(j)
        L2_xpath += ']'
        L2_to_hover_over = driver.find_element_by_xpath(L2_xpath)
    except NoSuchElementException:
        i += 1
        j = 1
        k = 1
        url  = "https://preview.panduit.com/content/panduit/en/home.html"
        driver.get(url)
        driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")
    L3_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
    L3_xpath += str(i)
    L3_xpath += ']/ul/li['
    L3_xpath += str(j)
    L3_xpath += ']/ul/li['
    L3_xpath += str(k)
    L3_xpath += ']/a'
    try:
        element_present = EC.presence_of_element_located((By.XPATH, L3_xpath))
        WebDriverWait(driver, 20).until(element_present)
        L3 = driver.find_element_by_xpath(L3_xpath)
        try:
            driver.execute_script('arguments[0].click();', L3)
            print driver.title
            driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")
            try:
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[1]/div/h2"))
                L3_h2 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[1]/div/h2")
                L3_title = L3_h2.get_property("innerText")
                L3_string = L3_title.replace(" ", "%20")
                L3_string = L3_title.replace("&", "%26").replace(" ", "%20").replace("/", "~2F")
                new_L3_string = L3_string
            except TimeoutException:
                break
            m = 1
            next_page = 1
            thumbImageCount = 0
            imageCount = 0
            while m != 31:
                element = '/html/body/div/div[2]/div/div[2]/div[4]/div[2]/div['
                element += str(m)
                element += ']/div[1]/a/img'
                try:
                    elementImg = driver.find_element_by_xpath(element)
                    elementOut = elementImg.get_attribute('src')
                    el = str(elementOut)
                    if 'https://preview.panduit.com/is/image/content/dam/panduit/en/general/image-not-available.png?$search-thumb$' in el:
                        thumbImageCount+=1
                    driver.execute_script("arguments[0].click();", elementImg)
                    driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")
                    try:
                        img_xpath = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[2]/ul/li')
                    except NoSuchElementException:
                        imageCount+=1
                    driver.back()
                    driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")
                    if m == 30:   
                        try:
                            current_url = driver.current_url
                            next_page += 1
                            url_path = "?do=panduit_l3;i%3D1;page%3D"+str(next_page)+";pt%3Dproducts;q%3D*;q1%3D"+new_L3_string+";sp_cs%3DUTF-8;x1%3Dl3-title"
                            if "?do=" not in current_url:
                                new_url = current_url+url_path
                            else:
                                prev_page = next_page - 1
                                new_url = current_url.replace("?do=panduit_l3;i%3D1;page%3D"+str(prev_page)+";pt%3Dproducts;q%3D*;q1%3D"+new_L3_string+";sp_cs%3DUTF-8;x1%3Dl3-title", "?do=panduit_l3;i%3D1;page%3D"+str(next_page)+";pt%3Dproducts;q%3D*;q1%3D"+new_L3_string+";sp_cs%3DUTF-8;x1%3Dl3-title") 
                            driver.implicitly_wait(20)
                            driver.get(new_url) 
                            driver.implicitly_wait(20)
                        except NoSuchElementException:
                            break
                        m = 1
                    else:
                        m += 1  
                except NoSuchElementException:
                    print "Number of Missing Thumb Images: ",thumbImageCount
                    print "Number of Missing Images: ",imageCount
                    break
            thumbImageCount = 0
            imagCount = 0
        except ElementNotVisibleException:
            k = 0
            url  = "https://preview.panduit.com/content/panduit/en/home.html"
            driver.get(url)
            driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")
        k += 1
        url  = "https://preview.panduit.com/content/panduit/en/home.html"
        driver.get(url)
        driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")
    except TimeoutException:
        j += 1
        k = 1
        url  = "https://preview.panduit.com/content/panduit/en/home.html"
        driver.get(url)
        driver.execute_script("var queries = ['link[rel=stylesheet][href]', 'style'];for (var i = 0; i < queries.length; i++) {var remove = document.querySelectorAll(queries[i]);for (var j = 0; j < remove.length; j++) {remove[j].outerHTML = '';}}var inline = document.querySelectorAll('*[style]');for (var i = 0; i < inline.length; i++) {inline[i].removeAttribute('style');}")
