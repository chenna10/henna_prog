'''
Created on Jun 30, 2017

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
driver.set_window_size(1680, 1050)
driver.set_window_position(0, 0)
driver.get(url)


all_products = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/a')
for i in range(1, 12):
    all_products.click()
    driver.implicitly_wait(50)
    L1_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
    L1_xpath += str(i)
    L1_xpath += ']'
    L1 = driver.find_element_by_xpath(L1_xpath)
    try:
        element_present_L1 = EC.presence_of_element_located((By.XPATH, L1_xpath))
        WebDriverWait(driver, 30).until(element_present_L1)
        L1 = driver.find_element_by_xpath(L1_xpath).click()
        print driver.title
    except ElementNotVisibleException:
        pass
    try:
        L1_main_img_xpath = '/html/body/div/div[3]/div[2]/div/div[2]/a/picture/img'
        element_present_img = EC.presence_of_element_located((By.XPATH, L1_main_img_xpath))
        WebDriverWait(driver, 30).until(element_present_img)
        L1_main_img_1 = driver.find_element_by_xpath(L1_main_img_xpath).click()
        print driver.title
        driver.back()
        follow_loop1 = range(1, 4)
        for k in follow_loop1:
            L1_img_xpath1 = '/html/body/div/div[3]/div[2]/div/div[2]/div/div['
            L1_img_xpath1 += str(k)
            L1_img_xpath1 += ']/a'
            driver.find_element_by_xpath(L1_img_xpath1).click()
            print driver.title
            driver.back()
        L1_main_img_2 = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[3]/a/picture/img').click()
        print driver.title
        driver.back()
        follow_loop2 = range(1, 4)
        for l in follow_loop2:
            L1_img_xpath2 = '/html/body/div/div[3]/div[2]/div/div[3]/div/div['
            L1_img_xpath2 += str(l)
            L1_img_xpath2 += ']/a'
            driver.find_element_by_xpath(L1_img_xpath2).click()
            print driver.title
            driver.back()
    except NoSuchElementException:
        pass
    six_img = driver.find_elements_by_class_name('img-with-border')
    print "There are", len(six_img), "images on the", "L1 page."
    for j in range(1, 11):
        driver.implicitly_wait(50)
        try:
            driver.implicitly_wait(50)
            L2_xpath = '//*[@id="accordion"]/li['
            L2_xpath += str(j)
            L2_xpath += ']/h4/a'
            element_present = EC.presence_of_element_located((By.XPATH, L2_xpath))
            WebDriverWait(driver, 10).until(element_present)
            try:
                L2 = driver.find_element_by_xpath(L2_xpath).click()
            except ElementNotVisibleException:
                pass
            driver.implicitly_wait(50)
            print driver.current_url
            print driver.title
            L2_main_img_xpath = '/html/body/div/div[3]/div[2]/div/div[2]/a'
            element_present_img = EC.presence_of_element_located((By.XPATH, L2_main_img_xpath))
            WebDriverWait(driver, 30).until(element_present_img)
            try:
                driver.implicitly_wait(50)
                L2_main_img1 = driver.find_element_by_xpath(L2_main_img_xpath)
                driver.implicitly_wait(50)
                L2_main_img1.click()
                print driver.title
                driver.back()
                follow_loop1 = range(1, 4)
                for k in follow_loop1:
                    L2_img_xpath1 = '/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div['
                    L2_img_xpath1 += str(k)
                    L2_img_xpath1 += ']/a/picture/img'
                    driver.find_element_by_xpath(L2_img_xpath1).click()
                    print driver.title
                    driver.back()
                L2_main_img_2 = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[3]/a').click()
                print driver.title
                driver.back()
                follow_loop2 = range(1, 4)
                for l in follow_loop2:
                    L2_img_xpath2 = '/html/body/div[1]/div[3]/div[2]/div/div[3]/div/div['
                    L2_img_xpath2 += str(l)
                    L2_img_xpath2 += ']/a/picture/img'
                    driver.find_element_by_xpath(L2_img_xpath2).click()
                    print driver.title
                    driver.back()
            except NoSuchElementException:
                pass
            six_img = driver.find_elements_by_class_name('img-with-border')
            print "There are", len(six_img), "images on the", "L2 page."
            driver.back()
        except TimeoutException:
            pass
        for k in range(1, 9):
            driver.implicitly_wait(50)
            try:
                L3_xpath = '/html/body/div/div[3]/div[1]/div/ul/li['
                L3_xpath += str(k)
                L3_xpath += ']/h4/a'
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
    print "Waiting for new L1"
        
        