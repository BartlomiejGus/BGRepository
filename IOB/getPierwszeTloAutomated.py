import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import scipy.misc
import math
import os,sys

path = "C:/Users/barte/Desktop/StudiaMGR/IOB/Projekt/drzewa/dab/"
listaZdjec = os.listdir(path)

for zdjecie in listaZdjec:
    img = cv2.imread(path+zdjecie)
    
    numOfIterations = 3
    margines = 100
    
    imgWidth = img.shape[1]
    imgHeight = img.shape[0]
    
    values = (
    	("Definite Background", cv2.GC_BGD),
    	("Probable Background", cv2.GC_PR_BGD),
    	("Definite Foreground", cv2.GC_FGD),
    	("Probable Foreground", cv2.GC_PR_FGD),
    )
    
    
    #model pierwszego planu
    fgdModel = np.zeros((1,65),np.float64)
    
    #model drugiego planu
    bgdModel = np.zeros((1,65),np.float64)
    
    topx = 0
    topy=0
    botx = imgWidth-topx
    boty = imgHeight-topy
    rect = (topx,topy,(botx-topx+1),(boty-topy+1))
    
    img = img[topy:boty+1,topx:botx+1]
    
    mask = np.zeros(img.shape[:2],np.uint8)
    
    imgWidth = img.shape[1]
    imgHeight = img.shape[0]
    
    mask[0:imgHeight,0:imgWidth]= values[1][1]
    mask[0:imgHeight,0:margines] = values[0][1]
    mask[0:imgHeight,imgWidth-margines:imgWidth] = values[0][1]
    mask[0:imgHeight,int(imgWidth/2)-30:int(imgWidth/2)+30] = values[2][1]
    
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,numOfIterations,cv2.GC_INIT_WITH_MASK)
    
    mask2 = np.where((mask==0)|(mask==2),0,1).astype('uint8')
     
    img = img*mask2[:,:,np.newaxis]
    
    imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresholdValue, imgThreshold = cv2.threshold(imgGrayscale, 1.0, 255.0, cv2.THRESH_BINARY)
                
    
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key = cv2.contourArea, reverse = True) [:2]
    cnt = contours[0]
    
    paramtery = cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,0.01*paramtery,True)
    
    x1,y1,w1,h1 = cv2.boundingRect(approx)
    
    imgDrzewo = img[y1:y1+h1,x1:x1+w1]
    
    drzewoHeight = imgDrzewo.shape[0]
    drzewoWidth = imgDrzewo.shape[1]
    windowWidth = 128
    windowHeight = 128
    
    
    listaZdjec = []
    listaPunktowZdjec = []
    listaPunktowNiepoprawnych = []
    for i in range(0,drzewoHeight,int(windowHeight/2)):
        if(i+windowHeight<drzewoHeight):
            j=0
            while (j+windowWidth<drzewoWidth):
                    imgProbe = imgDrzewo[i:i+windowHeight,j:j+windowWidth]
                    b,g,r = cv2.split(imgProbe)
                    czyPoprawny = True
                    for ii in range(0,windowHeight):
                        for jj in range(0,windowWidth):
                            if b[ii,jj] == 0 and g[ii,jj] == 0 and r[ii,jj] == 0:
                                czyPoprawny = False
                                break
                        if czyPoprawny == False:
                            break
                    if czyPoprawny == True:
                        listaPunktowZdjec.append([i,j])
                        listaZdjec.append(imgProbe)
                        j = j+int(windowWidth/2+1)
                    else:
                        listaPunktowNiepoprawnych.append([i,j])
                        j = j+jj+1
    
    newPath = "C:/Users/barte/Desktop/StudiaMGR/IOB/Projekt/stworzoneDrzewav2/dab/"
    zdjecie = zdjecie[0:len(zdjecie)-4]
    os.mkdir(newPath+zdjecie)
    os.chdir(newPath+zdjecie)
    i=0
    for zdjecie in listaZdjec:
        cv2.imwrite(str(i)+".jpg",zdjecie)
        i=i+1