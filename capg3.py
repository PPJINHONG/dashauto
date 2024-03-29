import os
import time
from datetime import datetime
from time import sleep
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor

# 이미지 폴더 지정
screenshots_path = 'ScreenShots'

# 이미지 폴더가 존재하지 않으면 생성
if not os.path.exists(screenshots_path):
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
        self.driver.set_window_size(1920, 1080) 
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit()  # Clean up driver when we are cleaned up

# 웹페이지 로그인 함수
def login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath):
    driver.get(url)
    sleep(100)
    driver.switch_to.default_content()
    driver.switch_to.parent_frame()

    try:
        driver.implicitly_wait(3)        
        driver.find_element('xpath', '//*[@id="details-button"]').click()
        sleep(10)
        driver.find_element('xpath', '//*[@id="proceed-link"]').click()
        sleep(10)
        driver.find_element('xpath', '//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div[2]/div[2]/a').click() 
        sleep(10)
    except Exception as e:
        print(e)
    finally:
        print("Step 1, login")
        driver.implicitly_wait(3)           
        username = driver.find_element('xpath', userid_xpath)                                            
        username.clear()
        username.send_keys(userid)
        sleep(3)
        print("Step 2, login")
        password = driver.find_element('xpath', passwd_xpath)
        password.clear()
        password.send_keys(passwd)
        sleep(3)
        print("Step 3, login")
        driver.find_element('xpath', login_xpath).click()
        sleep(3)

# 웹드라이버 생성 및 로그인 함수
def create_driver_and_login(bot):
    driver = Driver().driver

    if bot == "k8s_cluster_1center_ccskr-rancher-prd":
        url = "https://hubble-apne2-prd.platform.hcloud.io/grafana/login/generic_oauth"
        userid, passwd = 'cocop', 'cocop'
        userid_xpath, passwd_xpath, login_xpath = '//*[@id="username"]', '//*[@id="password"]', '//*[@id="kc-form-login"]/button'
    elif bot == "k8s_cluster_1center_ccskr-devworks-prd":
        url = "http://10.11.67.29:3000/login"
        userid, passwd = 'readonly', 'readonly!23'
        userid_xpath = '//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        passwd_xpath = '//*[@id="current-password"]'
        login_xpath = '//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
    elif bot == "k8s_cluster_1center_ccskr-dkc2hpkr-prd":
        url = "http://10.11.67.29:3000/login"
        userid, passwd = 'readonly', 'readonly!23'
        userid_xpath = '//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        passwd_xpath = '//*[@id="current-password"]'
        login_xpath = '//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
      
    login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
    return driver

# 스크린샷 촬영 함수
def take_screenshot(bot):
    print("Step 1, take_screenshot")
    try:
        driver = create_driver_and_login(bot)
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

                # 최종 페이지 및 저장파일 이름 설정
                if bot == "k8s_cluster_1center_ccskr-rancher-prd":
                    url = 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/coBoVkG4z/kr-apne1-rancher-local?orgId=27'
                    filename = f'{screenshots_path}/KR1_Rancher-prd_{datetime.now().strftime("%Y%m%d_%H%M")}.png'
                elif bot == "k8s_cluster_1center_ccskr-devworks-prd":
                    url = 'http://10.11.67.29:3000/d/1HihRd54k/coc-k8s-summary-dashboard-alert-system-kr1-kr_devworks_prd_cluster?orgId=1'
                    filename = f'{screenshots_path}/KR1_ccskr-devworks-prd_{datetime.now().strftime("%Y%m%d_%H%M")}.png'
                elif bot == "k8s_cluster_1center_ccskr-dkc2hpkr-prd":
                    url = 'http://10.11.67.29:3000/d/oOYkgdc4z/coc-k8s-summary-dashboard-alert-system-kr1-dkc2-hpkr?orgId=1'
                    filename = f'{screenshots_path}/KR1_ccskr-dkc2hpkr-prd_{datetime.now().strftime("%Y%m%d_%H%M")}.png'

                try:
                    driver.get(url)                 
                    sleep(50)                 
                    driver.set_window_size(1920, 1080)
                    sleep(10)
                    driver.maximize_window()
                    sleep(10)
                    driver.execute_script("document.body.style.zoom=0.80")
                    sleep(2)
                except Exception as e:
                    print(e)

                try:
                    driver.save_screenshot(filename)
                except KeyboardInterrupt:
                    print('Caught keyboardinterrupt')
                    pass                
                        
                print("Step 4, take_screenshot")

            except (KeyboardInterrupt, SystemExit):
                print("\nkeyboardinterrupt caught")
                print("\n... Program Stopped Manually!")
                break

    except (KeyboardInterrupt, SystemExit):
        print("\nkeyboardinterrupt caught")
        print("\n... Program Stopped Manually!")
        pass

def process_screencapture():
    number_threads = 11

    bots = [
        "k8s_cluster_1center_ccskr-rancher-prd",
        "k8s_cluster_1center_ccskr-devworks-prd",
        "k8s_cluster_1center_ccskr-dkc2hpkr-prd",
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
