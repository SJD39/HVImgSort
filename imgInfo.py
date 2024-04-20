# 批量获取图片真实格式
# jpeg  FF D8 FF
# png   89 50 4E 47 0D 0A 1A 0A
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
def getImgWH(imgsFormat):
    for imgPath, format in imgsFormat:
        match format:
            case "JPEG":
                with open(imgPath, 'rb') as img:
                    print(img.read(200).hex().upper())
                continue
            case "PNG":
                continue
            case _:
                continue

getImgWH(getTrueFormat(['C:/Users/15615/Desktop/23.png','C:/Users/15615/Desktop/233.jpg']))