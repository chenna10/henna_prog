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

while i != 13 and j != 13 and k != 12:
    all_products = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/a')
    all_products.click()
    driver.implicitly_wait(10)
    L1_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
    L1_xpath += str(i)
    L1_xpath += ']'
    try:
        element_present_L1 = EC.presence_of_element_located((By.XPATH, L1_xpath))
        WebDriverWait(driver, 3).until(element_present_L1)
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
        WebDriverWait(driver, 3).until(element_present)
        L3 = driver.find_element_by_xpath(L3_xpath)
        try:
            L3.click()
            L3_BreadCrumb = driver.find_element_by_xpath('/html/body/div/div[1]/div/p')
            print L3_BreadCrumb.get_property('innerText')
            try:
                WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath('//*[@id="accordion"]/li[13]/div/h4/a/span'))
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
                    WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_xpath(facet_xpath))
                    facets = driver.find_element_by_xpath(facet_xpath)
                    print facets.get_property('innerText').encode('utf-8')
            except TimeoutException:
                print "Next L3"
        except ElementNotVisibleException:
            k = 0
        k += 1
    except TimeoutException:
        print "Next L2"
        j += 1
        k = 1