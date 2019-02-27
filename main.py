from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

url = ""
key = []
chkKey = False

with open("key_value", mode='r') as f:
    for s_line in f:
        key.append(s_line.replace('\n',''))
browser = webdriver.PhantomJS()
browser.implicitly_wait(5)
browser.get(url)
if key[0] == "":
    chkKey = True
    key[0] = input("Input ASP_ID: ")
if key[1] == "":
    key[1] = input("Input ASP_PASSWORD: ")
browser.find_element_by_id("uAspLogin_TxtUser").send_keys(key[0])
browser.find_element_by_id("uAspLogin_TxtPass").send_keys(key[1])
browser.find_element_by_id("uAspLogin_BtnLogin").click()
element = browser.find_element_by_xpath("//*[@id='DdlKaisya']")
Select(element).select_by_value("") # valueの値(入力必須)
if key[2] == "":
    key[2] = input("Input USER_ID: ")
browser.find_element_by_id("TxtUser").send_keys(key[2])
if key[3] == "":
    key[3] = input("Input PASSWORD: ")
browser.find_element_by_id("TxtPass").send_keys(key[3])
browser.find_element_by_id("BtnLogin").click()

sleep(1)
browser.find_element_by_id("BtnCheckAll").click()
sleep(1)
browser.find_element_by_id("BtnInp").click()
sleep(1)
if chkKey:
    ans = input("Do you want to save your settings ? (y/n): ")
    if ans == "y":
        with open("key_value", mode='w') as f:
            for item in key:
                f.write(item+"\n")
browser.quit()
exit()
