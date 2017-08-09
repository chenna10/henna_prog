'''
Created on Jun 27, 2017

@author: che
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementNotVisibleException


path_to_chromedriver = 'C:\Users\che\Desktop\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
url = 'https://preview.panduit.com/content/panduit/en/home.html'
driver.implicitly_wait(10)
driver.set_window_size(1680, 1050)
driver.set_window_position(0, 0)
driver.get(url)


L2_page = ["Cable Managers & Accessories", "Cabinets & Accessories", "Enclosures & Accessories", "Thermal Management & Containment", "Racks & Accessories", "Crimpers, Cutters, Strippers & Accessories", "Lugs, Splices, Split Bolts & Accessories", "Terminals & Terminal Kits"]
for i in range(1, 12):
    for j in range(1, 10):
        all_products = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/a')
        all_products.click()
        L1_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
        L1_xpath += str(i)
        L1_xpath += ']'
        L1_to_hover_over = driver.find_element_by_xpath(L1_xpath)
        hover = ActionChains(driver).move_to_element(L1_to_hover_over).perform()
        try:
            L2_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
            L2_xpath += str(i)
            L2_xpath += ']/ul/li['
            L2_xpath += str(j)
            L2_xpath += ']'
            element_present = EC.presence_of_element_located((By.XPATH, L2_xpath))
            WebDriverWait(driver, 3).until(element_present)
            L2 = driver.find_element_by_xpath(L2_xpath)
            try:
                L2.click()
            except ElementNotVisibleException:
                print ""
            print driver.title
            try:
                main_img_1 = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[2]/a/picture/img').click()
                print driver.title
                driver.back()
                follow_loop1 = range(1, 4)
                for k in follow_loop1:
                    xpath = '/html/body/div/div[3]/div[2]/div/div[2]/div/div['
                    xpath += str(k)
                    xpath += ']/a'
                    driver.find_element_by_xpath(xpath).click()
                    print driver.title
                    driver.back()
                main_img_2 = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[3]/a/picture/img').click()
                print driver.title
                driver.back()
                follow_loop2 = range(1, 4)
                for l in follow_loop2:
                    xpath = '/html/body/div/div[3]/div[2]/div/div[3]/div/div['
                    xpath += str(l)
                    xpath += ']/a'
                    driver.find_element_by_xpath(xpath).click()
                    print driver.title
                    driver.back()
            except NoSuchElementException:
                print "No L2 Page goes straight to L3"
            six_img = driver.find_elements_by_class_name('img-with-border')
            print "There are", len(six_img), "images on the", "L2 page."
        except TimeoutException:
            print "Waiting for loop to end"
        print "Next L2!"
    
            
            
    
    
    
       


    

    