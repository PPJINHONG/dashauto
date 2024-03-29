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

Sentences1 = [
    '',
    '',
    '',
    '',
    '',

]


Sentences2 = [
    '',
    '',
    '',
    '',
    '',

]


screenshots_path = 'ScreenShots'
isExist = os.path.exists(screenshots_path)
if not isExist:
    os.makedirs(screenshots_path)
    print("The new directory is created!")

# 리포트 폴더 지정
jeniffer_pdf_path = 'Reports'

# 리포트 폴더 존재 유무 체크 (필요 시 생성)
isExist = os.path.exists(jeniffer_pdf_path)
if not isExist:
    os.makedirs(jeniffer_pdf_path)
    print("The new directory is created!")

def gen_jeniffer_pdf():
    Created = False
    while not Created:
        try:
            # 파일 삭제 (최근 것 제외)
            filename_1 = glob.glob(os.path.join('ScreenShots', 'TMS_MAIN_*.png'))[:-3]
            filename_2 = glob.glob(os.path.join('ScreenShots', 'TMS_Gen1_*.png'))[:-3]
            filename_3 = glob.glob(os.path.join('ScreenShots', 'TMS_Gen2_*.png'))[:-3]
            filename_4 = glob.glob(os.path.join('ScreenShots', 'TMS_ETC_*.png'))[:-3]
            # filename_5 = glob.glob(os.path.join('ScreenShots', 'TMS_SBS_VOICE_*.png'))[:-3]
            # filename_6 = glob.glob(os.path.join('ScreenShots', 'CENTER_SEARCH_MAIN_*.png'))[:-3]
            # filename_7 = glob.glob(os.path.join('ScreenShots', 'CENTER_SEARCH_OLD_*.png'))[:-3]
            # filename_8 = glob.glob(os.path.join('ScreenShots', 'CENTER_SEARCH_NEW_*.png'))[:-3]
            # filename_9 = glob.glob(os.path.join('ScreenShots', 'VCRM_*.png'))[:-3]

            filenames = [
                filename_1,
                filename_2,
                filename_3,
                filename_4,
                #filename_5,
                # filename_6,
                # filename_7,
                # filename_8,
                # filename_9,
            ]

            for files in filenames:
                for file in files:
                    print(file)
                    os.remove(file)
            print("file deleted")

            # # 파일 목록 (최근 것만)
            filename_1 = glob.glob(os.path.join('ScreenShots', 'TMS_MAIN_*.png'))[-1]
            filename_2 = glob.glob(os.path.join('ScreenShots', 'TMS_Gen1_*.png'))[-1]
            filename_3 = glob.glob(os.path.join('ScreenShots', 'TMS_Gen2_*.png'))[-1]    
            filename_4 = glob.glob(os.path.join('ScreenShots', 'TMS_ETC_*.png'))[-1]
            #filename_5 = glob.glob(os.path.join('ScreenShots', 'TMS_SBS_VOICE_*.png'))[-1]
            # filename_6 = glob.glob(os.path.join('ScreenShots', 'CENTER_SEARCH_MAIN_*.png'))[-1]
            # filename_7 = glob.glob(os.path.join('ScreenShots', 'CENTER_SEARCH_OLD_*.png'))[-1]
            # filename_8 = glob.glob(os.path.join('ScreenShots', 'CENTER_SEARCH_NEW_*.png'))[-1]
            # filename_9 = glob.glob(os.path.join('ScreenShots', 'VCRM_*.png'))[-1]

            filenames = [
                filename_1,
                filename_2,
                filename_3,
                filename_4,
                #filename_5,
                # filename_6,
                # filename_7,
                # filename_8,
                # filename_9,
            ]
            
            pdf = PdfFileWriter()

            inch = 72

            for i, file in enumerate(filenames):  # for each slide
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
                imgDoc.drawString(20, 560, Sentences1[i])
                imgDoc.drawString(20, 540, Sentences2[i])
                imgDoc.drawImage(file, 0, 0, width=780, height=590, preserveAspectRatio=True, mask='auto')
                # x, y - start position
                # in my case -25, -45 needed
                imgDoc.save()
                # Use PyPDF to merge the image-PDF into the template
                pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
            filename = 'Jennifer_dashboard_KR_' + datetime.now().strftime('%Y%m%d-%H%M') + '.pdf'
            filename = os.path.join(jeniffer_pdf_path, filename)
            pdf.write(open(filename,"wb"))
            Created = True
        except Exception as e:
            print(e)
            sleep(10)
            pass

# if __name__ == '__main__':

#     # fonts = [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]
#     # print(fonts)
    
#     filename = 'Jennifer_dashboard_' + datetime.now().strftime('%Y%m%d-%H%M') + '.pdf'

#     gen_pdf(filename)