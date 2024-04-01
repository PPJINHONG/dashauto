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
        caps = webdriver.DesiredCapabilities.CHROME.copy()
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
        if bot == "dummy_client":
            url = "https://ccsdev-dummy-aws.live/login"
            userid = 'coc@hyundai.com'
            passwd = 'coc1!'
            userid_xpath='//*[@id="reactRoot"]/div[1]/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div[1]/main/div[3]/div/div[2]/div/div/form/button'
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "network":
            # Login Info
            url = "http://10.7.19.118:3000/login"
            userid = 'monitor'
            passwd = 'P@ssw0rd'
            userid_xpath='//*[@id="login-view"]/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="login-view"]/div/form/div[2]/div[2]/div/div/input'
            login_xpath='//*[@id="login-view"]/div/form/button'
            # Login        
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "network_2":
            # Login Info
            url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
            userid = 'cocop'
            passwd = 'cocop'
            userid_xpath='//*[@id="username"]'
            passwd_xpath='//*[@id="password"]'
            login_xpath='//*[@id="kc-form-login"]/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        elif bot == "lb(a10)":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)

        elif bot == "lb(f5)":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)

        elif bot == "total_1":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)

        elif bot == "total_2":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)

        elif bot == "host_1":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
           
        elif bot == "host_1_new":
            # Login Info            
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath) 

        elif bot == "vm_1":
            # Login Info            
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath) 

        elif bot == "host_2":
            # Login Info              
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)   

        elif bot == "vm_2":
            # Login Info              
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
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
                if bot == "dummy_client":
                    url = 'https://ccsdev-dummy-aws.live/d/8Wa4pnYVk/kr-ccs-dummy-client?orgId=1&refresh=10s'
                    filename = screenshots_path + '/DUMMY_CLIENT_KR_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "network":
                    url = 'http://10.7.19.118:3000/d/Ax-HFsa4z/yiwang-ccs-bordermoniteoring-keulraudeuunyeongsenteo?orgId=1&from=now-2d&to=now'
                    filename = screenshots_path + '/KR1_BORDER_NETWORK_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "network_2":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/RbJ9FxXnk/inteones-caryang-data-sms-hoeseon?orgId=13&from=now-2d&to=now'
                    filename = screenshots_path + '/KR2_BORDER_NETWORK_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "lb(a10)":
                    url = 'http://10.11.67.29:3000/d/tdbzxsNnz1/kr-a10-3030-old-a10?orgId=1&from=now-2d&to=now'
                    filename = screenshots_path + '/KR1_A10_LB(KRTMS-PRD-L7)_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "lb(f5)":
                    url = 'http://10.11.67.29:3000/d/ixuLyos7k/kr-lb-f5?from=now-2d&to=now&orgId=1'
                    filename = screenshots_path + '/KR1_F5_LB(KRCLOUD-PRD-L7)_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "total_1":
                    url = 'http://10.11.67.29:3000/d/-zbrCFr7g/kr-1senteo-prd-ccs-neteuweokeu-jonghab-moniteoring?orgId=1&from=now-2d&to=now'
                    filename = screenshots_path + '/KR1_Network_Monitor_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "total_2":
                    url = 'http://10.11.67.29:3000/d/9zxCEzp4k/kr-2senteo-prd-ccs-neteuweokeu-jonghab-moniteoring?orgId=1'
                    filename = screenshots_path + '/KR2_Network_Monitor_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "host_1":
                    url = 'http://10.11.67.29:3000/d/vGUN6GW4z/kr-1senteo-prd-old-bm-resources?orgId=1&from=now-30m&to=now'
                    filename = screenshots_path + '/KR1_OLD_PRD_HOST_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "host_1_new":
                    url = 'http://10.11.67.29:3000/d/yo86eMWVz/kr-1senteo-prd-new-bm-resources?orgId=1&from=now-30m&to=now'
                    filename = screenshots_path + '/KR1_NEW_PRD_HOST_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "host_2":
                    url = 'http://10.11.67.29:3000/d/U_asi7W4z/kr-2senteo-prd-bm-resources?orgId=1&from=now-30m&to=now'
                    filename = screenshots_path + '/KR2_HOST_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "vm_1":        
                    url = 'http://10.11.67.29:3000/d/yVNMjMZVk/kr-1senteo-prd-vm-resources?orgId=1&from=now-30m&to=now'
                    filename = screenshots_path + '/KR1_PRD_VM_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "vm_2":        
                    url = 'http://10.11.67.29:3000/d/Jxvrz7Z4k/kr-2senteo-prd-vm-resources?orgId=1&from=now-30m&to=now'
                    filename = screenshots_path + '/KR2_PRD_VM_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'         
                try:
                    if bot=="dummy_client" or bot=="network_2":
                        sleep(20)
                        driver.get(url)                 
                        sleep(100)                 
                        driver.set_window_size(1920,1080)
                        sleep(20)
                        driver.maximize_window()
                        sleep(20)
                        driver.execute_script("document.body.style.zoom=0.67")
                        sleep(20) 
                    elif bot=="lb(a10)":
                        driver.get(url)                 
                        sleep(180)                 
                        driver.set_window_size(1920,1080)
                        driver.maximize_window()
                        sleep(2)
                        driver.execute_script("document.body.style.zoom=0.58")
                        sleep(2)
                        sleep(20)     
                    elif bot=="total_2":
                        driver.get(url)                 
                        sleep(180)                 
                        driver.set_window_size(1920,1080)
                        driver.maximize_window()
                        sleep(20)
                        driver.execute_script("document.body.style.zoom=0.50")
                        sleep(20)
                    else:
                        driver.get(url)                 
                        sleep(180)                 
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

    number_threads = 12
    
    # total2의 경우 LB가 포함되어 있음
    bots = [
        "dummy_client",
        "network",
        "network_2",
        "lb(a10)",
        "lb(f5)",
        "total_1",
        "total_2",
        "host_1",
        "host_1_new",
        "vm_1",
        "host_2",
        "vm_2",
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



#with 문 이용한 자원 반납 고려해야함