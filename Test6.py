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
(driver.page_source).encode('utf-8')

i = 1
j = 1
k = 1

while i != 13 and j != 13 and k != 13:
    all_products = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/a')
    all_products.click()
    driver.implicitly_wait(10)
    L1_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
    L1_xpath += str(i)
    L1_xpath += ']'
    try:
        element_present_L1 = EC.presence_of_element_located((By.XPATH, L1_xpath))
        WebDriverWait(driver, 30).until(element_present_L1)
        L1_to_hover_over = driver.find_element_by_xpath(L1_xpath)
        hover_L1 = ActionChains(driver).move_to_element(L1_to_hover_over).perform()
    except ElementNotVisibleException:
        pass
    L2_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
    L2_xpath = L2_xpath + str(i)
    L2_xpath += ']/ul/li['
    L2_xpath = L2_xpath + str(j)
    L2_xpath += ']'
    try:
        L2_to_hover_over = driver.find_element_by_xpath(L2_xpath)
        hover_L2 = ActionChains(driver).move_to_element(L2_to_hover_over).perform()
    except NoSuchElementException:
        print "Next L1"
        i += 1
        j = 1
        k = 1
    L3_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
    L3_xpath += str(i)
    L3_xpath += ']/ul/li['
    L3_xpath += str(j)
    L3_xpath += ']/ul/li['
    L3_xpath += str(k)
    L3_xpath += ']'
    try:
        element_present = EC.presence_of_element_located((By.XPATH, L3_xpath))
        WebDriverWait(driver, 30).until(element_present)
        L3 = driver.find_element_by_xpath(L3_xpath)
        try:
            L3.click()
            L3_BreadCrumb = driver.find_element_by_xpath('/html/body/div/div[1]/div/p')
            print L3_BreadCrumb.get_property('innerText')
            L3_title = driver.title
            print L3_title
            L3_string = L3_title.replace(" ", "%"+"20")
            L3_string = L3_title.replace("&", "%"+"26")
            L3_string = L3_title.replace("Panduit | ", "")
            try:
                WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath('//*[@id="accordion"]/li[13]/div/h4/a/span'))
                show_all_xpath = driver.find_elements_by_xpath('//*[@id="accordion"]/li[13]/div/h4/a/span')
                show_all = driver.find_element_by_link_text('Show All')
                show_all.click()
            except TimeoutException:
                print "No Show All"
            
            try:
                l = 1
                for l in range (1, 30):
                    facet_xpath = '//*[@id="accordion"]/li['
                    facet_xpath += str(l) 
                    facet_xpath += ']/h4/a/span'
                    WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(facet_xpath))
                    facets = driver.find_element_by_xpath(facet_xpath)
                    print facets.get_property('innerText').encode('utf-8')
            except TimeoutException:
                pass
            print "Starting To Check Images"
            m = 1
            next_page = 1 
            while m != 31:
                no_image_xpath = '/html/body/div/div[2]/div/div[2]/div[4]/div[2]/div['
                no_image_xpath += str(m)
                no_image_xpath += ']/div[1]/a/img'
                try:
                    WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(no_image_xpath))
                    no_image = driver.find_element_by_xpath(no_image_xpath)
                    WebDriverWait(driver, 30)
                    image_not_aval = no_image.get_property('outerHTML')
                    image_not_aval_check = "/is/image/content/dam/panduit/en/general/image-not-available.png?$search-thumb$"
                    if image_not_aval_check in image_not_aval:
                        print image_not_aval
                        no_image.click()
                        print driver.title
                        print driver.current_url
                        driver.back()
                    elif image_not_aval_check not in image_not_aval:
                        print ""
                except TimeoutException:
                    break
                if m == 30:   
                    try:
                        current_url = driver.current_url
                        next_page += 1
                        new_url = current_url+"?i=1;page%3D"+str(next_page)+";pt%3Dproducts;q%3D*;q1%3D"+L3_string+";sp_cs%3DUTF-8;x1%3Dl3-title"
                        driver.get(new_url) 
                        print new_url
                    except NoSuchElementException:
                        pass
                    print "Next Page"
                    m = 1
                else:
                    m += 1
        except ElementNotVisibleException:
            k = 0
        k += 1
    except TimeoutException:
        print "Next L2"
        j += 1
        k = 1