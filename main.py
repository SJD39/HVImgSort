import window
import imgInfo
import fun

imgPaths = []


def run():
    imgFolder = window.svo_selectImgFolder.get()
    if imgFolder == "":
        window.messagebox.showerror("错误", "请选择图片文件夹")
        return
    print(imgFolder)
    return
