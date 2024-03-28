# step1.관련 패키지 및 모듈 import
from schedule import every, repeat, run_pending, clear
from datetime import datetime
from time import sleep

import smtplib

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.create_report_infra_new import *
from utils.create_report_kr_jeniffer import *
from utils.SMTP_new import *

# 각리전 기준시간 09:00 에 보내야함 
# 리전별 메일 각각 한개에 보고서 각각 첨부하여 보낼것

def main():
    # filename1 = 'Infra_in_detail_' + datetime.now().strftime('%Y%m%d-%H%M') + '.pdf'
    # filename2 = 'Jennifer_dashboard_' + datetime.now().strftime('%Y%m%d-%H%M') + '.pdf'

    # 테스트 ::: 10분 마다
    # every(20).minutes.do(gen_infra_pdf)
    # every(20).minutes.do(gen_jeniffer_pdf)
    # every(20).minutes.do(send_email)

    # 추석연휴
    # # 1사간 마다, 50분에
    # every().hours.at(":21").do(gen_infra_pdf)
    # every().hours.at(":21").do(gen_jeniffer_pdf)
    # # 1시간 마다, 정시에 
    # every().hours.at(":00").do(send_email) 
    # # 한시간 한번, 50분에
    gen_infra_pdf("KR")
    gen_jeniffer_pdf()
    send_email("KR")

    # # 하루 한번, 9시 00분에
    # every().day.at("08:50").do(gen_infra_pdf)pytho
    # every().day.at("08:55").do(gen_jeniffer_pdf)
    
 #   try:
 #       while True:    
 #           run_pending()
 #           sleep(1)
 #   except KeyboardInterrupt as e:
 #       print(e)
 #       # Remove all jobs
 #       clear()
 #       pass

if __name__ == '__main__':
    main()
