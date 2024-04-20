import os

# 获取指定路径下图片路径
# 参数：['路径']
# 返回值：['图片路径']
def getImgPath(folder, subdir = True):
    imgPaths = []
    imgFormat = (".jpg", ".png", ".jpeg")

    for filePath, dirnames, fileNames in os.walk(folder):
        for fileName in fileNames:
            if subdir == False and filePath != folder:
                break
            if fileName.endswith(imgFormat):
                imgPaths.append(filePath + "\\" + fileName)
                continue
        continue

    return imgPaths

# 批量获取图片真实格式
# jpeg  FF D8 FF
# png   89 50 4E 47 0D 0A 1A 0A
# 参数：['图片路径']
# 返回值：['图片路径', '图片格式']
def getTrueFormat(imgPaths):
    imgsFormat = []

    for imgPath in imgPaths:
        with open(imgPath, 'rb') as img:
            imgHead = img.read(11).hex().upper()
            if imgHead[0:16] == "89504E470D0A1A0A":
                imgsFormat.append([imgPath, 'PNG'])
                continue
            elif imgHead[0:6] == "FFD8FF":
                imgsFormat.append([imgPath, 'JPEG'])
                continue

    return imgsFormat

# 批量读取图片长宽信息
# 参数：['图片路径', '图片格式']
def getImgWH(imgsFormat):
    for imgPath, format in imgsFormat:
        match format:
            case "JPEG":
                with open(imgPath, 'rb') as img:
                    i = 0

                    # 读FFC0位置
                    while True:
                        line = img.readline(2).hex().upper()
                        print(line)

                        if line == "":
                            break
                        
                        if line.find("FFC0") != -1:
                            print((i * 4) + line.find("FFC0"))
                            break

                        # 如果C0在一段起始，并且上一段尾是FF
                        if line.find('C0') == 0 and n == True:
                            n = False
                            print((i * 4) - 2)
                            break
                        else:
                            n = False

                        if line.find('FF') == 2:
                            n = True

                        i = i + 1

                    
                continue
            case "PNG":
                continue
            case _:
                continue

getImgWH(getTrueFormat(['C:/Users/15615/Desktop/23.png','C:/Users/15615/Desktop/233.jpg']))
input()