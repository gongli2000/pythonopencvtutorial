import cv2
import numpy as np

def showImage(image):
        cv2.imshow('windowname', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        
def getBlobsImage():
    return cv2.imread('/Users/larry/sampleimages/twoblobs.png')


def getContours(im):
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours,mh

def drawContours(image,contours,rgb,thickness):
         cv2.drawContours(image, contours, -1, rgb, thickness)


def drawContoursOnImage():
        im = getBlobsImage()
        im2,contours = getContours(im)
        drawContours(im,contours,(0,255,0),3)
        showImag

drawContoursOnImage()


def captureCamera():
        cap = cv2.VideoCapture(0)
        while(True):
                ret, frame = cap.read()
                cv2.imshow('image',frame)
                if (cv2.waitKey(1) >= 0):
                   break
        cv2.destroyAllWindows()
        cv2.waitKey(1)


