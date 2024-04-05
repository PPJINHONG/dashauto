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

 #    def __del__(self):
 #       self.driver.quit() # clean up driver when we are cleaned up

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

        if bot == "lb(f5)":

            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)

        elif bot == "fw_1":
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
        # elif bot == "total_1":
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


        elif bot == "database_1":
            # Login Info              
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)  
        elif bot == "mongo":
            # Login Info              
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)  
        elif bot == "netapp_info":
            # Login Info
            url = "http://10.11.67.29:3000/login"
            userid = 'readonly'
            passwd = 'readonly!23'
            userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
            passwd_xpath='//*[@id="current-password"]'
            login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'  
            # Login                
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)                             
        elif bot == "storage_1":
            # Login Info              
            url = "https://10.107.48.110/sysmgr/v4/"
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'      
            # Login                    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)  
        elif bot == "storage_2":
            # Login Info              
            url = "https://10.107.48.130/sysmgr/v4/"
            userid = 'spark'
            passwd = 'tmvkzm1!'
            userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
            passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
            login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'    
            # Login    
            login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)                   
        # elif bot == "cluster_info_1":
        #     # Login Info              
        #     url = "http://10.11.67.29:3000/login"
        #     userid = 'readonly'
        #     passwd = 'readonly!23'
        #     userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        #     passwd_xpath='//*[@id="current-password"]'
        #     login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
        #     # Login                    
        #     login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        # elif bot == "cluster_info_2":
        #     # Login Info              
        #     url = "http://10.11.67.29:3000/login"
        #     userid = 'readonly'
        #     passwd = 'readonly!23'
        #     userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        #     passwd_xpath='//*[@id="current-password"]'
        #     login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
        #     # Login                    
        #     login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)    
        # elif bot == "cluster_info_3":
        #     # Login Info              
        #     url = "http://10.11.67.29:3000/login"
        #     userid = 'readonly'
        #     passwd = 'readonly!23'
        #     userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        #     passwd_xpath='//*[@id="current-password"]'
        #     login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
        #     # Login                    
        #     login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)    
        # elif bot == "cluster_info_4":
        #     # Login Info              
        #     url = "http://10.11.67.29:3000/login"
        #     userid = 'readonly'
        #     passwd = 'readonly!23'
        #     userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        #     passwd_xpath='//*[@id="current-password"]'
        #     login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
        #     # Login                    
        #     login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)    
        # elif bot == "cluster_info_5":
        #     # Login Info              
        #     url = "http://10.11.67.29:3000/login"
        #     userid = 'readonly'
        #     passwd = 'readonly!23'
        #     userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        #     passwd_xpath='//*[@id="current-password"]'
        #     login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
        #     # Login                    
        #     login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)

        # elif bot == "IaaS_SLA":
        #     url = "http://172.16.17.74:3000/login"
        #     userid = 'spark'
        #     passwd = 'TldhTl1!'
        #     userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        #     passwd_xpath='//*[@id="current-password"]'
        #     login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
        #     # Login                    
        #     login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)      
        # elif bot == "IaaS_Resource":
        #     url = "http://172.16.17.74:3000/login"
        #     userid = 'spark'
        #     passwd = 'TldhTl1!'
        #     userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        #     passwd_xpath='//*[@id="current-password"]'
        #     login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
        #     # Login                    
        #     login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
        # elif bot == "IaaS_Summary":
        #     url = "http://172.16.17.74:3000/login"
        #     userid = 'spark'
        #     passwd = 'TldhTl1!'
        #     userid_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input'
        #     passwd_xpath='//*[@id="current-password"]'
        #     login_xpath='//*[@id="reactRoot"]/div/main/div[3]/div/div[2]/div/div/form/button'
        #     # Login                    
        #     login(driver, url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)                      
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


                if bot == "lb(f5)":
                    url = 'http://10.11.67.29:3000/d/sjElzXFVk/sg_f5_monitor?orgId=1'
                    filename = screenshots_path + '/LB(F5)_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "fw_1":
                    url = 'http://10.11.67.29:3000/d/0kQdZuFVk/sg-fw-monitor?orgId=1'
                    filename = screenshots_path + '/FW_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "total_1":
                    url = 'http://10.11.67.29:3000/d/qstVWXF4z/sg-prd-ccs-neteuweokeu-jonghab-moniteoring?orgId=1'
                    filename = screenshots_path + '/SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'

                elif bot == "host_1":
                    url = 'http://10.11.67.29:3000/d/dPViDjKVk/sg-bm-and-netapp-resource?orgId=1'
                    filename = screenshots_path + '/HOST_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'

                elif bot == "vm_1":        
                    url = 'http://10.11.67.29:3000/d/5bY3CrK4z/sg-vm-resource?orgId=1'
                    filename = screenshots_path + '/VM_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
 
                elif bot == "database_1":
                    url = "http://10.11.67.29:3000/d/RJrKguFVz/sg-prd-db-resource-usage-top-20?orgId=1"
                    filename = screenshots_path + '/DB_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'

                elif bot == "mongo":
                    url = 'http://10.11.67.29:3000/d/1Igbn754k/na_mongodb?orgId=1'
                    filename = screenshots_path + '/mongo_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "netapp_info":        
                    url = 'http://10.11.67.29:3000/d/Bh1NWuF4k/sg-netapp-dash-board?orgId=1'
                    filename = screenshots_path + '/NETAPP_INFO_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'

                elif bot == "storage_1":
                    url = "https://10.107.48.110/sysmgr/v4/"
                    filename = screenshots_path + '/NPS1_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                elif bot == "storage_2":
                    url = 'https://10.107.48.130/sysmgr/v4/'
                    filename = screenshots_path + '/NPS2_SG_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'

                # elif bot == "cluster_info_1":
                #     url = 'http://10.11.67.29:3000/d/s-HlRO5Vk/coc-k8s-summary-dashboard-alert-system-1?orgId=1'
                #     filename = screenshots_path + '/ccs_k8s_SG_1_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                # elif bot == "cluster_info_2":
                #     url = 'http://10.11.67.29:3000/d/6bgugO5Vk/coc-k8s-summary-dashboard-alert-system-2?orgId=1'
                #     filename = screenshots_path + '/ccs_k8s_SG_2_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                # elif bot == "cluster_info_3":
                #     url = 'http://10.11.67.29:3000/d/26t9gdcVz/coc-k8s-summary-dashboard-alert-system-3?orgId=1'
                #     filename = screenshots_path + '/ccs_k8s_SG_3_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                # elif bot == "cluster_info_4":
                #     url = 'http://10.11.67.29:3000/d/1R13gO54k/coc-k8s-summary-dashboard-alert-system-4?orgId=1'
                #     filename = screenshots_path + '/ccs_k8s_SG_4_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                # elif bot == "cluster_info_5":
                #     url = 'http://10.11.67.29:3000/d/bxw6gOc4z/coc-k8s-summary-dashboard-alert-system-5?orgId=1'
                #     filename = screenshots_path + '/ccs_k8s_SG_5_1center_PRD_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'   

                # elif bot == "IaaS_SLA":
                #     url = 'http://172.16.17.74:3000/d/DuMWqtPnk/sla-dashboard?orgId=1&refresh=15m'
                #     filename = screenshots_path + '/IaaS_SLA_SG_1center_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                # elif bot == "IaaS_Resource":
                #     url = 'http://172.16.17.74:3000/d/ASnb3Sb7k/dashboard-1?orgId=1&refresh=10s'
                #     filename = screenshots_path + '/IaaS_Resource_SG_1center_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                # elif bot == "IaaS_Summary":
                #     url = 'http://172.16.17.74:3000/d/4LbjUmf7z/iaas-dashboard-4?orgId=1&refresh=10s'
                #     filename = screenshots_path + '/IaaS_Summary_SG_1center_' + datetime.now().strftime('%Y%m%d_%H%M') + '.png'
                # end_time = time.time()
                # elapsed_time = end_time - start_time
                # # print(elapsed_time)   
                # with open('elapsed_time_{}.txt'.format(bot), 'w') as t:
                #     t.write('Total elapsed time of {}: {:.2f} sec'.format(bot, elapsed_time)) 
            
                try:
                    if bot=="lb(f5)":
                        driver.get(url)                 
                        sleep(50)                 
                        driver.set_window_size(1920,1080)
                        driver.maximize_window()
                        sleep(50)
                        driver.execute_script("document.body.style.zoom=0.75")
                        
                        sleep(200)     
                    elif bot=="total_1":
                        driver.get(url)                 
                        sleep(50)                 
                        driver.set_window_size(1920,1080)
                        driver.maximize_window()
                        sleep(50)
                        driver.execute_script("document.body.style.zoom=0.5")
                        
                        sleep(200) 
                    
                    

                    elif bot == "storage_1":
                # Login Info

                        sleep(100)
                                               
                        sleep(15)
                        # try:              
                        #     login_url = "https://10.107.48.110/sysmgr/v4/"
                        #     userid = 'spark'
                        #     passwd = 'tmvkzm1!'
                        #     userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
                        #     passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
                        #     login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'       
                        #     # Login                    
                        #     login(driver, login_url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
                        # except Exception as e:
                        #     print(e)
                        #     pass
                        sleep(180)    
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[2]/div[1]/div/cluster-capacity/div/div[2]/ngb-popover-window/div[2]/nwf-dismiss-button/button').click()          
                        sleep(30)
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[3]/div/div/cluster-performance/perf-interval-selection/div/ngb-tabset/ul/li[3]/a').click()
                            
                 
                        # driver.set_window_size(1920,1080)
                        sleep(15)
                        # driver.maximize_window()
                        sleep(15)
                        # driver.execute_script("document.body.style.transform='scale(0.75)'")
                        sleep(2)                         
                    elif bot == "storage_2":
                        sleep(100)
 
                        sleep(15)
                        # Login Info              
                        # try:
                        #     login_url = "https://10.107.48.130/sysmgr/v4/"
                        #     userid = 'spark'
                        #     passwd = 'tmvkzm1!'
                        #     userid_xpath='//*[@id="nwf-login-form"]/div[1]/input'
                        #     passwd_xpath='//*[@id="nwf-login-form"]/div[2]/input'
                        #     login_xpath='//*[@id="nwf-login-form"]/div[3]/nwf-loading-button/button'    
                        #     # Login    
                        #     login(driver, login_url, userid, userid_xpath, passwd, passwd_xpath, login_xpath)
                        # except Exception as e:
                        #     print(e)
                        #     pass   
                        sleep(180)    
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[2]/div[1]/div/cluster-capacity/div/div[2]/ngb-popover-window/div[2]/nwf-dismiss-button/button').click()          
                        sleep(30)
                        driver.find_element('xpath','/html/body/app-root/ui-view/ui-view/topnav/div/ui-view/mainbody/nwf-mainbody/div/main/dashboard/div/div[3]/div/div/cluster-performance/perf-interval-selection/div/ngb-tabset/ul/li[3]/a').click()
                                     
                        # driver.set_window_size(1920,1080)
                        sleep(15)
                        # driver.maximize_window()
                        sleep(15)
                        # driver.execute_script("document.body.style.transform='scale(0.75)'")
                        sleep(2)                                       
                    elif bot=="database_1":
                        driver.get(url)                 
                        sleep(180)                 
                        driver.set_window_size(1920,1080)
                        driver.maximize_window()
                        driver.execute_script("document.body.style.zoom=0.67")
                        sleep(2)
                    # elif bot=="IaaS_SLA":
                    #     driver.get(url)                 
                    #     sleep(180)                 
                    #     driver.set_window_size(1920,1080)
                    #     driver.maximize_window()
                    #     sleep(20) 
                    # elif bot=="IaaS_Resource":
                    #     driver.get(url)                 
                    #     sleep(180)                 
                    #     driver.set_window_size(1920,1080)
                    #     driver.maximize_window()
                    #     sleep(20)
                    # elif bot=="IaaS_Summary":
                    #     driver.get(url)                 
                    #     sleep(180)                 
                    #     driver.set_window_size(1920,1080)
                    #     driver.maximize_window()
                    #     sleep(20)
                    #     driver.execute_script("document.body.style.zoom=0.90")
                    #     sleep(20)            
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

    number_threads = 16
    
    # total2의 경우 LB가 포함되어 있음
    bots = [
        "lb(f5)",
        "fw_1",
        "total_1",
        "host_1",
        "vm_1",
        "database_1",
        "mongo",
        "storage_1",
        "storage_2",
        "netapp_info",
        # "cluster_info_1",
        # "cluster_info_2",
        # "cluster_info_3",
        # "cluster_info_4",
        # "cluster_info_5",
        # "IaaS_SLA",
        # "IaaS_Resource",
        # "IaaS_Summary",

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
