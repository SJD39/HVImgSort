# 批量获取图片真实格式
# jpeg  FF D8
# png   89 50 4E 47 0D 0A 1A 0A
def getTrueFormat(imgPaths):
    imgsFormat = []

    for imgPath in imgPaths:
        with open(imgPath, 'rb') as img:
            imgHead = img.read(11).hex().upper()
            if imgHead[0:16] == "89504E470D0A1A0A":
                imgsFormat.append([imgPath, 'PNG'])
                continue
            elif imgHead[0:4] == "FFD8":
                imgsFormat.append([imgPath, 'JPEG'])
                continue

    return imgsFormat

# 读取图片长宽信息
# jpeg  FF D8
# png   89 50 4E 47 0D 0A 1A 0A
def getImgWH(imgPaths):
    for imgPath in imgPaths:
        with open(imgPath, 'rb') as img:
            imgHead = img.read(11).hex().upper()
            if imgHead[0:16] == "89504E470D0A1A0A":

                continue
            elif imgHead[0:4] == "FFD8":

                continue

