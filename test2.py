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
from selenium.webdriver import ActionChains
# def start():
#     global driver
#     global ocr
#     ocr = ddddocr.DdddOcr()
#     driver = webdriver.Chrome()
   

#     try:

        
#         driver.get("https://inline.app/booking/-LzoSPyWXzTNSaE-I4QJ:inline-live-1/-MdytTkuohNf5wnBz1vZ?language=zh-tw")
#         # 執行 JavaScript 捲動網頁
#         # 調整網頁縮放比例
#         # 設定視窗大小
#         driver.maximize_window()
#         driver.execute_script("window.scrollBy(0, 2200);")
#         time.sleep(0.7)
#         target_element = driver.find_element(By.XPATH,"//*[@id='date-picker']")
#         target_element.click()
#         time.sleep(0.5)
#         driver.execute_script("window.scrollBy(0, 260);")

#         time.sleep(0.5)
#         target_element2 = driver.find_element(By.XPATH,"//*[@id='calendar-picker']/div[1]/div[3]/div[3]/div[2]/div[2]")
#         target_element2.click()
        
#         while True:
#             time.sleep(2)
#     except Exception as e:
#         driver.refresh()
#         messagebox.showerror("Error", e)
#         return
# start()



####### variable #######
adult_num="4"
kid_num="1"
reservation_date="2023-08-07"
am_or_pm="2"  #平日只有晚餐=2 假日午餐=2 假日晚餐=4
#######################

def start_refresh():
    global driver
    driver = webdriver.Chrome()
    try:
        driver.get("https://inline.app/booking/-LzoSPyWXzTNSaE-I4QJ:inline-live-1/-LzoSQ1_si_q2njdnE5o")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 2200);")
        time.sleep(0.5)
        adult = driver.find_element(By.XPATH, f"//select[@id='adult-picker']/option[@value={adult_num}]")  # 可以改人數0~10
        adult.click()
        kid = driver.find_element(By.XPATH, f"//select[@id='kid-picker']/option[@value={kid_num}]")  #可以改人數0~10 0~8
        kid.click()
        click_date = driver.find_element(By.ID, "date-picker")
        click_date.click()
        scroll_script = f"window.scrollBy(0, {530});"
        # 执行滚动操作
        driver.execute_script(scroll_script)
        time.sleep(0.5)
        elements = driver.find_element(By.XPATH, f"//div[@data-date='{reservation_date}']") #選擇要定位日期
            # wait until 最新可訂餐日期is available
        return elements

    except Exception as e:
        driver.refresh()
        print("ERROR:", str(e))

def start():

    try:

        elements = start_refresh()
        elements.click()
        scroll_script = f"window.scrollBy(0, {600});"
        # 执行滚动操作
        driver.execute_script(scroll_script)
        time.sleep(0.7)
        for i in range(1, 9):
       #非候補
        # #// *[ @ id = "book-now-content"] / div[4] / button[9]
            booking_time = driver.find_element(By.XPATH, f"// *[ @ id = 'book-now-content'] / div[{am_or_pm}] / button[{i}]")
            #print(booking_time.text)
            value = booking_time.get_attribute("aria-expanded")

            if value != "false":
                break
        #print(value)
        booking_time.click()
        confirm_button = driver.find_element(By.XPATH, "//*[@id='book-now-action-bar']/div[2]/button")
        # time.sleep(1)
        # confirm_button.click()

        time.sleep(20)
    except Exception as e:
        print("ERROR:", str(e))
start()