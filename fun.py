import os
import re

def getImgPath(folder, subdir = True):
    imgPaths = []
    imgFormat = (".jpg", ".png", ".jpeg")

    for filePath, dirnames, fileNames in os.walk(folder):
        for fileName in fileNames:
            if subdir == False and filePath != folder:
                break
            if fileName.endswith(imgFormat):
                imgPaths.append(filePath + "\\" + fileName)

    return imgPaths


