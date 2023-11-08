import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
import time
import base64
import ddddocr
import tkinter as tk 
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
import datetime

def usr_login(phone, pwd):
        # 找到 "會員登入" 按鈕
        button = driver.find_element(By.XPATH, "//button[contains(text(), '會員登入')]")
        # 使用 JavaScript 點擊按鈕
        driver.execute_script("arguments[0].click();", button)
        # 填寫電話號碼和密碼欄位
        phone_input = driver.find_element(By.XPATH, "//input[@name='phoneNumber']")
        phone_input.send_keys(phone)

        password_input = driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(pwd)
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()


def location(location):
    divs = driver.find_elements(By.CSS_SELECTOR, "div.css-1q0h9xx > div")
    target_div = divs[location] 
    # print(target_div.text)
    city = target_div.find_element(By.XPATH,".//div[@class='sc-jNXgPE bAwFVV']//button[contains(text(), '立即訂位')]")
    city.click()
    # test = driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]/button")
    # test.click()    


def people(target_div,human):
    aa = target_div.find_element(By.XPATH,".//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-adornedEnd MuiInputBase-readOnly sc-cQwIYT llLXOZ css-srhau5']")
    aa.click()

    bb = driver.find_element(By.XPATH,"//div[@class='sc-fJExmy cBUNma']//div[@class='sc-WCkqM bcTSzI']//div[@class='sc-bhVIhj eWTjrn']//button[contains(text(), '+')]")
    # 連續點擊
    for i in range(human):
        i
        driver.execute_script("arguments[0].click();", bb)

def times(target_div,when):
    cc = target_div.find_element(By.XPATH,"//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary sc-knuRna ettEBt css-1p9j1jv']")
    cc.click()
    # print(target_div.text)
    dd = driver.find_element(By.XPATH,"//div[@id='menu-timeSlot']//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiPaper-root MuiMenu-paper MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-1upby8d']//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-jnmgom']")
    # 在 <ul> 元素中找到所有的 <li> 元素
    lis = dd.find_elements(By.XPATH, ".//li")
    # print(lis[2].text)
    lis[when+1].click()

def date(target_div,month,day):
        
        weekday_mapping = {
            "Monday": "一",
            "Tuesday": "二",
            "Wednesday": "三",
            "Thursday": "四",
            "Friday": "五",
            "Saturday": "六",
            "Sunday": "日"
        }
        year = datetime.datetime.now().year
        date = datetime.date(year, month, day)
        weekday = date.strftime("%A") 
        weekday_chinese = weekday_mapping.get(weekday, "") 
        aa = target_div.find_element(By.XPATH,".//div[@class='sc-oclUV sc-kTGBUR ktMeUI ljgTdh']")
        aa.click()
        # # 找到大 <div> 元素
        big_div = driver.find_element(By.XPATH, "//div[@class='react-datepicker']")
        xpath = "//div[@aria-label='Choose 2023年{}月{}日 星期{}']//div[@class='sc-czShuu iGrUGw']".format(month, day,weekday_chinese)
        choose_div = big_div.find_element(By.XPATH, xpath)
        choose_div.click()


def start():
    global driver
    global ocr
    ocr = ddddocr.DdddOcr()
    driver = webdriver.Chrome()
   

    try:
        time.sleep(0.3)
        driver.get("https://youtube")
        
        # driver.maximize_window()
        # # 登入
        # usr_login("0900498886", "tyler19991101")
        
        # # 按X
        # elements = driver.find_element(By.XPATH,"//div[@id='root']//div[@class='sc-bczRLJ enoLQn']//main[@class='sc-dkzDqf jwcMVQ']//div[@class='sc-breuTD iLQxFV']//div[@class='sc-evZas sc-ksZaOG cKXYvf fdAlHL']//div[@class='sc-hAZoDl cHVSmW']//div[@class='sc-fnykZs RuPjI']/*[name()='svg']")
        # elements.click()
       
        # driver.execute_script("window.scrollBy(0, 300);")
        # time.sleep(0.5)
        # # 餐廳位置 0= 信義 1= 新莊
        
        # location(1)
        
        
        # divs = driver.find_elements(By.CSS_SELECTOR, "div.sc-fbHdRr.jYkEyS > div")
        # # 人數
        # people(divs[1],4)
        # # 時段 0= 中午 1= 下午 2= 晚上
        # times(divs[2],1)

        # date(divs[3],8,9)

        # submit_button = driver.find_element(By.XPATH, "//button[@class='sc-hKMtZM sc-bjjCGC QlVA-D gYprCY searchBooking']")
        # submit_button.click()
        # time.sleep(0.3)
        # test = driver.find_element(By.XPATH, "//div[@class='sc-zsjhC hASaJf']")
        
        # buttons = test.find_elements(By.TAG_NAME, "button")
        # buttons[0].click()
        # # print(buttons[0].text)
        # while True:
        #     time.sleep(2)
    except Exception as e:
        driver.refresh()
        messagebox.showerror("Error", e)
        return
start()
