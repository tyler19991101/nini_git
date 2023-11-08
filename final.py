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
import requests






def handle_radio_selection():
    global week
    if radio_var.get() == 1:
        week = 1
        print(week)
    elif radio_var.get() == 2:
        week = 2
        print(week)

def line_notify(text):

    # 填入您的授权令牌
    access_token = 'rWtw38sw4XNd4vXop7QzWkEWearLTfuDpjzmG6lKnGh'

    # 填入您要发送的消息内容
    message = str(text)

    # 发送通知的API URL
    url = 'https://notify-api.line.me/api/notify'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'message': message
    }

    try:
        # 发送POST请求
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        print('通知已发送！')
    except requests.exceptions.HTTPError as e:
        print(f'发送通知时出错：{e}')

def start_refresh():
    while 1:
        try:
            driver.get("https://webreg.tpech.gov.tw/RegOnline1_2.aspx?ChaId=&tab=&ZCode=S&DeptCode=6001&deptname=癌症特別門診&thidname=中醫中心&rom_dr=&page=3")
            elements = driver.find_element(By.XPATH, "(//table[3]//a[text()='許中華'])[%s]"%(week))
            #elements = driver.find_element(By.XPATH, "(//table[2]//a[text()='陳依庭'])[1]")
            # table[1], [2], [3] 表示掛號系統第幾週
            # 最後面[1],[2]... 則表示出現位置，若同天兩個醫生，上面為[1]，下面[2]
            return elements
           
        except:
            time.sleep(0.3) 
            driver.refresh()
    

def start():
    global driver
    global ocr
    ocr = ddddocr.DdddOcr()
    driver = webdriver.Chrome()
    ID = "E101337752"

    try:

        elements = start_refresh()
        elements.click()

        input_element = driver.find_element(By.ID, "no")
        input_element.send_keys(ID)
        year = driver.find_element(By.XPATH, "//select[@id='y1']/option[@value='32']")
        month = driver.find_element(By.XPATH, "//select[@id='m1']/option[@value='01']")
        day = driver.find_element(By.XPATH, "//select[@id='d1']/option[@value='24']")
        year.click()
        month.click()
        day.click()
        img = catcha_image()
        test = driver.find_element(By.ID, "TextBox1")
        test.send_keys(img)        
        when1 = driver.find_element(By.ID,"daLab").text
        when2 = driver.find_element(By.ID,"turnLab").text       
        where = driver.find_element(By.ID,"RoomLab").text
        who = driver.find_element(By.ID,"DrLab").text
        confirm = driver.find_element(By.ID,"Button1")
        print(confirm)
        #掛號
        #confirm.click()

        when = when1+when2



    except Exception as e:
        print("ERROR:", str(e))
    
    line_notify("掛號成功！ ✔︎"+"\n"+"日期："+str(when)+"\n"+"診間代號："+str(where)+"\n"+"醫生："+str(who))
    # driver.quit()

def catcha_image():
    #驗證碼辨識
    img_base64 = driver.execute_script("""
        var ele = arguments[0];
        var cnv = document.createElement('canvas');
        cnv.width = ele.width; cnv.height = ele.height;
        cnv.getContext('2d').drawImage(ele, 0, 0);
        return cnv.toDataURL('image/jpeg').substring(22);    
        """, driver.find_element(By.XPATH,"//*[@id=\"IMG1\"]"))
    res = ocr.classification(img_base64)
    print("img_pass: ",res)
    return res
def showTime():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Time.set(now)                    
    now = datetime.datetime.strptime(now,'%Y-%m-%d %H:%M:%S')
    window.after(1000, showTime)    # 視窗每隔 1000 毫秒再次執行一次 showTime()
    return now


def con(): #防呆
    Month_ = Month.get()
    Day_ = Day.get()
    Hour_ = Hour.get()
    Minute_ = Minute.get()
    Second_ = Second.get()

    if Month_ =='' or Day_ =='' or Hour_ =='' or Minute_ =='' or Second_ =='':
        messagebox.showwarning("輸入未完全","有空格，請檢查！！")

    elif Month_.isalpha() or Day_.isalpha() or  Hour_.isalpha() or  Minute_.isalpha() or Second_.isalpha():
        messagebox.showwarning("輸入有誤","請輸入數字！！")
 

    result = messagebox.askokcancel('時間確認',f'確定搶票時間是 {int(Month.get())}月{int(Day.get())}日 {int(Hour.get())}點{int(Minute.get())}分{int(Second.get())}秒嗎？')
    if result is True:
        month.config(state="disabled")
        day.config(state="disabled")
        hour.config(state="disabled")
        minute.config(state="disabled")
        second.config(state="disabled")
        wednesday_radio.config(state=tk.DISABLED)
        friday_radio.config(state=tk.DISABLED)
        countdown()
        
    else:
        pass
