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


def delfile():
    
    
    try:

        filename_a1 = glob.glob(os.path.join('ScreenShots', 'image1_*.png'))[:-3]
        filename_a2 = glob.glob(os.path.join('ScreenShots', 'image2_*.png'))[:-3]
        
        filelist_delete = [
            filename_a1,
            filename_a2,
        ]
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


    
    try:

        filename_a1 = glob.glob(os.path.join('ScreenShots', 'image1_*.png'))[:-3]
        filename_a1 = glob.glob(os.path.join('ScreenShots', 'image2_*.png'))[:-3]

        filelist = [
              filename_a1,
              filename_a2,
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









        #아래 저장 구문

    except Exception as e:
          print("리포트저장에러")







if __name__ == '__main__':

    # fonts = [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]
    # print(fonts)
    
    filename = 'Infra_in_detail_' + datetime.now().strftime('%Y%m%d-%H%M') + '.pdf'

    gen_pdf(filename)