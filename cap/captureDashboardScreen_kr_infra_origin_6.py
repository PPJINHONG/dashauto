import os
import sys
import signal
import time
import requests
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options

from concurrent.futures import ThreadPoolExecutor
import threading

# 이미지 폴더 지정
screenshots_path = 'ScreenShots'

# 이미지 폴더 존재 유무 체크 (필요 시 생성)
isExist = os.path.exists(screenshots_path)
if not isExist:
    os.makedirs(screenshots_path)
    print("The new directory is created!")

# 웹드라이버 클래스 (생성자/소멸자)
class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("disable-gpu")
        options.add_argument("disable-infobars")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(executable_path='chromedriver', options=options)
        self.driver.set_window_size(1920,1080) 
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit() # clean up driver when we are cleaned up

# 스레드별로 구분되는 네임스페이스 제공
thread_local = threading.local()

# 웹페이지 로그인 제공
def login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath):
    # Grafana 로그인 페이지로 이동
    driver.get(url)
    sleep(100)
    driver.switch_to.default_content()
    driver.switch_to.parent_frame()

    try:
        driver.implicitly_wait(3)        
        # 고급 버튼 클릭
        driver.find_element('xpath', '//*[@id="details-button"]').click()
        sleep(1)

        # 이동 버튼 클릭
        driver.find_element('xpath', '//*[@id="proceed-link"]').click()
        sleep(10)

        driver.find_element('xpath', '//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div[2]/div[2]/a').click() 
        sleep(10)

    except Exception as e:
        print(e)

    finally:
        print("Step 1, login")
        driver.implicitly_wait(3)           
        # UserID 입력
        username = driver.find_element('xpath', userid_xpath)                                            
        username.clear()
        username.send_keys(userid)
        sleep(3)

        print("Step 2, login")
        # Password 입력
        password = driver.find_element('xpath', passwd_xpath)
        password.clear()
        password.send_keys(passwd)
        sleep(3)

        print("Step 3, login")
        # Login 버튼 클릭
        driver.find_element('xpath', login_xpath).click()

        sleep(3)

# 웹드라이버 클래스와 로그인 함수를 사용한, 스레드별 웹페이지 띄우기
# 결과: 로그인 된 화면
def create_driver(bot):
    the_driver = getattr(thread_local, 'the_driver', None)
    if the_driver is None:

        # 웹드라이버 생성
        try:
            the_driver = Driver()
            setattr(thread_local, 'the_driver', the_driver)
        except Exception as e:
            print(e)
            pass

        # Special Initialization to login:
        try:
            driver = the_driver.driver
        except Exception as e:
            print(e)
            pass

        print("Step 1, create_driver")
        print(bot)
        sleep(30)
        if bot == "IaaS_SLA":
            url = "http://172.16.17.74:3000/login"
            userid = 'spark'
            passwd = 'TldhTl1!'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)      
        elif bot == "IaaS_Resource":
            url = "http://172.16.17.74:3000/login"
            userid = 'spark'
            passwd = 'TldhTl1!'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "IaaS_Summary":
            url = "http://172.16.17.74:3000/login"
            userid = 'spark'
            passwd = 'TldhTl1!'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
    return driver

def take_screenshot(bot):
    print("Step 1, take_screenshot")
    # 웹드라이버 생성
    try:
        driver = create_driver(bot)
    except KeyboardInterrupt:
        print('Caught keyboardinterrupt')
        pass

    print("Step 2, take_screenshot")   

    try:
        while True:
            try:
                print(f"Capturing the screens started at {datetime.now()}")
                print(f"It captures every 5 mins")
                print("Step 3, take_screenshot")

                start_time = time.time()

                # 최종(대시보드) 페이지 및 저장파일 이름 설정
                if bot == "IaaS_SLA":
                    url = 'http://172.16.17.74:3000/d/DuMWqtPnk/sla-dashboard?orgId=1'
                    filename = screenshots_path + '/KR2_IaaS_SLA_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "IaaS_Resource":
                    url = 'http://172.16.17.74:3000/d/ASnb3Sb7k/dashboard-1?orgId=1'
                    filename = screenshots_path + '/KR2_IaaS_Resource_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "IaaS_Summary":
                    url = 'http://172.16.17.74:3000/d/4LbjUmf7z/iaas-dashboard-4?orgId=1'
                    filename = screenshots_path + '/KR2_IaaS_Summary_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
            
                try:
                    if bot=="IaaS_SLA":
                        driver.get(url)                 
                        sleep(140)                 
                        driver.set_window_size(1920,1080)
                        sleep(20)
                        driver.maximize_window()
                        sleep(20) 
                    elif bot=="IaaS_Resource":
                        driver.get(url)                 
                        sleep(140)                 
                        driver.set_window_size(1920,1080)
                        sleep(20)
                        driver.maximize_window()
                        sleep(20)
                    elif bot=="IaaS_Summary":
                        driver.get(url)                 
                        sleep(140)                 
                        driver.set_window_size(1920,1080)
                        sleep(20)
                        driver.maximize_window()
                        sleep(20)
                        driver.execute_script("document.body.style.zoom=0.90")
                        sleep(20)
                    else:
                        driver.get(url)                 
                        sleep(140)                 
                        driver.set_window_size(1920,1080)
                        sleep(10)
                        driver.maximize_window()
                        sleep(10)
                        driver.execute_script("document.body.style.zoom=0.80")
                        sleep(2)
                except Exception as e:
                    print(e)

                # 화면 캡처 수행
                try:
                    driver.save_screenshot(filename)
                except KeyboardInterrupt:
                    print('Caught keyboardinterrupt')
                    pass                
                        
                print("Step 4, take_screenshot")

            # 예외 처리
            except (KeyboardInterrupt, SystemExit):
                print("\nkeyboardinterrupt caught")
                print("\n... Program Stopped Manually!")
                exiting.set()
            break

    # 예외 처리
    except (KeyboardInterrupt, SystemExit):
        print("\nkeyboardinterrupt caught")
        print("\n... Program Stopped Manually!")
        exiting.set()

def process_screencapture():

    number_threads = 3
    
    # total2의 경우 LB가 포함되어 있음
    bots = [
        "IaaS_SLA",
        "IaaS_Resource",
        "IaaS_Summary",
    ]

    with ThreadPoolExecutor(max_workers=number_threads) as pool:
        try:
            pool.map(take_screenshot, bots)
        except KeyboardInterrupt:
            print('Caught keyboardinterrupt')
            pass

if __name__ == "__main__":
    try:
        process_screencapture()
    except KeyboardInterrupt:
        print('Caught keyboardinterrupt')
        pass

    # 스레드 네임스페이스 삭제
    # Quit the selenium drivers:
    del thread_local

    # 메모리 캐시 삭제
    import gc
    gc.collect() # a little extra insurance
