import os
import re

imgFormat = (".jpg", ".png", ".jpeg")


def getImgPath(folder, subdir=True):
    imgPaths = []

    for filePath, dirnames, fileNames in os.walk(folder):
        for fileName in fileNames:
            if subdir == False and filePath != folder:
                break
            if fileName.endswith(imgFormat):
                imgPaths.append(filePath + "\\" + fileName)

    return imgPaths
