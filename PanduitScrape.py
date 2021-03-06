'''
Created on Jun 20, 2017

@author: che
'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


path_to_chromedriver = 'C:\Users\che\Desktop\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
url = 'https://preview.panduit.com/content/panduit/en/home.html'
driver.implicitly_wait(50)
driver.set_window_size(1680, 1050)
driver.set_window_position(0, 0)
driver.get(url)

all_products = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/a')
for i in range(1, 12):
    for j in range(1, 10):
        for k in range(1, 9):
            all_products.click()
            driver.implicitly_wait(50)
            L1_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
            L1_xpath += str(i)
            L1_xpath += ']'
            L1 = driver.find_element_by_xpath(L1_xpath)
            try:
                element_present_L1 = EC.presence_of_element_located((By.XPATH, L1_xpath))
                WebDriverWait(driver, 30).until(element_present_L1)
                L1_to_hover_over = driver.find_element_by_xpath(L1_xpath)
                hover_L1 = ActionChains(driver).move_to_element(L1_to_hover_over).perform()
            except ElementNotVisibleException:
                pass
            try:
                L2_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
                L2_xpath = L2_xpath + str(i)
                L2_xpath += ']/ul/li['
                L2_xpath = L2_xpath + str(j)
                L2_xpath += ']'
                L2_to_hover_over = driver.find_element_by_xpath(L2_xpath)
                hover_L2 = ActionChains(driver).move_to_element(L2_to_hover_over).perform()
            except NoSuchElementException:
                print ""
            try:
                L3_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
                L3_xpath += str(i)
                L3_xpath += ']/ul/li['
                L3_xpath += str(j)
                L3_xpath += ']/ul/li['
                L3_xpath += str(k)
                L3_xpath += ']'
                element_present = EC.presence_of_element_located((By.XPATH, L3_xpath))
                WebDriverWait(driver, 3).until(element_present)
                L3 = driver.find_element_by_xpath(L3_xpath)
                try:
                    L3.click()
                    print driver.title
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath('//*[@id="accordion"]'))
                    filters = driver.find_element_by_xpath('//*[@id="accordion"]')
                    more = filters.find_elements_by_link_text('More')
                    if more:
                        for facet in more:
                            name = facet.find_element_by_tag_name("IMG")
                            name.click()
                            facets = filters.get_property('innerText')
                            print facets
                            print '-----------------------------------------------------'
                    elif not more:
                        filters = driver.find_element_by_xpath('//*[@id="accordion"]')
                        print filters.get_property('innerText')
                except ElementNotVisibleException:
                    print ""
            except TimeoutException:
                print ''
            print "Next L3"
        print "Next L2"
    print "Next L1"