from selenium import webdriver
import time

driverLocation = '/usr/bin/chromedriver'

driver  = webdriver.Chrome(driverLocation)

def fb_login():
    driver.get("https://www.imdb.com")
    time.sleep(10)
    driver.find_element_by_class_name("ipc-button ipc-button--single-padding ipc-button--default-height ipc-button--core-baseAlt ipc-button--theme-baseAlt ipc-button--on-textPrimary ipc-text-button imdb-header__signin-text").click()
    driver.find_element_by_xpath("/html/body[@id='styleguide-v2']/div[@id='wrapper']/div[@id='root']/div[@id='pagecontent']/div[@id='content-2-wide']/div[@id='signin-options']/div/div[@class='list-group'][1]/a[@class='list-group-item'][1]")
    driver.find_element_by_id("email").send_keys("0673748444")
    time.sleep(10)
    driver.find_element_by_id("pass").send_keys("123$asdF")
    time.sleep(10)
    driver.find_element_by_id("loginbutton").click()
    time.sleep(5)
    driver.find_element_by_class_name("pretty_btn").click()


if __name__ == '__main__':
    fb_login()