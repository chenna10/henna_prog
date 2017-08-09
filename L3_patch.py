'''
Created on Jun 26, 2017

@author: che
'''
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


path_to_chromedriver = 'C:\Users\che\Desktop\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
url = 'https://preview.panduit.com/content/panduit/en/products/copper-systems/patch-panels-accessories.html'
driver.implicitly_wait(50)
driver.set_window_size(1680, 1050)
driver.set_window_position(0, 0)
driver.get(url)

pop_patch = driver.find_element_by_link_text('Populated Patch Panels').click()
url = driver.current_url
print url

print'---------------------------------------------------------------------------------------------'
driver.get(url)
# Facets for the first L3 in Cabinets, Thermal Management, Racks & Enclosures
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
else:
    filters = driver.find_element_by_xpath('//*[@id="accordion"]')
    print filters.get_property('innerText')

url = driver.back()
 
patch_pan = driver.find_element_by_link_text('Patch Panel Labels').click()
url = driver.current_url
print url

print'---------------------------------------------------------------------------------------------'
driver.get(url)
# Facets for the first L3 in Cabinets, Thermal Management, Racks & Enclosures
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
else:
    filters = driver.find_element_by_xpath('//*[@id="accordion"]')
    print filters.get_property('innerText')

url = driver.back()

patch_pan_acc = driver.find_element_by_link_text('Patch Panel Accessories').click()
url = driver.current_url
print url

print'---------------------------------------------------------------------------------------------'
driver.get(url)
# Facets for the first L3 in Cabinets, Thermal Management, Racks & Enclosures
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
else:
    filters = driver.find_element_by_xpath('//*[@id="accordion"]')
    print filters.get_property('innerText')

url = driver.back()

mod_patch_pan = driver.find_element_by_link_text('Modular Patch Panels').click()
url = driver.current_url
print url

print'---------------------------------------------------------------------------------------------'
driver.get(url)
# Facets for the first L3 in Cabinets, Thermal Management, Racks & Enclosures
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
else:
    filters = driver.find_element_by_xpath('//*[@id="accordion"]')
    print filters.get_property('innerText')
