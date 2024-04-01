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
        sleep(10)

        # 이동 버튼 클릭
        driver.find_element('xpath', '//*[@id="proceed-link"]').click()
        sleep(10)

        


##추가
    
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
        if bot == "k8s_cluster_2center_ccskr2-rancher-prd":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button' 
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "k8s_cluster_2center_ccs-prd":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button'
            # Login                  
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "k8s_cluster_2center_ccskr2-svchub-prd":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "k8s_cluster_2center_contents2_fcs":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "k8s_cluster_2center_contents2-wts":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "k8s_cluster_2center_epgprd":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "k8s_cluster_2center_podbbang-prd":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "k8s_cluster_2center_Hcloud":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button'
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


                if bot == "k8s_cluster_2center_ccskr2-rancher-prd":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/GgRmDQ-4z/kr_apne2_rancher_cluster-prd?orgId=27'
                    filename = screenshots_path + '/KR2_Rancher-prd_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "k8s_cluster_2center_ccs-prd":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/rBwSwVJVk/ccs_prd_cluster?orgId=27'
                    filename = screenshots_path + '/KR2_ccs-prd_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "k8s_cluster_2center_ccskr2-svchub-prd":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/rSN9C414k/ccskr2-svchub_cluster?orgId=27'
                    filename = screenshots_path + '/KR2_svchub-prd_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "k8s_cluster_2center_contents2_fcs":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/R79d6V1Vz/content2_fcs?orgId=27'
                    filename = screenshots_path + '/KR2_contents2-fcs-prd_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "k8s_cluster_2center_contents2-wts":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/BC7Fy314z/contents2-wts?orgId=27'
                    filename = screenshots_path + '/KR2_contents2-wts-prd_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "k8s_cluster_2center_epgprd":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/lGbf6VJVk/ccs_epg_cluster?orgId=27'
                    filename = screenshots_path + '/KR2_epgprd_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "k8s_cluster_2center_podbbang-prd":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/7gY_RSJVz/podbbang_cluster?orgId=27'
                    filename = screenshots_path + '/KR2_podbbang-prd_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "k8s_cluster_2center_Hcloud":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/k9v6s21Vk/ccs2_hcloud?orgId=27'
                    filename = screenshots_path + '/KR2_CCS_Hcloud_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                try:
                    driver.get(url)                 
                    sleep(240)                 
                    driver.set_window_size(1920,1080)
                    sleep(30)
                    driver.maximize_window()
                    sleep(30)
                    driver.execute_script("document.body.style.zoom=0.80")
                    sleep(15)
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

    number_threads = 15
    
    # total2의 경우 LB가 포함되어 있음
    bots = [
        "k8s_cluster_2center_ccskr2-rancher-prd",
        "k8s_cluster_2center_ccskr2-svchub-prd",
        "k8s_cluster_2center_ccs-prd",
        "k8s_cluster_2center_contents2_fcs",
        "k8s_cluster_2center_contents2-wts",
        "k8s_cluster_2center_epgprd",
        "k8s_cluster_2center_podbbang-prd",
        "k8s_cluster_2center_Hcloud"
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
