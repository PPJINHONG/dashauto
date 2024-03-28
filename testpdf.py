# -*- coding: utf-8 -*-
from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from PIL import Image
from time import sleep
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
mpl.rcParams['axes.unicode_minus']=False

import os
import glob




screenshots_path = 'ScreenShots'

isExist = os.path.exists(screenshots_path)
if not isExist:
    os.makedirs(screenshots_path)
    print("The new directory is created!")

# 리포트 폴더 지정
pdf_path = 'Reports'

# 리포트 폴더 존재 유무 체크 (필요 시 생성)
isExist = os.path.exists(pdf_path)
if not isExist:
    os.makedirs(pdf_path)
    print("The new directory is created!")



    


def createpdf(region):
    
    sentence_dict = {
        "KR": {
            "sentence_h1": [
                'KR1 상단 레거시 네트워크 - ISP회선(Internet, SMS, AWS) Traffic, FW CPU/Session',
                'KR2 상단 네트워크 - ISP회선(Internet, 차량DATA/SMS, AWS) Traffic',
                'KR1 TMS L7 - CPU,Memory,Connection,SNAT Pool Status, L7↔Backbone Traffic',
                'KR1 Cloud L7 - CPU, Memory, Service/SNAT Connection',
                'KR1 Network - CGN CPU,MEM, A10/F5 ServiceConnection, BorderLeaf/CGN Traffic',
                'KR2 Network - 의왕↔상암 전용회선 Traffic, Edge↔Router Traffic, NetworkLeaf↔FW/L7 Traffic, FW/L7 CPU/Memory/Connection',
                'KR1 TMS BM - CPU, Memory, Disk Free(%)',
                'KR1 Cloud BM - CPU, Memory, Disk Free(%)',
                'KR2 BM - CPU, Memory, Disk Free(%)',
                'KR1 VM - CPU, Memory, Disk Free(%)',
                'KR2 VM - CPU, Memory, Disk Free(%)',
                'KR1 DB - CPU, Memory, session',
                'KR2 DB - CPU, Memory, session',
                'KR1 CLOUD Netapp(NVME) - DISK usage, Spine↔Netapp CinderTraffic',
                'KR1 TMS,CDO Netapp(SAS,SSD) - DISK usage, Spine↔Netapp CinderTraffic',
                'KR1 TMS Netapp(SAS,SSD) - DISK usage, Spine↔Netapp CinderTraffic',
                'Storage: 1센터 신운영계 스토리지 클러스터 #1의 IOPS, Throughput 정보',
                'Storage: 1센터 신운영계 스토리지 클러스터 #2의 IOPS, Throughput 정보',
                'Storage: 1센터 구운영계 스토리지 클러스터의 IOPS, Throughput 정보',
                '',
                '',
                '',
                'Storage: 2센터 운영계 스토리지 클러스터 #1의 IOPS, Throughput 정보',
                'Storage: 2센터 운영계 스토리지 클러스터 #2의 IOPS, Throughput 정보',
                'Storage: 2센터 운영계 스토리지 클러스터 #3의 IOPS, Throughput 정보',
                'Storage: 2센터 운영계 스토리지 클러스터 #4의 IOPS, Throughput 정보',
                'Storage: 2센터 운영계 스토리지 클러스터 #5의 IOPS, Throughput 정보',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
            ],
            "sentence_h2": [
                '',
                '',
                '메모리 70% 이상 일경우 유의하여 모니터링',
                '',
                '',
                'IP 1개당 최대 NAT Connection 약 63000여개',
                'BM(Bare Metal): CCS내 모든 물리서버 대상 Worst Top 10 정보. Red가 아니면 모두 정상 (Red 기준 : CPU 10% 이하, 메모리 1G이하, free Disk 10% 이하)',
                'BM(Bare Metal): CCS내 모든 물리서버 대상 Worst Top 10 정보. Red가 아니면 모두 정상 (Red 기준 : CPU 10% 이하, 메모리 1G이하, Usage 90% 이상)',
                'BM(Bare Metal): CCS내 모든 물리서버 대상 Worst Top 10 정보. Red가 아니면 모두 정상 (Red 기준 : CPU 10% 이하, 메모리 3G이하, Usage 90% 이상)',
                'VM: CCS내 모든 가상서버 대상 Worst Top 10 정보 (Red 기준 : CPU 10% 이하, 메모리 500M이하, free Disk 10% 이하)',
                'VM: CCS내 모든 가상서버 대상 Worst Top 10 정보 (Red 기준 : CPU 10% 이하, 메모리 500M이하, free Disk 10% 이하)',
                '',
                '',
                '',
                '',
                '',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '',
                '',
                '',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
            ],
            "sentence_h3": [
                'http://10.7.19.118:3000/d/Ax-HFsa4z/yiwang-ccs-bordermoniteoring-keulraudeuunyeongsenteo?orgId=1&from=now-2d&to=now&refresh=30m',
                'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/RbJ9FxXnk/inteones-caryang-data-sms-hoeseon?orgId=13&from=now-2d&to=now',
                'http://10.11.67.29:3000/d/tdbzxsNnz1/kr-a10-3030-old-a10?orgId=1&refresh=5m&from=now-2d&to=now',
                'http://10.11.67.29:3000/d/ixuLyos7k/kr-lb-f5?from=now-2d&to=now&orgId=1&refresh=5m',
                'http://10.11.67.29:3000/d/-zbrCFr7g/1senteo-ccs-neteuweokeu-jonghab-moniteoring?orgId=1&from=now-2d&to=now',
                'http://10.11.67.29:3000/d/9zxCEzp4k/kr-2senteo-prd-ccs-neteuweokeu-jonghab-moniteoring?orgId=1&refresh=5m',
                'http://10.11.67.29:3000/d/vGUN6GW4z/kr-1senteo-prd-old-bm-resources?orgId=1&from=now-30m&to=now&refresh=30m',
                'http://10.11.67.29:3000/d/yo86eMWVz/kr-1senteo-prd-new-bm-resources?orgId=1&from=now-30m&to=now&refresh=30m',
                'http://10.11.67.29:3000/d/U_asi7W4z/kr-2senteo-prd-bm-resources?orgId=1&refresh=30m&from=now-30m&to=now',
                'http://10.11.67.29:3000/d/yVNMjMZVk/kr-1senteo-prd-vm-resources?orgId=1&refresh=30m&from=now-30m&to=now',
                'http://10.11.67.29:3000/d/Jxvrz7Z4k/kr-2senteo-prd-vm-resources?orgId=1&from=now-30m&to=now&refresh=30m',
                'http://10.11.67.29:3000/d/JU5R-_m4k/kr-1senteo-prd-db-resource-usage-top-20?orgId=1&from=now-6h&to=now&refresh=30m',
                'http://10.11.67.29:3000/d/bxdzB_iVz/kr-2senteo-prd-db-resource-usage-top-20?orgId=1&refresh=30m&from=now-6h&to=now',
                'http://10.11.67.29:3000/d/MWXLP7K4z1/kr-1center-netapp-nvme-dash-board?orgId=1&refresh=1d',
                'http://10.11.67.29:3000/d/jhvYINK4z2/kr-1centor-old-prd-and-new-prd-big-data?orgId=1&refresh=1d',
                'http://10.11.67.29:3000/d/gHJ-NHK4k3/kr-1centor-stg-netapp-dash-board?orgId=1&refresh=1d',
                'https://10.7.0.231/clusters/53770/explorer',
                'https://10.7.0.231/clusters/133326/explorer',
                'https://10.7.0.231/clusters/15462/explorer',
                'http://10.11.67.29:3000/d/ytGbd1UVk/kr2-prd_netapp?orgId=1&refresh=1d',
                'http://10.11.67.29:3000/d/IFrv6NWIk/kr-2center-netapp-prd-manila?orgId=1&refresh=1d',
                'http://10.11.67.29:3000/d/LIdYdJU4z/kr2_stg_netapp?orgId=1',
                'https://172.16.9.211/sysmgr/v4/',
                'https://172.16.9.216/sysmgr/v4/',
                'https://172.16.9.221/sysmgr/v4/',
                'https://172.16.9.226/sysmgr/v4/',
                'https://172.16.9.231/sysmgr/v4/',
                'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/coBoVkG4z/kr-apne1-rancher-local?orgId=27',
                'http://10.11.67.29:3000/d/1HihRd54k/coc-k8s-summary-dashboard-alert-system-kr1-kr_devworks_prd_cluster?orgId=1',
                'http://10.11.67.29:3000/d/oOYkgdc4z/coc-k8s-summary-dashboard-alert-system-kr1-dkc2-hpkr?orgId=1',
                'http://10.11.67.29:3000/d/95RgRd54z/coc-k8s-summary-dashboard-alert-system-kr1-dkc2-kpg?orgId=1',
                'http://10.11.67.29:3000/d/q20rev5Vz/coc-k8s-summary-dashboard-alert-system-kr1-dkc2-kpl?orgId=1',
                'http://10.11.67.29:3000/d/X0-SRdc4z/coc-k8s-summary-dashboard-alert-system-kr1-kr_svchub_prd_cluster?orgId=1',
                'http://10.11.67.29:3000/d/Zx4vgdcVz/coc-k8s-summary-dashboard-alert-system-kr1-kr_svchubcore_prd_cluster?orgId=1',
                'http://10.11.67.29:3000/d/KeocRd5Vz/coc-k8s-summary-dashboard-alert-system-kr1-kr_svchubutil_prd_cluster?orgId=1',
                'http://10.11.67.29:3000/d/Njzv9SZIk/coc-k8s-summary-dashboard-alert-system-krbig-vdsp-prd?orgId=1',
                'http://10.11.67.29:3000/d/Ig7ngd5Vk/coc-k8s-summary-dashboard-alert-system-kr1-kr_vtwin_prd_cluster?orgId=1',
                'http://10.11.67.29:3000/d/8IhZgdcVz/coc-k8s-summary-dashboard-alert-system-kr1-kr_vtwin2_prd_cluster?orgId=1',
                'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/GgRmDQ-4z/kr_apne2_rancher_cluster-prd?orgId=27',
                'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/rBwSwVJVk/ccs_prd_cluster?orgId=27',
            ]
        },
        "EU": {
            "sentence_h1": [
                'h1_first sentence',
                'h1_second sentence',
            ],
            "sentence_h2": [
                'h2_first sentence',
                'h2_second sentence',
            ],
            "sentence_h3": [
                'h3_first sentence',
                'h4_second sentence',
            ]
        }
    }
    
    # 언어에 따른 문장 선택
    if region in sentence_dict:

        sentences = sentence_dict[region]
        sentence_h1 = sentences["sentence_h1"]
        sentence_h2 = sentences["sentence_h2"]
        sentence_h3 = sentences["sentence_h3"]
    
    else:
        print("Unsupported language:", region)
        return


    
    if region == 'KR':
        common_filenames = [
        '%s1_BORDER_NETWORK_*.png',
        '%s2_BORDER_NETWORK_*.png',
        '%s1_F5_LB(KRCLOUD-PRD-L7)_*.png',
        '%s1_A10_LB(KRTMS-PRD-L7)_*.png',
        '%s1_Network_Monitor_*.png',
        '%s2_Network_Monitor_*.png',
        '%s1_OLD_PRD_HOST_*.png',
        '%s1_NEW_PRD_HOST_*.png',
        '%s2_HOST_*.png',
        '%s1_PRD_VM_*.png',
        '%s2_PRD_VM_*.png',
        '%s1_PRD_DB_*.png',
        '%s2_PRD_DB_*.png',
        '%s1_PRD_NETAPP(NVME)_*.png',
        '%s1_OLD&NEW_PRD_BIGDATA_NETAPP_*.png',
        '%s1_STG_NETAPP_*.png',
        '%s1_NETAPP(NVMe01)NPS1_*.png',
        '%s1_NETAPP(NVMe02)NPS1_*.png',
        '%s1_OLDPRD_NETAPP_*.png',
        '%s2_PRD_NETAPP(Cinder)_*.png',
        '%s2_PRD_NETAPP(Manila)_*.png',
        '%s2_STG_NETAPP_*.png',
        '%s2_PRD_FAS_03R02_NETAPP_*.png',
        '%s2_PRD_AFF_03R02_NETAPP_*.png',
        '%s2_PRD_FAS_03R03_NETAPP_*.png',
        '%s2_PRD_AFF_03R03_NETAPP_*.png',
        '%s2_PRD_FAS_03R04_NETAPP_*.png',
        '%s1_Rancher-prd_*.png',
        '%s1_ccskr-devworks-prd_*.png',
        '%s1_ccskr-dkc2hpkr-prd_*.png',
        '%s1_ccskr-dkc2kpgkr-prd_*.png',
        '%s1_ccskr-dkc2kplkr-prd_*.png',
        '%s1_ccskr-svchub-prd_*.png',
        '%s1_ccskr-svchubcore-prd_*.png',
        '%s1_ccskr-svchubutil-prd_*.png',
        '%s1_kr-vdsp-prd_*.png',
        '%s1_ccskr-vtwin-prd_*.png',
        '%s1_ccskr-vtwin2-prd_*.png',
        '%s2_Rancher-prd_*.png',
        '%s2_ccs-prd_*.png'
    ]
        
    elif region == 'EU':
        common_filenames = [
        '%s1_BORDER_NETWORK_*.png',
        '%s2_BORDER_NETWORK_*.png',
     ]

    # 파일 검색
            
    try:
        filelist_delete = []
        
        for filename_pattern in common_filenames:
            filenames = glob.glob(os.path.join('ScreenShots', filename_pattern % region))
            
            if not filenames:  # 파일을 찾지 못한 경우
                print("No image files found for pattern:", filename_pattern )
                return  # 함수 종료
            else:
                filelist_delete.append(filenames[-3])
        
        for filelist in filelist_delete:
            if not filelist:
                continue
            for file in filelist:
                
                try:
                    print("Deleting file:", file)
                    os.remove(file)
                    print("File deleted!!!")
    
                except Exception as e:
                    print("Error deleting file:", file)
                    print(e)

            
    except Exception as e:
                    print(e)
                    print('삭제함수에러')

    filelist_recently = []

    for filename_pattern in common_filenames:
            filenames = glob.glob(os.path.join('ScreenShots', filename_pattern))
            
            if not filenames:  # 파일을 찾지 못한 경우
                print("No image files found for pattern:", filename_pattern)
                return  # 함수 종료
            else:
                filelist_recently.append(filenames[-1])

       

    pdf = PdfFileWriter()

    inch = 72
                    
    for i, file in enumerate(filelist_recently):  # for each slide
                        # Using ReportLab Canvas to insert image into PDF
                  
                        imgTemp = BytesIO()
                        imgDoc = canvas.Canvas(imgTemp, pagesize=(11*inch, 8.5*inch))
                        fontname = 'C:\\Users\\H2207039\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumBarunGothic.ttf'
                        pdfmetrics.registerFont(TTFont("NanumBarunGothic", fontname))

                        # Draw image on Canvas and save PDF in buffer
                        print(file)
                        Words = file.split(".")[0].split("\\")

                        Title = Words[1]
                        imgDoc.setFont('NanumBarunGothic', 14)
                        imgDoc.drawString(20, 580, Title)
                        imgDoc.setFont('NanumBarunGothic', 12)
                        imgDoc.drawString(20, 560, sentence_h1[i])
                        imgDoc.drawString(20, 540, sentence_h2[i])
                        imgDoc.drawString(20, 520, sentence_h3[i])
                        imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                        # x, y - start position
                        # in my case -25, -45 needed
                        imgDoc.save()
                        # Use PyPDF to merge the image-PDF into the template
                        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
                    
    print("pdf create")
    filename = 'Infra_in_detail' + datetime.now().strftime('%Y%m%d_%H%M') + '.pdf'
    filename = os.path.join(pdf_path, filename)
    pdf.write(open(filename,"wb"))

        

    
    print("리포트저장에러")




# if __name__ == '__main__':

#     # fonts = [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]
#     # print(fonts)
    
#     filename = 'Infra_in_detail_' + datetime.now().strftime('%Y%m%d-%H%M') + '.pdf'

#     gen_pdf(filename)