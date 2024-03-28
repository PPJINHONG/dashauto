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

def gen_infra_pdf(region):
   
        if region == "KR":
            Created = False
            Sentences_KR_1 = [
                #'CCS서비스 API 호출',
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
                # '',
                # '',
                # '',
                # '',
                # '',
                # '',
                # 'IaaS포탈 SLA정의: 1분 간격의 로그인 접속시도 집계. 100% 항상유지 필수/ Total Error값 증가 시 키클락 서비스 확인필요',
                # 'IaaS포탈 아키텍처 구성 인스턴스 별 CPU/메모리/디스크 목록으로 사용율 80% 초과 시 해당 서비스 재기동 필요.',
                # 'IaaS포탈 전체 인스턴스 다이어그램으로 서비스 Up/Down 체크. 다이어그램 부분 빨간색으로 변동시 서비스 장애로 확인 필요',
            ]
            Sentences_KR_2 = [
                #'',
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
                # '',
                # '',
                # '',
                # '',
                # '',
                # '',
                # '',
                # '',
                # '',
            ]
            Sentences_KR_3 = [
                #'https://ccsdev-dummy-aws.live/d/8Wa4pnYVk/kr-ccs-dummy-client?orgId=1&refresh=10s',
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
                # 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/rSN9C414k/ccskr2-svchub_cluster?orgId=27',
                # 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/R79d6V1Vz/content2_fcs?orgId=27',
                # 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/BC7Fy314z/contents2-wts?orgId=27',
                # 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/lGbf6VJVk/ccs_epg_cluster?orgId=27',
                # 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/7gY_RSJVz/podbbang_cluster?orgId=27',
                # 'https://hubble-apne2-prd.platform.hcloud.io/grafana/d/k9v6s21Vk/ccs2_hcloud?orgId=27',
                # 'http://172.16.17.74:3000/d/DuMWqtPnk/sla-dashboard?orgId=1&refresh=15m',
                # 'http://172.16.17.74:3000/d/ASnb3Sb7k/dashboard-1?orgId=1&refresh=10s',
                # 'http://172.16.17.74:3000/d/4LbjUmf7z/iaas-dashboard-4?orgId=1&refresh=10s',
            ]            
            while not Created:
                try:
                    #파일 삭제 (최근 것 제외)
                    #filename_dummy_client = glob.glob(os.path.join('ScreenShots', 'DUMMY_CLIENT_%s_PRD_*.png'% (region)))[:-3]
                    
                    # filename_network = glob.glob(os.path.join('ScreenShots', '%s1_BORDER_NETWORK_*.png'% (region)))[:-3]
                    # filename_network_2 = glob.glob(os.path.join('ScreenShots', '%s2_BORDER_NETWORK_*.png'% (region)))[:-3]
                    # filename_lb_a10 = glob.glob(os.path.join('ScreenShots', '%s1_A10_LB(KRTMS-PRD-L7)_*.png'% (region)))[:-3]
                    # filename_lb_f5 = glob.glob(os.path.join('ScreenShots', '%s1_F5_LB(KRCLOUD-PRD-L7)_*.png'% (region)))[:-3]
                    # filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s1_Network_Monitor_*.png'% (region)))[:-3]
                    # filename_total_2 = glob.glob(os.path.join('ScreenShots', '%s2_Network_Monitor_*.png'% (region)))[:-3]
                    # filename_host_1 = glob.glob(os.path.join('ScreenShots', '%s1_OLD_PRD_HOST_*.png'% (region)))[:-3]
                    # filename_host_1_new = glob.glob(os.path.join('ScreenShots', '%s1_NEW_PRD_HOST_*.png'% (region)))[:-3]
                    # filename_vm_1 = glob.glob(os.path.join('ScreenShots', '%s2_HOST_*.png'% (region)))[:-3]
                    # filename_host_2 = glob.glob(os.path.join('ScreenShots', '%s1_PRD_VM_*.png'% (region)))[:-3]
                    # filename_vm_2 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_VM_*.png'% (region)))[:-3]
                    # filename_database_1 = glob.glob(os.path.join('ScreenShots', '%s1_PRD_DB_*.png'% (region)))[:-3]
                    # filename_database_2 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_DB_*.png'% (region)))[:-3]
                    # filename_netapp_nvme = glob.glob(os.path.join('ScreenShots', '%s1_PRD_NETAPP(NVME)_*.png'% (region)))[:-3]
                    # filename_netapp_old_new_prd_bigdata = glob.glob(os.path.join('ScreenShots', '%s1_OLD&NEW_PRD_BIGDATA_NETAPP_*.png'% (region)))[:-3]
                    # filename_netapp_stg = glob.glob(os.path.join('ScreenShots', '%s1_STG_NETAPP_*.png'% (region)))[:-3]
                    # filename_storage_new_1 = glob.glob(os.path.join('ScreenShots', '%s1_NETAPP(NVMe01)NPS1_*.png'% (region)))[:-3]
                    # filename_storage_new_2 = glob.glob(os.path.join('ScreenShots', '%s1_NETAPP(NVMe02)NPS1_*.png'% (region)))[:-3]
                    # filename_storage_old_1 = glob.glob(os.path.join('ScreenShots', '%s1_OLDPRD_NETAPP_*.png'% (region)))[:-3]
                    # filename_netapp_prd_2center = glob.glob(os.path.join('ScreenShots', '%s2_PRD_NETAPP(Cinder)_*.png'% (region)))[:-3]
                    # filename_netapp_manila_prd_2center = glob.glob(os.path.join('ScreenShots', '%s2_PRD_NETAPP(Manila)_*.png'% (region)))[:-3]
                    # filename_netapp_stg_2center = glob.glob(os.path.join('ScreenShots', '%s2_STG_NETAPP_*.png'% (region)))[:-3]
                    # filename_storage_2center_fas_03r02 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_FAS_03R02_NETAPP_*.png'% (region)))[:-3]
                    # filename_storage_2center_aff_03r02 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_AFF_03R02_NETAPP_*.png'% (region)))[:-3]
                    # filename_storage_2center_fas_03r03 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_FAS_03R03_NETAPP_*.png'% (region)))[:-3]
                    # filename_storage_2center_aff_03r03 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_AFF_03R03_NETAPP_*.png'% (region)))[:-3]
                    # filename_storage_2center_fas_03r04 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_FAS_03R04_NETAPP_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_rancher_prd = glob.glob(os.path.join('ScreenShots', '%s1_Rancher-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_devworks_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-devworks-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_dkc2hpkr_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-dkc2hpkr-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_dkc2kpgkr_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-dkc2kpgkr-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_dkc2kplkr_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-dkc2kplkr-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_svchub_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-svchub-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_svchubcore_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-svchubcore-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_svchubutil_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-svchubutil-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_kr_vdsp_prd = glob.glob(os.path.join('ScreenShots', '%s1_kr-vdsp-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_vtwin_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-vtwin-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_1center_ccskr_vtwin2_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-vtwin2-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_2center_ccskr2_rancher_prd = glob.glob(os.path.join('ScreenShots', '%s2_Rancher-prd_*.png'% (region)))[:-3]
                    # filename_k8s_cluster_2center_ccs_prd = glob.glob(os.path.join('ScreenShots', '%s2_ccs-prd_*.png'% (region)))[:-3]
                    # # filename_k8s_cluster_2center_ccskr2_svchub_prd = glob.glob(os.path.join('ScreenShots', '%s2_svchub-prd_*.png'% (region)))[:-3]
                    # # filename_k8s_cluster_2center_contents2_fcs = glob.glob(os.path.join('ScreenShots', '%s2_contents2-fcs-prd_*.png'% (region)))[:-3]
                    # # filename_k8s_cluster_2center_contents2_wts = glob.glob(os.path.join('ScreenShots', '%s2_contents2-wts-prd_*.png'% (region)))[:-3]
                    # # filename_k8s_cluster_2center_epgprd = glob.glob(os.path.join('ScreenShots', '%s2_epgprd_*.png'% (region)))[:-3]
                    # # filename_k8s_cluster_2center_podbbang_prd = glob.glob(os.path.join('ScreenShots', '%s2_podbbang-prd_*.png'% (region)))[:-3]
                    # # filename_k8s_cluster_2center_Hcloud = glob.glob(os.path.join('ScreenShots', '%s2_CCS_Hcloud_*.png'% (region)))[:-3]


                    # # filename_IaaS_SLA = glob.glob(os.path.join('ScreenShots', '%s2_IaaS_SLA_*.png'% (region)))[:-3]
                    # # filename_IaaS_Resource = glob.glob(os.path.join('ScreenShots', '%s2_IaaS_Resource_*.png'% (region)))[:-3]
                    # # filename_IaaS_Summary = glob.glob(os.path.join('ScreenShots', '%s2_IaaS_Summary_*.png'% (region)))[:-3]


                    # filelist_delete = [
                    #     #filename_dummy_client,
                    #     filename_network,
                    #     filename_network_2,
                    #     filename_lb_a10,
                    #     filename_lb_f5,
                    #     filename_total_1,
                    #     filename_total_2,
                    #     filename_host_1,
                    #     filename_host_1_new,
                    #     filename_vm_1,
                    #     filename_host_2,
                    #     filename_vm_2,
                    #     filename_database_1,
                    #     filename_database_2,
                    #     filename_netapp_nvme,
                    #     filename_netapp_old_new_prd_bigdata,
                    #     filename_netapp_stg,
                    #     filename_storage_new_1,
                    #     filename_storage_new_2,
                    #     filename_storage_old_1,
                    #     filename_netapp_prd_2center,
                    #     filename_netapp_manila_prd_2center,
                    #     filename_netapp_stg_2center,
                    #     filename_storage_2center_fas_03r02,
                    #     filename_storage_2center_aff_03r02,
                    #     filename_storage_2center_fas_03r03,
                    #     filename_storage_2center_aff_03r03,
                    #     filename_storage_2center_fas_03r04,
                    #     filename_k8s_cluster_1center_ccskr_rancher_prd,
                    #     filename_k8s_cluster_1center_ccskr_devworks_prd,
                    #     filename_k8s_cluster_1center_ccskr_dkc2hpkr_prd,
                    #     filename_k8s_cluster_1center_ccskr_dkc2kpgkr_prd,
                    #     filename_k8s_cluster_1center_ccskr_dkc2kplkr_prd,
                    #     filename_k8s_cluster_1center_ccskr_svchub_prd,
                    #     filename_k8s_cluster_1center_ccskr_svchubcore_prd,
                    #     filename_k8s_cluster_1center_ccskr_svchubutil_prd,
                    #     filename_k8s_cluster_1center_kr_vdsp_prd,
                    #     filename_k8s_cluster_1center_ccskr_vtwin_prd,
                    #     filename_k8s_cluster_1center_ccskr_vtwin2_prd,
                    #     filename_k8s_cluster_2center_ccskr2_rancher_prd,
                    #     filename_k8s_cluster_2center_ccs_prd,
                    #     # filename_k8s_cluster_2center_ccskr2_svchub_prd,
                    #     # filename_k8s_cluster_2center_contents2_fcs,
                    #     # filename_k8s_cluster_2center_contents2_wts,
                    #     # filename_k8s_cluster_2center_epgprd,
                    #     # filename_k8s_cluster_2center_podbbang_prd,
                    #     # filename_k8s_cluster_2center_Hcloud,
                       
                    #     # filename_IaaS_SLA,
                    #     # filename_IaaS_Resource,
                    #     # filename_IaaS_Summary,
                    # ]
                    # for files in filelist_delete:
                    #     for file in files:
                    #         print(file)
                    #         os.remove(file)
                    #         print("file deleted")
                    
                # except Exception as e:
                #     print(e)
                #     print("삭제안됨")
                #     sleep(10)
                #     pass            

                # try:
                    # 파일 목록 (최근 것만)
                   # filename_dummy_client = glob.glob(os.path.join('ScreenShots', 'DUMMY_CLIENT_%s_PRD_*.png'% (region)))[-1]
                    filename_network = glob.glob(os.path.join('ScreenShots', '%s1_BORDER_NETWORK_*.png'% (region)))[-1]
                    filename_network_2 = glob.glob(os.path.join('ScreenShots', '%s2_BORDER_NETWORK_*.png'% (region)))[-1]
                    filename_lb_f5 = glob.glob(os.path.join('ScreenShots', '%s1_F5_LB(KRCLOUD-PRD-L7)_*.png'% (region)))[-1]
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', '%s1_A10_LB(KRTMS-PRD-L7)_*.png'% (region)))[-1]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s1_Network_Monitor_*.png'% (region)))[-1]
                    filename_total_2 = glob.glob(os.path.join('ScreenShots', '%s2_Network_Monitor_*.png'% (region)))[-1]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', '%s1_OLD_PRD_HOST_*.png'% (region)))[-1]
                    filename_host_1_new = glob.glob(os.path.join('ScreenShots', '%s1_NEW_PRD_HOST_*.png'% (region)))[-1]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', '%s2_HOST_*.png'% (region)))[-1]
                    filename_host_2 = glob.glob(os.path.join('ScreenShots', '%s1_PRD_VM_*.png'% (region)))[-1]
                    filename_vm_2 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_VM_*.png'% (region)))[-1]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', '%s1_PRD_DB_*.png'% (region)))[-1]
                    filename_database_2 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_DB_*.png'% (region)))[-1]
                    filename_netapp_nvme = glob.glob(os.path.join('ScreenShots', '%s1_PRD_NETAPP(NVME)_*.png'% (region)))[-1]
                    filename_netapp_old_new_prd_bigdata = glob.glob(os.path.join('ScreenShots', '%s1_OLD&NEW_PRD_BIGDATA_NETAPP_*.png'% (region)))[-1]
                    filename_netapp_stg = glob.glob(os.path.join('ScreenShots', '%s1_STG_NETAPP_*.png'% (region)))[-1]
                    filename_storage_new_1 = glob.glob(os.path.join('ScreenShots', '%s1_NETAPP(NVMe01)NPS1_*.png'% (region)))[-1]
                    filename_storage_new_2 = glob.glob(os.path.join('ScreenShots', '%s1_NETAPP(NVMe02)NPS1_*.png'% (region)))[-1]
                    filename_storage_old_1 = glob.glob(os.path.join('ScreenShots', '%s1_OLDPRD_NETAPP_*.png'% (region)))[-1]
                    filename_netapp_prd_2center = glob.glob(os.path.join('ScreenShots', '%s2_PRD_NETAPP(Cinder)_*.png'% (region)))[-1]
                    filename_netapp_manila_prd_2center = glob.glob(os.path.join('ScreenShots', '%s2_PRD_NETAPP(Manila)_*.png'% (region)))[-1]
                    filename_netapp_stg_2center = glob.glob(os.path.join('ScreenShots', '%s2_STG_NETAPP_*.png'% (region)))[-1]
                    filename_storage_2center_fas_03r02 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_FAS_03R02_NETAPP_*.png'% (region)))[-1]
                    filename_storage_2center_aff_03r02 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_AFF_03R02_NETAPP_*.png'% (region)))[-1]
                    filename_storage_2center_fas_03r03 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_FAS_03R03_NETAPP_*.png'% (region)))[-1]
                    filename_storage_2center_aff_03r03 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_AFF_03R03_NETAPP_*.png'% (region)))[-1]
                    filename_storage_2center_fas_03r04 = glob.glob(os.path.join('ScreenShots', '%s2_PRD_FAS_03R04_NETAPP_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_rancher_prd = glob.glob(os.path.join('ScreenShots', '%s1_Rancher-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_devworks_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-devworks-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_dkc2hpkr_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-dkc2hpkr-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_dkc2kpgkr_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-dkc2kpgkr-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_dkc2kplkr_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-dkc2kplkr-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_svchub_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-svchub-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_svchubcore_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-svchubcore-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_svchubutil_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-svchubutil-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_kr_vdsp_prd = glob.glob(os.path.join('ScreenShots', '%s1_kr-vdsp-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_vtwin_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-vtwin-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_1center_ccskr_vtwin2_prd = glob.glob(os.path.join('ScreenShots', '%s1_ccskr-vtwin2-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_2center_ccskr2_rancher_prd = glob.glob(os.path.join('ScreenShots', '%s2_Rancher-prd_*.png'% (region)))[-1]
                    filename_k8s_cluster_2center_ccs_prd = glob.glob(os.path.join('ScreenShots', '%s2_ccs-prd_*.png'% (region)))[-1]

                    #filename_k8s_cluster_2center_ccskr2_svchub_prd = glob.glob(os.path.join('ScreenShots', '%s2_svchub-prd_*.png'% (region)))[-1]
                    #filename_k8s_cluster_2center_contents2_fcs = glob.glob(os.path.join('ScreenShots', '%s2_contents2-fcs-prd_*.png'% (region)))[-1]
                    #filename_k8s_cluster_2center_contents2_wts = glob.glob(os.path.join('ScreenShots', '%s2_contents2-wts-prd_*.png'% (region)))[-1]
                    #filename_k8s_cluster_2center_epgprd = glob.glob(os.path.join('ScreenShots', '%s2_epgprd_*.png'% (region)))[-1]
                    #filename_k8s_cluster_2center_podbbang_prd = glob.glob(os.path.join('ScreenShots', '%s2_podbbang-prd_*.png'% (region)))[-1]
                    #filename_k8s_cluster_2center_Hcloud = glob.glob(os.path.join('ScreenShots', '%s2_CCS_Hcloud_*.png'% (region)))[-1]
                    #filename_IaaS_SLA = glob.glob(os.path.join('ScreenShots', '%s2_IaaS_SLA_*.png'% (region)))[-1]
                    #filename_IaaS_Resource = glob.glob(os.path.join('ScreenShots', '%s2_IaaS_Resource_*.png'% (region)))[-1]
                    #filename_IaaS_Summary = glob.glob(os.path.join('ScreenShots', '%s2_IaaS_Summary_*.png'% (region)))[-1]

                    filelist = [
                      # filename_dummy_client,
                        filename_network,
                        filename_network_2,
                        filename_lb_a10,
                        filename_lb_f5,
                        filename_total_1,
                        filename_total_2,
                        filename_host_1,
                        filename_host_1_new,
                        filename_vm_1,
                        filename_host_2,
                        filename_vm_2,
                        filename_database_1,
                        filename_database_2,
                        filename_netapp_nvme,
                        filename_netapp_old_new_prd_bigdata,
                        filename_netapp_stg,
                        filename_storage_new_1,
                        filename_storage_new_2,
                        filename_storage_old_1,
                        filename_netapp_prd_2center,
                        filename_netapp_manila_prd_2center,
                        filename_netapp_stg_2center,
                        filename_storage_2center_fas_03r02,
                        filename_storage_2center_aff_03r02,
                        filename_storage_2center_fas_03r03,
                        filename_storage_2center_aff_03r03,
                        filename_storage_2center_fas_03r04,
                        filename_k8s_cluster_1center_ccskr_rancher_prd,
                        filename_k8s_cluster_1center_ccskr_devworks_prd,
                        filename_k8s_cluster_1center_ccskr_dkc2hpkr_prd,
                        filename_k8s_cluster_1center_ccskr_dkc2kpgkr_prd,
                        filename_k8s_cluster_1center_ccskr_dkc2kplkr_prd,
                        filename_k8s_cluster_1center_ccskr_svchub_prd,
                        filename_k8s_cluster_1center_ccskr_svchubcore_prd,
                        filename_k8s_cluster_1center_ccskr_svchubutil_prd,
                        filename_k8s_cluster_1center_kr_vdsp_prd,
                        filename_k8s_cluster_1center_ccskr_vtwin_prd,
                        filename_k8s_cluster_1center_ccskr_vtwin2_prd,
                        filename_k8s_cluster_2center_ccskr2_rancher_prd,
                        filename_k8s_cluster_2center_ccs_prd,

                        # filename_k8s_cluster_2center_ccskr2_svchub_prd,
                        # filename_k8s_cluster_2center_contents2_fcs,
                        # filename_k8s_cluster_2center_contents2_wts,
                        # filename_k8s_cluster_2center_epgprd,
                        # filename_k8s_cluster_2center_podbbang_prd,
                        # filename_k8s_cluster_2center_Hcloud,
                        # filename_IaaS_SLA,
                        # filename_IaaS_Resource,
                        # filename_IaaS_Summary,
                    ]
                # except Exception as e:
                #     print(e)
                #     sleep(60)
                #     pass   
                    pdf = PdfFileWriter()

                    inch = 72
                    
                    for i, file in enumerate(filelist):  # for each slide
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
                        imgDoc.drawString(20, 560, Sentences_KR_1[i])
                        imgDoc.drawString(20, 540, Sentences_KR_2[i])
                        imgDoc.drawString(20, 520, Sentences_KR_3[i])
                        imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                        # x, y - start position
                        # in my case -25, -45 needed
                        imgDoc.save()
                        # Use PyPDF to merge the image-PDF into the template
                        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
                    
                    print("pdf create")
                    filename = 'Infra_in_detail_%s_'%(region) + datetime.now().strftime('%Y%m%d_%H%M') + '.pdf'
                    filename = os.path.join(pdf_path, filename)
                    pdf.write(open(filename,"wb"))
            

                    Created = True

                except Exception as e:
                    print(e)
                    print('위에 수정')
                    sleep(5) #변경60
                   
                    pass

        elif region == "RU" :
            Created = False
            Sentences_RU_1 = [
                '',
                '',
                '',
                'BM(Bare Metal): CCS내 모든 물리서버 대상 Worst Top 10 정보. Red가 아니면 모두 정상',
                'VM: CCS내 모든 가상서버 대상 Worst Top 10  정보.',
                'RU DB : RU PRD DB 정보 (CPU, Memory, session)',
                'Storage: 운영계 스토리지 클러스터 의 IOPS, Throughput 정보',
                '',
                
            ]


            Sentences_RU_2 = [
                '',    
                '',
                '',
                '(Red 기준 : CPU 10% 이하, 메모리 1G이하, free Disk 10% 이하)',
                '(Red 기준 : CPU 10% 이하, 메모리 500M이하, free Disk 10% 이하)',
                '',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '',
                
  
            ]

            Sentences_RU_3 = [
                'http://10.11.67.29:3000/d/MYEQGw5Vk/rutms-a10-resource-monitor?orgId=1',
                'http://10.11.67.29:3000/d/HK5wzuFVkasdf/rutms-fw_resource-monitor?orgId=1',
                'http://10.11.67.29:3000/d/-FwPmOcVz/ru-prd-ccs-neteuweokeu-jonghab-moniteoring?orgId=1&refresh=1h',
                'http://10.11.67.29:3000/d/rDJA39K4z/ru-bm-and-netapp-resource?orgId=1',
                'http://10.11.67.29:3000/d/HEd3C9FVk/ru-vm-resource?orgId=1',
                'http://10.11.67.29:3000/d/3MMHzXKVz/ru-prd-db-resource-usage-top-20?orgId=1',
                'https://10.7.0.231/clusters/70559/explorer',
                'http://10.11.67.29:3000/d/Rv-oDy54k/ru-netapp-dash-board?orgId=1',
                
            ]            
            while not Created:
                try:
                    #파일 삭제 (최근 것 제외)
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', 'LB(A10)_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[:-3]

                    filelist_delete = [
                        filename_lb_a10,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_storage_1,
                        filename_netapp_info,

                    ]

                    for files in filelist_delete:
                        for file in files:
                            print(file)
                            os.remove(file)
                    print("file deleted")



                    # 파일 목록 (최근 것만)
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', 'LB(A10)_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[-1]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[-1]


                    filelist = [
                        filename_lb_a10,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_storage_1,
                        filename_netapp_info,

                    ]
                    
                    pdf = PdfFileWriter()

                    inch = 72
                
                    for i, file in enumerate(filelist):  # for each slide
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
                        imgDoc.drawString(20, 560, Sentences_RU_1[i])
                        imgDoc.drawString(20, 540, Sentences_RU_2[i])
                        imgDoc.drawString(20, 520, Sentences_RU_3[i])
                        imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                        # x, y - start position
                        # in my case -25, -45 needed
                        imgDoc.save()
                        # Use PyPDF to merge the image-PDF into the template
                        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
                    
                    print("pdf create")
                    filename = 'Infra_in_detail_%s_'%(region) + datetime.now().strftime('%Y%m%d_%H%M') + '.pdf'
                    filename = os.path.join(pdf_path, filename)
                    pdf.write(open(filename,"wb"))
            

                    Created = True

                except Exception as e:
                    print(e)
                    sleep(60)
                    pass
            print()
        elif region == "EU" :
            Created = False
            Sentences_EU_1 = [
                '',
                '',
                '',
                'BM(Bare Metal): CCS내 모든 물리서버 대상 Worst Top 10 정보. Red가 아니면 모두 정상',
                'VM: CCS EU 내 모든 가상서버 대상 Worst Top 10  정보.',
                'EU DB : EU PRD DB 정보 (CPU, Memory, session)',
                '',
                'Storage: 운영계 스토리지 클러스터 의 IOPS, Throughput 정보',
                '',
                '',
                '',
                '',
                '',
                # '',                                                                                                
            ]


            Sentences_EU_2 = [
                '',
                '',
                '',
                '(Red 기준 : CPU 10% 이하, 메모리 300M이하, free Disk 10% 이하)',
                '(Red 기준 : CPU 10% 이하, 메모리 500M이하, free Disk 10% 이하) ',
                '',
                '',
                '',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '',
                '',
                '',
                '',
                # '',                                                                                
            ]

            Sentences_EU_3 = [
                'http://10.11.67.29:3000/d/BfKKMwcVz/eutms-a10-resource-monitor?orgId=1&refresh=5m',
                'http://10.11.67.29:3000/d/HK5wzuFVk2/eutms-fw_resource-monitor?orgId=1&refresh=5m',
                'http://10.11.67.29:3000/d/MtWXiuFVz/eu-prd-ccs-neteuweokeu-jonghab-moniteoring?orgId=1',
                'http://10.11.67.29:3000/d/ZdXDq9F4k/eu-bm-and-netapp-resource?orgId=1',
                'http://10.11.67.29:3000/d/_us9CrK4z/eu-vm-resource?orgId=1',
                'http://10.11.67.29:3000/d/t4xORuFVz/eu-prd-db-resource-usage-top-20?orgId=1',
                'http://10.11.67.29:3000/d/y0-T77cVk/eu_mongodb?orgId=1',
                'http://10.11.67.29:3000/d/bhPMpo54k/eu-netapp-dash-board',
                'https://10.7.0.231/clusters/69010/explorer',
                'http://10.11.67.29:3000/d/k4uJRdc4z/coc-k8s-summary-dashboard-alert-system-eu-1?orgId=1',
                'http://10.11.67.29:3000/d/BBEbgOc4k/coc-k8s-summary-dashboard-alert-system-eu-2?orgId=1',
                'http://10.11.67.29:3000/d/6yD-Rdc4k/coc-k8s-summary-dashboard-alert-system-eu-3?orgId=1',
                'http://10.11.67.29:3000/d/niGBgO5Vz/coc-k8s-summary-dashboard-alert-system-eu-4?orgId=1',
                # '',
                # '',                                                                
            ]            
            while not Created:
                try:
                    #파일 삭제 (최근 것 제외)
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', 'LB(A10)_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_mongo = glob.glob(os.path.join('ScreenShots', 'mongo_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_1 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_1_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_2 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_2_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_3 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_3_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_4 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_4_1center_PRD_*.png'%(region)))[:-3]
                    # filename_zabbix_dash = glob.glob(os.path.join('ScreenShots', 'zabbix_%s_1center_PRD_*.png'%(region)))[:-3]

                    filelist_delete = [
                        filename_lb_a10,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_mongo,
                        filename_netapp_info,
                        filename_storage_1,
                        filename_cluster_info_1,
                        filename_cluster_info_2,
                        filename_cluster_info_3,
                        filename_cluster_info_4,
                        # filename_zabbix_dash,
                    ]

                    for files in filelist_delete:
                        for file in files:
                            print(file)
                            os.remove(file)
                    print("file deleted")


                    # 스크린샷 캡처
                    # 파일 목록 (최근 것만)
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', 'LB(A10)_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[-1]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_mongo = glob.glob(os.path.join('ScreenShots', 'mongo_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_1 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_1_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_2 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_2_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_3 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_3_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_4 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_4_1center_PRD_*.png'%(region)))[-1]
                    # filename_zabbix_dash = glob.glob(os.path.join('ScreenShots', 'zabbix_%s_1center_PRD_*.png'%(region)))[-1]

                    filelist = [
                        filename_lb_a10,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_mongo,
                        filename_netapp_info,
                        filename_storage_1,
                        filename_cluster_info_1,
                        filename_cluster_info_2,
                        filename_cluster_info_3,
                        filename_cluster_info_4,
                        # filename_zabbix_dash,
                    ]
                    
                    pdf = PdfFileWriter()

                    inch = 72
                
                    for i, file in enumerate(filelist):  # for each slide
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
                        imgDoc.drawString(20, 560, Sentences_EU_1[i])
                        imgDoc.drawString(20, 540, Sentences_EU_2[i])
                        imgDoc.drawString(20, 520, Sentences_EU_3[i])
                        imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                        # x, y - start position
                        # in my case -25, -45 needed
                        imgDoc.save()
                        # Use PyPDF to merge the image-PDF into the template
                        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
                    
                    print("pdf create")
                    filename = 'Infra_in_detail_%s_'%(region) + datetime.now().strftime('%Y%m%d_%H%M') + '.pdf'
                    filename = os.path.join(pdf_path, filename)
                    pdf.write(open(filename,"wb"))
            

                    Created = True

                except Exception as e:
                    print(e)
                    sleep(60)
                    pass
            print()
        elif region == "SG" :
            Created = False
            Sentences_SG_1 = [
                '',
                '',
                '',
                'BM(Bare Metal): CCS SG 내 모든 물리서버 대상 Worst Top 10 정보. Red가 아니면 모두 정상',
                'VM: CCS SG 내 모든 가상서버 대상 Worst Top 10  정보.',
                'SG DB : SG PRD DB 정보 (CPU, Memory, session)',
                '',
                'Storage: 운영계 스토리지 클러스터 의 IOPS, Throughput 정보',
                'Storage: 운영계 스토리지 클러스터 의 IOPS, Throughput 정보',
                '',
                '',
                '',
                '',
                '',
                '',
                # 'IaaS포탈 SLA정의: 1분 간격의 로그인 접속시도 집계. 100% 항상유지 필수/ Total Error값 증가 시 키클락 서비스 확인필요.',
                # 'IaaS포탈 아키텍처 구성 인스턴스 별 CPU/메모리/디스크 목록으로 사용율 80% 초과 시 해당 서비스 재기동 필요.',
                # 'IaaS포탈 전체 인스턴스 다이어그램으로 서비스 Up/Down 체크. 다이어그램 부분 빨간색으로 변동시  서비스 장애로 확인 필요',
                
            ]


            Sentences_SG_2 = [
                '',
                '',
                '',
                '(Red 기준 : CPU 10% 이하, 메모리 3G이하, free Disk 10% 이하)',
                '(Red 기준 : CPU 10% 이하, 메모리 370M이하, free Disk 10% 이하)',
                '',
                '',
                '',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '',
                '',
                '',
                '',
                '',
                # '',
                # '',
                # '',
  
            ]

            Sentences_SG_3 = [
                'http://10.11.67.29:3000/d/sjElzXFVk/sg_f5_monitor?orgId=1',
                'http://10.11.67.29:3000/d/0kQdZuFVk/sg-fw-monitor?orgId=1',
                'http://10.11.67.29:3000/d/qstVWXF4z/sg-prd-ccs-neteuweokeu-jonghab-moniteoring?orgId=1',
                'http://10.11.67.29:3000/d/dPViDjKVk/sg-bm-and-netapp-resource?orgId=1',
                'http://10.11.67.29:3000/d/5bY3CrK4z/sg-vm-resource?orgId=1',
                'http://10.11.67.29:3000/d/RJrKguFVz/sg-prd-db-resource-usage-top-20?orgId=1',
                'http://10.11.67.29:3000/d/sWpQ77c4k/sg_mongodb?orgId=1',
                'http://10.11.67.29:3000/d/Bh1NWuF4k/sg-netapp-dash-board?orgId=1',
                'https://10.107.48.110/sysmgr/v4/',
                'https://10.107.48.130/sysmgr/v4/',
                'http://10.11.67.29:3000/d/s-HlRO5Vk/coc-k8s-summary-dashboard-alert-system-1',
                'http://10.11.67.29:3000/d/6bgugO5Vk/coc-k8s-summary-dashboard-alert-system-2?orgId=1',
                'http://10.11.67.29:3000/d/26t9gdcVz/coc-k8s-summary-dashboard-alert-system-3?orgId=1',
                'http://10.11.67.29:3000/d/1R13gO54k/coc-k8s-summary-dashboard-alert-system-4?orgId=1',
                'http://10.11.67.29:3000/d/bxw6gOc4z/coc-k8s-summary-dashboard-alert-system-5?orgId=1',
                # 'http://172.16.17.74:3000/d/DuMWqtPnk/sla-dashboard?orgId=1&refresh=15m',
                # 'http://172.16.17.74:3000/d/ASnb3Sb7k/dashboard-1?orgId=1&refresh=10s',
                # 'http://172.16.17.74:3000/d/4LbjUmf7z/iaas-dashboard-4?orgId=1&refresh=10s',
            ]            
            while not Created:
                try:
                    #파일 삭제 (최근 것 제외)
                    filename_lb_f5 = glob.glob(os.path.join('ScreenShots', 'LB(F5)_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_mongo = glob.glob(os.path.join('ScreenShots', 'mongo_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_storage_2 = glob.glob(os.path.join('ScreenShots', 'NPS2_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_1 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_1_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_2 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_2_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_3 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_3_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_4 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_4_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_5 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_5_1center_PRD_*.png'%(region)))[:-3]
                    filename_IaaS_SLA = glob.glob(os.path.join('ScreenShots', 'IaaS_SLA_%s_1center_*.png'%(region)))[:-3]
                    filename_IaaS_Resource = glob.glob(os.path.join('ScreenShots', 'IaaS_Resource_%s_1center_*.png'%(region)))[:-3]
                    filename_IaaS_Summary = glob.glob(os.path.join('ScreenShots', 'IaaS_Summary_%s_1center_*.png'%(region)))[:-3]

                    filelist_delete = [
                        filename_lb_f5,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_mongo,
                        filename_netapp_info,
                        filename_storage_1,
                        filename_storage_2,
                        filename_cluster_info_1,
                        filename_cluster_info_2,
                        filename_cluster_info_3,
                        filename_cluster_info_4,
                        filename_cluster_info_5,
                        filename_IaaS_SLA,
                        filename_IaaS_Resource,
                        filename_IaaS_Summary,                       
                    ]

                    for files in filelist_delete:
                        for file in files:
                            print(file)
                            os.remove(file)
                    print("file deleted")



                    # 파일 목록 (최근 것만)
                    # filename_border_network = glob.glob(os.path.join('ScreenShots', 'BORDER_NETWORK_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_lb_f5 = glob.glob(os.path.join('ScreenShots', 'LB(F5)_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[-1]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_mongo = glob.glob(os.path.join('ScreenShots', 'mongo_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_storage_2 = glob.glob(os.path.join('ScreenShots', 'NPS2_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_1 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_1_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_2 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_2_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_3 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_3_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_4 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_4_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_5 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_5_1center_PRD_*.png'%(region)))[-1]
                    # filename_IaaS_SLA = glob.glob(os.path.join('ScreenShots', 'IaaS_SLA_%s_1center_*.png'%(region)))[-1]
                    # filename_IaaS_Resource = glob.glob(os.path.join('ScreenShots', 'IaaS_Resource_%s_1center_*.png'%(region)))[-1]
                    # filename_IaaS_Summary = glob.glob(os.path.join('ScreenShots', 'IaaS_Summary_%s_1center_*.png'%(region)))[-1]

                    filelist = [
                        filename_lb_f5,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_mongo,
                        filename_netapp_info,
                        filename_storage_1,
                        filename_storage_2,
                        filename_cluster_info_1,
                        filename_cluster_info_2,
                        filename_cluster_info_3,
                        filename_cluster_info_4,
                        filename_cluster_info_5,
                        # filename_IaaS_SLA,
                        # filename_IaaS_Resource,
                        # filename_IaaS_Summary,
                    ]
                    
                    pdf = PdfFileWriter()

                    inch = 72
                
                    for i, file in enumerate(filelist):  # for each slide
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
                        imgDoc.drawString(20, 560, Sentences_SG_1[i])
                        imgDoc.drawString(20, 540, Sentences_SG_2[i])
                        imgDoc.drawString(20, 520, Sentences_SG_3[i])
                        imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                        # x, y - start position
                        # in my case -25, -45 needed
                        imgDoc.save()
                        # Use PyPDF to merge the image-PDF into the template
                        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
                    
                    print("pdf create")
                    filename = 'Infra_in_detail_%s_'%(region) + datetime.now().strftime('%Y%m%d_%H%M') + '.pdf'
                    filename = os.path.join(pdf_path, filename)
                    pdf.write(open(filename,"wb"))
            

                    Created = True

                except Exception as e:
                    print(e)
                    print('삭제오류')
                    sleep(60)
                    pass

            print('삭제함수 종료')
            print()
        
        elif region == "LA47" :
            Created = False
            Sentences_NA_1 = [
                'Gen2 Monitoring - Infra Cutover',
                'Gen2 Monitoring - Infra Load Balancer',
                'LA4 and LA7 MOF',
                'L4 & L7 and app process Monitoring',
                'L4 VPX monitor',
                'L7 VPX Monitor',

            ]           
            while not Created:
                try:
                    #파일 삭제 (최근 것 제외)
                    filename_na_01 = glob.glob(os.path.join('ScreenShots', 'na_01_%s_*.png'%(region)))[:-3]
                    filename_na_02 = glob.glob(os.path.join('ScreenShots', 'na_02_%s_*.png'%(region)))[:-3]
                    filename_na_03 = glob.glob(os.path.join('ScreenShots', 'na_03_%s_*.png'%(region)))[:-3]
                    filename_na_04 = glob.glob(os.path.join('ScreenShots', 'na_04_%s_*.png'%(region)))[:-3]
                    filename_na_05 = glob.glob(os.path.join('ScreenShots', 'na_05_%s_*.png'%(region)))[:-3]
                    filename_na_06 = glob.glob(os.path.join('ScreenShots', 'na_06_%s_*.png'%(region)))[:-3]

                    filelist_delete = [
                        filename_na_01,
                        filename_na_02,
                        filename_na_03,
                        filename_na_04,
                        filename_na_05,
                        filename_na_06,              
                    ]

                    for files in filelist_delete:
                        for file in files:
                            print(file)
                            os.remove(file)
                    print("file deleted")



                    # 파일 목록 (최근 것만)
                    filename_na_01 = glob.glob(os.path.join('ScreenShots', 'na_01_%s_*.png'%(region)))[-1]
                    filename_na_02 = glob.glob(os.path.join('ScreenShots', 'na_02_%s_*.png'%(region)))[-1]
                    filename_na_03 = glob.glob(os.path.join('ScreenShots', 'na_03_%s_*.png'%(region)))[-1]
                    filename_na_04 = glob.glob(os.path.join('ScreenShots', 'na_04_%s_*.png'%(region)))[-1]
                    filename_na_05 = glob.glob(os.path.join('ScreenShots', 'na_05_%s_*.png'%(region)))[-1]
                    filename_na_06 = glob.glob(os.path.join('ScreenShots', 'na_06_%s_*.png'%(region)))[-1]              


                    filelist = [
                        filename_na_01,
                        filename_na_02,
                        filename_na_03,
                        filename_na_04,
                        filename_na_05,
                        filename_na_06, 

                    ]
                    
                    pdf = PdfFileWriter()

                    inch = 72
                
                    for i, file in enumerate(filelist):  # for each slide
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
                        imgDoc.drawString(20, 560, Sentences_NA_1[i])
                        #imgDoc.drawString(20, 540, Sentences_NA_1[i])
                        #imgDoc.drawString(20, 520, Sentences_NA_1[i])
                        imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                        # x, y - start position
                        # in my case -25, -45 needed
                        imgDoc.save()
                        # Use PyPDF to merge the image-PDF into the template
                        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
                    
                    print("pdf create")
                    filename = 'Infra_in_detail_%s_'%(region) + datetime.now().strftime('%Y%m%d_%H%M') + '.pdf'
                    filename = os.path.join(pdf_path, filename)
                    pdf.write(open(filename,"wb"))
            

                    Created = True

                except Exception as e:
                    print(e)
                    sleep(60)
                    pass
            print()
        elif region == "NA" :
            Created = False
            Sentences_NA_1 = [
                '',
                '',
                '',
                'BM(Bare Metal): CCS NA 내 모든 물리서버 대상 Worst Top 10 정보. Red가 아니면 모두 정상',
                'VM: CCS NA 내 모든 가상서버 대상 Worst Top 10  정보.',
                'NA DB : NA PRD DB 정보 (CPU, Memory, session)',
                '',
                '',
                'Storage: 운영계 스토리지 클러스터 의 IOPS, Throughput 정보',
                'Storage: 운영계 스토리지 클러스터 의 IOPS, Throughput 정보',
                '',
                '',
                '',
                '',
                '',
                # 'IaaS포탈 SLA정의: 1분 간격의 로그인 접속시도 집계. 100% 항상유지 필수/ Total Error값 증가 시 키클락 서비스 확인필요.',
                # 'IaaS포탈 아키텍처 구성 인스턴스 별 CPU/메모리/디스크 목록으로 사용율 80% 초과 시 해당 서비스 재기동 필요.',
                # 'IaaS포탈 전체 인스턴스 다이어그램으로 서비스 Up/Down 체크. 다이어그램 부분 빨간색으로 변동시  서비스 장애로 확인 필요',            

            ]


            Sentences_NA_2 = [
                '',
                '',
                '',
                '(Red 기준 : CPU 10% 이하, 메모리 1G이하, free Disk 10% 이하)',
                '(Red 기준 : CPU 10% 이하, 메모리 500M이하, free Disk 10% 이하)',
                '',
                '',
                '',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '비교 수치 일평균 peak iops / peak throughput (Mbps)',
                '',
                '',
                '',
                '',
                '',
                # '',
                # '',
                # '',
                # '',
                
            ]

            Sentences_NA_3 = [
                'http://10.11.67.29:3000/d/EHCxmuK4k/natms-a10-resource-monitor?orgId=1',
                'http://10.11.67.29:3000/d/HK5wzuFVk22/natms-fw_resource-monitor?orgId=1&refresh=5m',
                'http://10.11.67.29:3000/d/--HdWuF4k/na-prd-ccs-neteuweokeu-jonghab-moniteoring?orgId=1',
                'http://10.11.67.29:3000/d/67-wNjK4k/na-bm-and-netapp-resource?orgId=1',
                'http://10.11.67.29:3000/d/0azeCrF4k/na-vm-resource?orgId=1',
                'http://10.11.67.29:3000/d/7DOFRuKVz/na-prd-db-resource-usage-top-20?orgId=1',
                'http://10.11.67.29:3000/d/1Igbn754k/na_mongodb?orgId=1',
                'http://10.11.67.29:3000/d/LjsjmuF4z/na-prd-netapp-dash-board?orgId=1',
                'https://10.7.0.231/clusters/6035/explorer',
                'https://10.7.0.231/clusters/82788/explorer',
                'http://10.11.67.29:3000/d/DJdDeD5Vz/coc-k8s-summary-dashboard-alert-system-na-1?orgId=1',
                'http://10.11.67.29:3000/d/FnMc6vc4k/coc-k8s-summary-dashboard-alert-system-na-2?orgId=1',
                'http://10.11.67.29:3000/d/iBqceD5Vk/coc-k8s-summary-dashboard-alert-system-na-3?orgId=1',
                'http://10.11.67.29:3000/d/lxRheD5Vz/coc-k8s-summary-dashboard-alert-system-na-4?orgId=1',
                'http://10.11.67.29:3000/d/OYNJ6v5Vz/coc-k8s-summary-dashboard-alert-system-na-5?orgId=1',
                # 'http://172.16.17.74:3000/d/DuMWqtPnk/sla-dashboard?orgId=1&refresh=15m',
                # 'http://172.16.17.74:3000/d/ASnb3Sb7k/dashboard-1?orgId=1&refresh=10s',
                # 'http://172.16.17.74:3000/d/4LbjUmf7z/iaas-dashboard-4?orgId=1&refresh=10s',
                
            ]            
            while not Created:
                try:
                    #파일 삭제 (최근 것 제외)
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', 'LB(A10)_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_mongo = glob.glob(os.path.join('ScreenShots', 'mongo_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_storage_2 = glob.glob(os.path.join('ScreenShots', 'NPS2_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_1 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_1_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_2 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_2_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_3 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_3_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_4 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_4_1center_PRD_*.png'%(region)))[:-3]
                    filename_cluster_info_5 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_5_1center_PRD_*.png'%(region)))[:-3]
                    # filename_zabbix_dash = glob.glob(os.path.join('ScreenShots', 'zabbix_%s_1center_PRD_*.png'%(region)))[:-3]

                    filename_IaaS_SLA = glob.glob(os.path.join('ScreenShots', 'IaaS_SLA_%s_2center_*.png'%(region)))[:-3]
                    filename_IaaS_Resource = glob.glob(os.path.join('ScreenShots', 'IaaS_Resource_%s_2center_*.png'%(region)))[:-3]
                    filename_IaaS_Summary = glob.glob(os.path.join('ScreenShots', 'IaaS_Summary_%s_2center_*.png'%(region)))[:-3]

                    filelist_delete = [
                        filename_lb_a10,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_mongo,
                        filename_netapp_info,
                        filename_storage_1,
                        filename_storage_2,
                        filename_cluster_info_1,
                        filename_cluster_info_2,
                        filename_cluster_info_3,
                        filename_cluster_info_4,
                        filename_cluster_info_5,
                        # filename_zabbix_dash,
                        filename_IaaS_SLA,
                        filename_IaaS_Resource,
                        filename_IaaS_Summary,                        
                    ]

                    for files in filelist_delete:
                        for file in files:
                            print(file)
                            os.remove(file)
                    print("file deleted")



                    # 파일 목록 (최근 것만)
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', 'LB(A10)_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[-1]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_mongo = glob.glob(os.path.join('ScreenShots', 'mongo_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_storage_2 = glob.glob(os.path.join('ScreenShots', 'NPS2_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_1 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_1_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_2 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_2_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_3 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_3_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_4 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_4_1center_PRD_*.png'%(region)))[-1]
                    filename_cluster_info_5 = glob.glob(os.path.join('ScreenShots', 'ccs_k8s_%s_5_1center_PRD_*.png'%(region)))[-1]
                    # filename_zabbix_dash = glob.glob(os.path.join('ScreenShots', 'zabbix_%s_1center_PRD_*.png'%(region)))[-1]
                    # filename_IaaS_SLA = glob.glob(os.path.join('ScreenShots', 'IaaS_SLA_%s_2center_*.png'%(region)))[-1]
                    # filename_IaaS_Resource = glob.glob(os.path.join('ScreenShots', 'IaaS_Resource_%s_2center_*.png'%(region)))[-1]
                    # filename_IaaS_Summary = glob.glob(os.path.join('ScreenShots', 'IaaS_Summary_%s_2center_*.png'%(region)))[-1]                    



                    filelist = [
                        filename_lb_a10,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_mongo,
                        filename_netapp_info,
                        filename_storage_1,
                        filename_storage_2,
                        filename_cluster_info_1,
                        filename_cluster_info_2,
                        filename_cluster_info_3,
                        filename_cluster_info_4,
                        filename_cluster_info_5,
                        # filename_zabbix_dash,
                        # filename_IaaS_SLA,
                        # filename_IaaS_Resource,
                        # filename_IaaS_Summary,
                    ]
                    
                    pdf = PdfFileWriter()

                    inch = 72
                
                    for i, file in enumerate(filelist):  # for each slide
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
                        imgDoc.drawString(20, 560, Sentences_NA_1[i])
                        imgDoc.drawString(20, 540, Sentences_NA_2[i])
                        imgDoc.drawString(20, 520, Sentences_NA_3[i])
                        imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                        # x, y - start position
                        # in my case -25, -45 needed
                        imgDoc.save()
                        # Use PyPDF to merge the image-PDF into the template
                        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
                    
                    print("pdf create")
                    filename = 'Infra_in_detail_%s_'%(region) + datetime.now().strftime('%Y%m%d_%H%M') + '.pdf'
                    filename = os.path.join(pdf_path, filename)
                    pdf.write(open(filename,"wb"))
            

                    Created = True

                except Exception as e:
                    print(e)
                    sleep(60)
                    pass
            print()
        elif region == "CN" :
            Created = False
            Sentences_CN_1 = [
                '',
                '',
                '',
                'BM(Bare Metal): CCS CN 내 모든 물리서버 대상 Worst Top 10 정보. Red가 아니면 모두 정상',
                'VM: CCS CN 내 모든 가상서버 대상 Worst Top 10  정보.',
                'CN DB : CN PRD DB 정보 (CPU, Memory, session)',
                '',
                'Storage: 운영계 스토리지 클러스터 의 IOPS, Throughput 정보',
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

            ]


            Sentences_CN_2 = [
                '',
                '',
                '',
                '(Red 기준 : CPU 10% 이하, 메모리 500M이하, free Disk 10% 이하)',
                '(Red 기준 : CPU 10% 이하, 메모리 300M이하, free Disk 10% 이하)',
                '',
                '',
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
            ]

            Sentences_CN_3 = [
                'http://10.11.67.29:3000/d/CNA10PRDMON/cntms-a10-resource-monitor-2?orgId=1&from=now-24h&to=now',
                'http://10.11.67.29:3000/d/HK5wzuFVk/cntms-fw_resource-monitor?orgId=1',             
                'http://10.11.67.29:3000/d/KEzWdkx4k/cn-prd-ccs-neteuweokeu-jonghab-moniteoring_cn_local_bm?orgId=1',
                'http://10.11.67.29:3000/d/y8fH39F4z/cn-bm-and-netapp-resource_cn_bm?orgId=1',
                'http://10.11.67.29:3000/d/0wC_C9KVk/cn-vm-resource?orgId=1',
                'http://10.11.67.29:3000/d/cuCvRXFVz/cn-prd-db-resource-usage-top-20?orgId=1',
                'http://10.11.67.29:3000/d/UV_0nn54z/cn_mongodb?orgId=1',
                'http://10.11.67.29:3000/d/gCFdtpc4k/cn-netapp-dash-board?orgId=1',
                'https://10.7.0.231/clusters/124202/explorer',
                'http://10.11.67.29:3000/d/6-ohBrAVk/coc-k8s-summary-dashboard-alert-system-hpg?orgId=1',
                'http://10.11.67.29:3000/d/tPHGkO54z/coc-k8s-summary-dashboard-alert-system-2?orgId=1',
                'http://10.11.67.29:3000/d/0SInzdcVk/coc-k8s-summary-dashboard-alert-system-3?orgId=1',
                'http://10.11.67.29:3000/d/gTW4kOcVz/coc-k8s-summary-dashboard-alert-system-4?orgId=1',
                'http://10.11.67.29:3000/d/HUDSkd54k/coc-k8s-summary-dashboard-alert-system-5?orgId=1',
                'http://10.11.67.29:3000/d/qSoHkdcVz/coc-k8s-summary-dashboard-alert-system-6?orgId=1',
                'http://10.11.67.29:3000/d/cYaDzOcVk/coc-k8s-summary-dashboard-alert-system-7?orgId=1',
                'http://10.11.67.29:3000/d/pJ-dkO5Vz/coc-k8s-summary-dashboard-alert-system-8?orgId=1',
                'http://10.11.67.29:3000/d/vRN5zOcVk/coc-k8s-summary-dashboard-alert-system-9?orgId=1',
            ]
            
            while not Created:
                try:
                    #파일 삭제 (최근 것 제외)
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', 'LB(A10)_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_mongo = glob.glob(os.path.join('ScreenShots', 'mongo_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_1 = glob.glob(os.path.join('ScreenShots', '%s_DKC_HPG_Cluster_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_2 = glob.glob(os.path.join('ScreenShots', '%s_DKC_HPL_Cluster_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_3 = glob.glob(os.path.join('ScreenShots', '%s_DKC_KPG_Cluster_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_4 = glob.glob(os.path.join('ScreenShots', '%s_DKC_KPL_Cluster_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_5 = glob.glob(os.path.join('ScreenShots', '%s_DKC_GPQ_Cluster_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_6 = glob.glob(os.path.join('ScreenShots', '%s_DKC_GPL_Cluster_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_7 = glob.glob(os.path.join('ScreenShots', '%s_SVCHUB_Core_Cluster_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_8 = glob.glob(os.path.join('ScreenShots', '%s_SVCHUB_DMZ_Cluster_PRD_*.png'%(region)))[:-3]
                    filename_u_cluster_9 = glob.glob(os.path.join('ScreenShots', '%s_Vtwin_Cluster_PRD_*.png'%(region)))[:-3]

                    filelist_delete = [
                        filename_lb_a10,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_mongo,
                        filename_netapp_info,
                        filename_storage_1,
                        filename_u_cluster_1,
                        filename_u_cluster_2,
                        filename_u_cluster_3,
                        filename_u_cluster_4,
                        filename_u_cluster_5,
                        filename_u_cluster_6,
                        filename_u_cluster_7,
                        filename_u_cluster_8,
                        filename_u_cluster_9,
                    ]

                    for files in filelist_delete:
                        for file in files:
                            print(file)
                            os.remove(file)
                    print("file deleted")



                    # 파일 목록 (최근 것만)
                    filename_lb_a10 = glob.glob(os.path.join('ScreenShots', 'LB(A10)_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_fw_1 = glob.glob(os.path.join('ScreenShots', 'FW_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_total_1 = glob.glob(os.path.join('ScreenShots', '%s_1center_PRD_*.png'%(region)))[-1]
                    filename_host_1 = glob.glob(os.path.join('ScreenShots', 'HOST_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_vm_1 = glob.glob(os.path.join('ScreenShots', 'VM_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_database_1 = glob.glob(os.path.join('ScreenShots', 'DB_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_mongo = glob.glob(os.path.join('ScreenShots', 'mongo_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_netapp_info = glob.glob(os.path.join('ScreenShots', 'NETAPP_INFO_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_storage_1 = glob.glob(os.path.join('ScreenShots', 'NPS1_%s_1center_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_1 = glob.glob(os.path.join('ScreenShots', '%s_DKC_HPG_Cluster_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_2 = glob.glob(os.path.join('ScreenShots', '%s_DKC_HPL_Cluster_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_3 = glob.glob(os.path.join('ScreenShots', '%s_DKC_KPG_Cluster_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_4 = glob.glob(os.path.join('ScreenShots', '%s_DKC_KPL_Cluster_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_5 = glob.glob(os.path.join('ScreenShots', '%s_DKC_GPQ_Cluster_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_6 = glob.glob(os.path.join('ScreenShots', '%s_DKC_GPL_Cluster_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_7 = glob.glob(os.path.join('ScreenShots', '%s_SVCHUB_Core_Cluster_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_8 = glob.glob(os.path.join('ScreenShots', '%s_SVCHUB_DMZ_Cluster_PRD_*.png'%(region)))[-1]
                    filename_u_cluster_9 = glob.glob(os.path.join('ScreenShots', '%s_Vtwin_Cluster_PRD_*.png'%(region)))[-1]

                    filelist = [                       
                        filename_lb_a10,
                        filename_fw_1,
                        filename_total_1,
                        filename_host_1,
                        filename_vm_1,
                        filename_database_1,
                        filename_mongo,
                        filename_netapp_info,
                        filename_storage_1,
                        filename_u_cluster_1,
                        filename_u_cluster_2,
                        filename_u_cluster_3,
                        filename_u_cluster_4,
                        filename_u_cluster_5,
                        filename_u_cluster_6,
                        filename_u_cluster_7,
                        filename_u_cluster_8,
                        filename_u_cluster_9,
                    ]
                    
                    pdf = PdfFileWriter()

                    inch = 72
                
                    for i, file in enumerate(filelist):  # for each slide
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
                        imgDoc.drawString(20, 560, Sentences_CN_1[i])
                        imgDoc.drawString(20, 540, Sentences_CN_2[i])
                        imgDoc.drawString(20, 520, Sentences_CN_3[i])
                        imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                        # x, y - start position
                        # in my case -25, -45 needed
                        imgDoc.save()
                        # Use PyPDF to merge the image-PDF into the template
                        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
                    
                    print("pdf create")
                    filename = 'Infra_in_detail_%s_'%(region) + datetime.now().strftime('%Y%m%d_%H%M') + '.pdf'
                    filename = os.path.join(pdf_path, filename)
                    pdf.write(open(filename,"wb"))
            

                    Created = True

                except Exception as e:
                    print(e)
                    sleep(60)
                    pass
            print()       
        print('종료문')   
if __name__ == '__main__':

    # fonts = [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]
    # print(fonts)
    
    filename = 'Infra_in_detail_' + datetime.now().strftime('%Y%m%d-%H%M') + '.pdf'

    gen_pdf(filename)
