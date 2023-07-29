import os
import tkinter
import tkinter.ttk
from tkinter import filedialog


# 选择文件夹
def selectFolder():
    folderPath = filedialog.askdirectory()
    if folderPath == "":
        return
    svo_selectFolderPath.set(folderPath)
    return


# 打开文件夹
def openFolder():
    path = svo_selectFolderPath.get()
    if path == "":
        return
    os.system("start " + path)
    return


window = tkinter.Tk()
window.title("横竖图分类4.0")

svo_selectFolderPath = tkinter.StringVar()
svo_landscape = tkinter.StringVar(value=1.5)
svo_portrait = tkinter.StringVar(value=0.5)

lbl_landscape = tkinter.ttk.Label(window, text="横向比例：")
txt_landscape = tkinter.ttk.Entry(window, textvariable=svo_landscape, width=10)
lbl_portrait = tkinter.ttk.Label(window, text="纵向比例：")
txt_portrait = tkinter.ttk.Entry(window, textvariable=svo_portrait, width=10)
btn_run = tkinter.ttk.Button(window, text="运行")
lbl_selectFolder = tkinter.ttk.Label(window, text="目标文件夹：")
txt_selectFolder = tkinter.ttk.Entry(window, textvariable=svo_selectFolderPath)
btn_selectFolder = tkinter.ttk.Button(window, text="选择文件夹", command=selectFolder)
btn_openFolder = tkinter.ttk.Button(window, text="打开文件夹", command=openFolder)

lbl_landscape.grid(row=0, column=0, padx=5, pady=5)
txt_landscape.grid(row=0, column=1, padx=5, pady=5)
lbl_portrait.grid(row=0, column=2, padx=5, pady=5)
txt_portrait.grid(row=0, column=3, padx=5, pady=5)
btn_run.grid(row=0, column=4, padx=5, pady=5)

lbl_selectFolder.grid(row=1, column=0, padx=5, pady=5)
txt_selectFolder.grid(row=1, column=1, padx=5, pady=5, columnspan=2)
btn_selectFolder.grid(row=1, column=3, padx=5, pady=5)
btn_openFolder.grid(row=1, column=4, padx=5, pady=5)

window.mainloop()
