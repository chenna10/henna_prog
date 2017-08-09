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
from selenium.webdriver.support.ui import Select



path_to_chromedriver = 'C:\Users\che\Desktop\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
url = 'https://preview.panduit.com/content/panduit/en/home.html'
driver.set_window_size(1680, 1050)
driver.set_window_position(0, 0)
driver.get(url)
(driver.page_source).encode('utf-8')

i = 4
j = 3
k = 1



while i != 13 and j != 13 and k != 13:
    try:
        all_products = driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/a')
        all_products.click()
        driver.implicitly_wait(60)
        L1_xpath = '//*[@id="bs-example-navbar-collapse-1"]/div/ul[1]/li[1]/ul/li['
        L1_xpath += str(i)
        L1_xpath += ']'
        element_present_L1 = EC.presence_of_element_located((By.XPATH, L1_xpath))
        WebDriverWait(driver, 60).until(element_present_L1)
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
        WebDriverWait(driver, 60).until(element_present)
        L3 = driver.find_element_by_xpath(L3_xpath)
        try:
            L3.click()
            print driver.current_url
            try:
                WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[1]/div/h2"))
                L3_h2 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[1]/div/h2")
                L3_title = L3_h2.get_property("innerText")
                print L3_title
                L3_string = L3_title.replace(" ", "%20")
                L3_string = L3_title.replace("&", "%26").replace(" ", "%20").replace("/", "~2F")
                new_L3_string = L3_string
            except TimeoutException:
                break
            next_page = 2
            m = 1
            while m != 31:
                title_xpath = '/html/body/div/div[2]/div/div[2]/div[4]/div[2]/div['
                title_xpath += str(m)
                title_xpath += ']/div[2]/label'
                image_xpath = '/html/body/div/div[2]/div/div[2]/div[4]/div[2]/div['
                image_xpath += str(m)
                image_xpath += ']/div[1]/a/img'
                driver.implicitly_wait(60)
                try:
                    WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath(title_xpath))
                    driver.implicitly_wait(60)
                    images = driver.find_elements_by_xpath(title_xpath)
                    driver.implicitly_wait(60)
                    for image in images:
                        driver.implicitly_wait(60)
                        print image.get_property('innerText'),
                        driver.implicitly_wait(60)
                        print ",",
                        driver.implicitly_wait(60)
                        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, image_xpath)))
                        driver.implicitly_wait(60)
                        img = driver.find_element_by_xpath(image_xpath)
                        driver.implicitly_wait(60)
                        print img.get_attribute('outerHTML'),
                        print ",",
                        driver.implicitly_wait(60)
                        print img.get_attribute('src')
                        driver.implicitly_wait(60)
                except TimeoutException:
                    break  
                if m == 30:   
                    try:
                        pageNo = driver.find_element_by_link_text(str(next_page))
                            driver.execute_script('arguments[0].click();', pageNo)
                            next_page+=1
                            driver.implicitly_wait(30)  
                    except NoSuchElementException:
                        break
                    m = 1
                else:
                    m += 1  
        except ElementNotVisibleException:
            k = 0
        k += 1
    except TimeoutException:
        j += 1
        k = 1