def countdown():
    
    years2 = int(datetime.datetime.now(tz=TW_time).strftime('%Y'))
    # month2 = int(datetime.datetime.now(tz=TW_time).strftime('%m'))
    # days2 = int(datetime.datetime.now(tz=TW_time).strftime('%d'))
    if Hour.get()!='' and Minute.get()!='' and Second.get()!='':
        test = datetime.datetime(years2,int(Month.get()),int(Day.get()),int(Hour.get()),int(Minute.get()),int(Second.get()))
        test = test.strptime(str(test),'%Y-%m-%d %H:%M:%S')

        remaining_time = test - showTime()
        # 计算天数和小时数
        days = remaining_time.days
        hours = remaining_time.seconds // 3600
        minutes = (remaining_time.seconds % 3600) // 60
        seconds = remaining_time.seconds % 60
        if remaining_time.total_seconds() == 5:
            start()
        if remaining_time.total_seconds() <= 0 :
            
            print("Countdown finished!")

            month.config(state="normal")
            month.delete(0, tk.END)
            day.config(state="normal")
            day.delete(0, tk.END)
            hour.config(state="normal")
            hour.delete(0, tk.END)
            minute.config(state="normal")
            minute.delete(0, tk.END)
            second.config(state="normal")
            second.delete(0, tk.END)
            wednesday_radio.config(state=tk.NORMAL)
            friday_radio.config(state=tk.NORMAL)
            return  # 停止调用countdown()
        else:
            print("Remaining time: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))
        window.after(1000,countdown)

def calendar():
    def print_sel():
        
        s_data = str(cal.selection_get())+" "+str(hour1.get())+":"+str(minute1.get())
        date_string = str(cal.selection_get())
        year, month1, day1 = date_string.split("-")
        month.insert(0,month1)
        day.insert(0,day1)
        hour.insert(0,hour1.get())
        minute.insert(0,minute1.get())
        second.insert(0,second1.get())
        print(s_data)
        top.destroy()
    top = tk.Toplevel()
    top.geometry("300x250")
    today = datetime.date.today()
    mindate = today
    maxdate = today + datetime.timedelta(days=60)
    cal = Calendar(top, font="Arial 14", selectmode='day',locale='zh_CN',mindate=mindate,maxdate=maxdate,background="red",foreground="blue",bordercolor="red",selectbackground="red",selectforeground="red",disabledselectbackground=True)
    cal.place(x=0,y=0,width=300,height=200)
    value = 0
    value_h = ["00","01","02","03","04","05","06","07","08","09",10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    value_m = ["00","01","02","03","04","05","06","07","08","09",10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
    value_s = ["00","01","02","03","04","05","06","07","08","09",10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
    hour1 =ttk.Combobox(master=top,values=value_h,width=3,height=15,state="normal",cursor="arrow",font=("",20))
    hour1.place(x=0,y=200)
    ttk.Label(top,text="時").place(x=60,y=195,width=20,height=40)
    minute1 =ttk.Combobox(master=top,values=value_m,width=3,height=15,state="normal",cursor="arrow",font=("",20))
    minute1.place(x=80,y=200)
    ttk.Label(top,text="分").place(x=140,y=195,width=20,height=40)
    second1 =ttk.Combobox(master=top,values=value_s,width=3,height=15,state="normal",cursor="arrow",font=("",20))
    second1.place(x=160,y=200)
    ttk.Label(top,text="秒").place(x=220,y=195,width=20,height=40)
    tk.Button(top,text="確定",command=print_sel).place(x=240,y=205)

TW_time = datetime.timezone(datetime.timedelta(hours=8))    # 設定所在時區 ( 台灣是 GMT+8 )

window = Tk()
Time = tk.StringVar() 

# 設定視窗標題
window.title('Yellow-Cow Killer')
tk.Label(text="↓ 現在時間 ↓", font=('Arial',20)).pack(side="top",fill="x")
tk.Label(textvariable=Time, font=('Arial',20)).pack(side="top",fill="x")
window.geometry("300x600+250+150")
Month = tk.StringVar()
Day = tk.StringVar()
Year  = tk.StringVar()
Hour = tk.StringVar()
Minute = tk.StringVar()
Second = tk.StringVar()
tk.Label(text="何時掛號(輸入24小時制)", font=('Arial',20)).pack(side="top",fill="x")
tk.Label(text="月:").pack(side="top")
month = tk.Entry(textvariable=Month)
month.pack(side="top")
tk.Label(text="日:").pack(side="top")
day = tk.Entry(textvariable=Day)
day.pack(side="top")
tk.Label(text="時:").pack(side="top")
hour = tk.Entry(textvariable=Hour)
hour.pack(side="top")
tk.Label(text="分:").pack(side="top")
minute = tk.Entry(textvariable=Minute)
minute.pack(side="top")
tk.Label(text="秒:").pack(side="top")
second = tk.Entry(textvariable=Second)
second.pack(side="top")
start_time=tk.Button(text="透過日曆選取時間",command=calendar).pack(side="top")
tk.Button(text="確認時間",command=con).pack(side="top",fill="x",expand=True)
tk.Label(text="《看診時間》", font=('Arial',20)).pack(side="top",fill="x")
radio_var = tk.IntVar(value=1)
handle_radio_selection()
# 建立單選框
wednesday_radio = tk.Radiobutton(window, text="週三", font=('Arial',18),variable=radio_var, value=1, command=handle_radio_selection)
wednesday_radio.pack(side="top")
friday_radio = tk.Radiobutton(window, text="週五",font=('Arial',18) ,variable=radio_var, value=2, command=handle_radio_selection)
friday_radio.pack(side="top")
tk.Button(text="直接開始",command=start).pack(side="top",fill="x",expand=True)
showTime()


# 執行主程式
window.mainloop()
