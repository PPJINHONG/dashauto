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
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-proxy-certificate-handler")
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
    sleep(60)
    driver.switch_to.default_content()
    driver.switch_to.parent_frame()

    try:
        driver.implicitly_wait(3)        
        # 고급 버튼 클릭
        driver.find_element('xpath', '//*[@id="details-button"]').click()
        sleep(1)

        # 이동 버튼 클릭
        driver.find_element('xpath', '//*[@id="proceed-link"]').click()
        sleep(50)

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
        sleep(10)

        print("Step 2, login")
        # Password 입력
        password = driver.find_element('xpath', passwd_xpath)
        password.clear()
        password.send_keys(passwd)
        sleep(10)

        print("Step 3, login")
        # Login 버튼 클릭
        driver.find_element('xpath', login_xpath).click()

        sleep(10)

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
        if bot == "database_1":
            # Login Info              
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)  

        elif bot == "database_2":
            # Login Info              
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)      
        elif bot == "netapp(nvme)":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "netapp(old&new_prd_bigdata)":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "netapp(stg)":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)                              
        elif bot == "storage_new_1":
            # Login Info              
            url = "https://10.7.0.231/"
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/dl/dd[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/dl/dd[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/button'     
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)  
        elif bot == "storage_new_2":
            # Login Info              
            url = "https://10.7.0.231/"
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/dl/dd[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/dl/dd[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/button' 
            # Login    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)               
        elif bot == "storage_old_1":
            # Login Info              
            url = "https://10.7.0.231/"
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/dl/dd[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/dl/dd[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/button'
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
                if bot == "database_1":
                    url = "http://10.11.67.29:3000/d/JU5R-_m4k/kr-1senteo-prd-db-resource-usage-top-20?orgId=1&from=now-6h&to=now"
                    filename = screenshots_path + '/KR1_PRD_DB_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "database_2":
                    url = "http://10.11.67.29:3000/d/bxdzB_iVz/kr-2senteo-prd-db-resource-usage-top-20?orgId=1&from=now-6h&to=now"
                    filename = screenshots_path + '/KR2_PRD_DB_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "netapp(nvme)":        
                    url = 'http://10.11.67.29:3000/d/MWXLP7K4z1/kr-1center-netapp-nvme-dash-board?orgId=1'
                    filename = screenshots_path + '/KR1_PRD_NETAPP(NVME)_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "netapp(old&new_prd_bigdata)":        
                    url = 'http://10.11.67.29:3000/d/jhvYINK4z2/kr-1centor-old-prd-and-new-prd-big-data?orgId=1'
                    filename = screenshots_path + '/KR1_OLD&NEW_PRD_BIGDATA_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "netapp(stg)":        
                    url = 'http://10.11.67.29:3000/d/gHJ-NHK4k3/kr-1centor-stg-netapp-dash-board?orgId=1'
                    filename = screenshots_path + '/KR1_STG_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_new_1":
                    url = "https://10.7.0.231/clusters/53770/explorer"
                    filename = screenshots_path + '/KR1_NETAPP(NVMe01)NPS1_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_new_2":
                    url = 'https://10.7.0.231/clusters/133326/explorer'
                    filename = screenshots_path + '/KR1_NETAPP(NVMe02)NPS1_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_old_1":
                    url = 'https://10.7.0.231/clusters/15462/explorer'
                    filename = screenshots_path + '/KR1_OLDPRD_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
            
                try:
                    if bot == "storage_new_1":
                # Login Info
                        try:              
                            login_url = "https://10.7.0.231/"
                            userid = 'spark'
                            passwd = 'tmvkzm1!'
                            userid_xpath='//*[@id="nwf-login-form"]/dl/dd[1]/input'
                            passwd_xpath='//*[@id="nwf-login-form"]/dl/dd[2]/input'
                            login_xpath='//*[@id="nwf-login-form"]/button'
                            # Login
                            login(driver, login_url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
                        except Exception as e:
                            print(e)
                            pass                         
                        sleep(30)
                        driver.get(url)                        
                        sleep(240)
                        driver.find_element('xpath','//*[@id="mainViewContainer"]/main/div/div/div[3]/div/performance-explorer/nwf-grid-params-controller/div[2]/div/div[2]/span').click()
                        sleep(30)                   
                        driver.set_window_size(1920,1080)
                        sleep(20)
                        driver.maximize_window()
                        sleep(20)                         
                    elif bot == "storage_new_2":
                        try:              
                            login_url = "https://10.7.0.231/"
                            userid = 'spark'
                            passwd = 'tmvkzm1!'
                            userid_xpath='//*[@id="nwf-login-form"]/dl/dd[1]/input'
                            passwd_xpath='//*[@id="nwf-login-form"]/dl/dd[2]/input'
                            login_xpath='//*[@id="nwf-login-form"]/button'
                            # Login
                            login(driver, login_url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
                        except Exception as e:
                            print(e)
                            pass                         
                        sleep(30)
                        driver.get(url)                        
                        sleep(240)
                        driver.find_element('xpath','//*[@id="mainViewContainer"]/main/div/div/div[3]/div/performance-explorer/nwf-grid-params-controller/div[2]/div/div[2]/span').click()
                        sleep(30)                   
                        driver.set_window_size(1920,1080)
                        sleep(20)
                        driver.maximize_window()
                        sleep(20)                                        
                    elif bot == "storage_old_1":
                        try:              
                            login_url = "https://10.7.0.231/"
                            userid = 'spark'
                            passwd = 'tmvkzm1!'
                            userid_xpath='//*[@id="nwf-login-form"]/dl/dd[1]/input'
                            passwd_xpath='//*[@id="nwf-login-form"]/dl/dd[2]/input'
                            login_xpath='//*[@id="nwf-login-form"]/button'
                            # Login
                            login(driver, login_url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
                        except Exception as e:
                            print(e)
                            pass                         
                        sleep(30)
                        driver.get(url)                        
                        sleep(240)
                        driver.find_element('xpath','//*[@id="mainViewContainer"]/main/div/div/div[3]/div/performance-explorer/nwf-grid-params-controller/div[2]/div/div[2]/span').click()
                        sleep(30)                   
                        driver.set_window_size(1920,1080)
                        sleep(20)
                        driver.maximize_window()
                        sleep(20)
                    elif bot=="database_1" or bot=="database_2":
                        driver.get(url)                 
                        sleep(240)                 
                        driver.set_window_size(1920,1080)
                        driver.maximize_window()
                        sleep(20)
                        driver.execute_script("document.body.style.zoom=0.67")
                        sleep(2)
                    elif bot=="netapp(nvme)" or bot=="netapp(old&new_prd_bigdata)" or bot=="netapp(stg)":
                        driver.get(url)                 
                        sleep(240)                 
                        driver.set_window_size(1920,1080)
                        driver.maximize_window()
                        sleep(20)
                        driver.execute_script("document.body.style.zoom=0.67")
                        sleep(2)
                    else:
                        driver.get(url)                 
                        sleep(240)                 
                        driver.set_window_size(1920,1080)
                        sleep(20)
                        driver.maximize_window()
                        sleep(20)
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

    number_threads = 8
    
    # total2의 경우 LB가 포함되어 있음
    bots = [
        "database_1",
        "database_2",
        "netapp(nvme)",
        "netapp(old&new_prd_bigdata)",
        "netapp(stg)",
        "storage_new_1",
        "storage_new_2",
        "storage_old_1",
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
