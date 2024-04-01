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
        sleep(10)

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

        if bot == "netapp_prd_2center":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "netapp_manila_prd_2center":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "netapp_stg_2center":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)          
        elif bot == "storage_2center_fas_03r02":
            # Login Info              
            url = "https://172.16.9.211/sysmgr/v4/"
            # url = 'https://localhost:7001/sysmgr/v4/'
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'      
            # Login  
            sleep(10)                  
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)  
        elif bot == "storage_2center_aff_03r02":
            # Login Info              
            url = "https://172.16.9.216/sysmgr/v4/"
            # url = 'https://localhost:7002/sysmgr/v4/'
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'      
            # Login
            sleep(10)                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)            
        elif bot == "storage_2center_fas_03r03":
            # Login Info              
            url = "https://172.16.9.221/sysmgr/v4/"
            # url = 'https://localhost:7003/sysmgr/v4/'
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'      
            # Login                    
            sleep(10) 
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)  
        elif bot == "storage_2center_aff_03r03":
            # Login Info              
            url = "https://172.16.9.226/sysmgr/v4/"
            # url = 'https://localhost:7004/sysmgr/v4/'
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'      
            # Login                    
            sleep(10) 
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)  
        elif bot == "storage_2center_fas_03r04":
            # Login Info              
            url = "https://172.16.9.231/sysmgr/v4/"
            # url = 'https://localhost:7005/sysmgr/v4/'
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'      
            # Login                    
            sleep(10) 
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
                if bot == "netapp_prd_2center":        
                    url = 'http://10.11.67.29:3000/d/ytGbd1UVk/kr2-prd_netapp?orgId=1&refresh=1d'
                    filename = screenshots_path + '/KR2_PRD_NETAPP(Cinder)_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "netapp_manila_prd_2center":        
                    url = 'http://10.11.67.29:3000/d/IFrv6NWIk/kr-2center-netapp-prd-manila?orgId=1&refresh=1d'
                    filename = screenshots_path + '/KR2_PRD_NETAPP(Manila)_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "netapp_stg_2center":        
                    url = 'http://10.11.67.29:3000/d/LIdYdJU4z/kr2_stg_netapp?orgId=1'
                    filename = screenshots_path + '/KR2_STG_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_2center_fas_03r02":
                    url = 'https://172.16.9.211/sysmgr/v4/'
                    filename = screenshots_path + '/KR2_PRD_FAS_03R02_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_2center_aff_03r02":
                    url = 'https://172.16.9.216/sysmgr/v4/'
                    filename = screenshots_path + '/KR2_PRD_AFF_03R02_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_2center_fas_03r03":
                    url = 'https://172.16.9.221/sysmgr/v4/'
                    filename = screenshots_path + '/KR2_PRD_FAS_03R03_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_2center_aff_03r03":
                    url = 'https://172.16.9.226/sysmgr/v4/'
                    filename = screenshots_path + '/KR2_PRD_AFF_03R03_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_2center_fas_03r04":
                    url = 'https://172.16.9.231/sysmgr/v4/'
                    filename = screenshots_path + '/KR2_PRD_FAS_03R04_NETAPP_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                try:
                    if bot=="netapp_prd_2center" or bot=="netapp_manila_prd_2center" or bot=="netapp_stg_2center":
                        driver.get(url)                 
                        sleep(240)                 
                        driver.set_window_size(1920,1080)
                        driver.maximize_window()
                        sleep(20)
                        driver.execute_script("document.body.style.zoom=0.67")
                        sleep(2)                                     
                    
                    elif bot == "storage_2center_fas_03r02":
                # Login Info

                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[2]/div[1]/div/cluster-capacity/div/div[2]/ngb-popover-window/div[2]/nwf-dismiss-button/button').click()          
                        sleep(30)
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[3]/div/div/cluster-performance/perf-interval-selection/div/ngb-tabset/ul/li[3]/a').click()
                            
                 
                        # driver.set_window_size(1920,1080)
                        # sleep(15)
                        # driver.maximize_window()
                        # sleep(15)
                        # driver.execute_script("document.body.style.transform='scale(0.75)'")
                        sleep(2)

                    elif bot == "storage_2center_aff_03r02":
                        sleep(5)    
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[2]/div[1]/div/cluster-capacity/div/div[2]/ngb-popover-window/div[2]/nwf-dismiss-button/button').click()          
                        sleep(30)
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[3]/div/div/cluster-performance/perf-interval-selection/div/ngb-tabset/ul/li[3]/a').click()
                            
                 
                        # driver.set_window_size(1920,1080)
                        # sleep(15)
                        # driver.maximize_window()
                        # sleep(15)
                        # driver.execute_script("document.body.style.transform='scale(0.75)'")
                        sleep(2)    
                    elif bot == "storage_2center_fas_03r03":
                        sleep(5)    
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[2]/div[1]/div/cluster-capacity/div/div[2]/ngb-popover-window/div[2]/nwf-dismiss-button/button').click()          
                        sleep(30)
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[3]/div/div/cluster-performance/perf-interval-selection/div/ngb-tabset/ul/li[3]/a').click()
                            
                 
                        # driver.set_window_size(1920,1080)
                        # sleep(15)
                        # driver.maximize_window()
                        # sleep(15)
                        # driver.execute_script("document.body.style.transform='scale(0.75)'")
                        sleep(2)    
                    elif bot == "storage_2center_aff_03r03":
                # Login Info

                        try:              
                            login_url = "https://172.16.9.226/sysmgr/v4/"
                            # login_url = 'https://localhost:7004/sysmgr/v4/'
                            userid = 'spark'
                            passwd = 'tmvkzm1!'
                            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
                            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
                            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'       
                            # Login                    
                            login(driver, login_url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
                        except Exception as e:
                            print(e)
                            pass
                        sleep(10)    
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[2]/div[1]/div/cluster-capacity/div/div[2]/ngb-popover-window/div[2]/nwf-dismiss-button/button').click()          
                        sleep(30)
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[3]/div/div/cluster-performance/perf-interval-selection/div/ngb-tabset/ul/li[3]/a').click()
                            
                 
                        # driver.set_window_size(1920,1080)
                        sleep(15)
                        # driver.maximize_window()
                        sleep(15)
                        # driver.execute_script("document.body.style.transform='scale(0.75)'")
                        sleep(2)    
                    elif bot == "storage_2center_fas_03r04":
                # Login Info

          
                        try:              
                            login_url = "https://172.16.9.231/sysmgr/v4/"
                            # login_url = 'https://localhost:7005/sysmgr/v4/'
                            userid = 'spark'
                            passwd = 'tmvkzm1!'
                            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
                            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
                            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'       
                            # Login                    
                            login(driver, login_url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
                        except Exception as e:
                            print(e)
                            pass
                        sleep(60)    
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[2]/div[1]/div/cluster-capacity/div/div[2]/ngb-popover-window/div[2]/nwf-dismiss-button/button').click()          
                        sleep(30)
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[3]/div/div/cluster-performance/perf-interval-selection/div/ngb-tabset/ul/li[3]/a').click()
                            
                 
                        # driver.set_window_size(1920,1080)
                        sleep(15)
                        # driver.maximize_window()
                        sleep(15)
                        # driver.execute_script("document.body.style.transform='scale(0.75)'")
                        sleep(2)       
                    else:
                        driver.get(url)                 
                        sleep(240)                 
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

    number_threads = 8
    
    # total2의 경우 LB가 포함되어 있음
    bots = [
        "netapp_prd_2center",
        "netapp_manila_prd_2center",
        "netapp_stg_2center",
        "storage_2center_fas_03r02",
        "storage_2center_aff_03r02",
        "storage_2center_fas_03r03",
        "storage_2center_aff_03r03",
        "storage_2center_fas_03r04",
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
