import os
import tkinter
import tkinter.ttk
from tkinter import filedialog
from tkinter import messagebox
import main


# 反馈
def feedback():
    messagebox.showinfo("保持联系", "建议与我们保持联系以及时获得新的内容或BUG修复\rQ群：609062643\rQQ：3069935480")


# 选择图片文件夹
def selectImgFolder():
    folder = filedialog.askdirectory()
    if folder == "":
        return
    svo_selectImgFolder.set(folder)

    if svo_selectOutFolder.get() != "":
        return
    svo_selectOutFolder.set(folder)
    return


# 选择输出文件夹
def selectOutFolder():
    folder = filedialog.askdirectory()
    if folder == "":
        return
    svo_selectOutFolder.set(folder)
    return


# 打开图片文件夹
def openImgFolder():
    path = svo_selectImgFolder.get()
    if path == "":
        return
    os.system("start " + path)
    return


# 打开输出文件夹
def openOutFolder():
    path = svo_selectOutFolder.get()
    if path == "":
        return
    os.system("start " + path)
    return


window = tkinter.Tk()
window.title("横竖图分类4.0")

svo_selectImgFolder = tkinter.StringVar()
svo_selectOutFolder = tkinter.StringVar()
svo_landscape = tkinter.StringVar(value=1.5)
svo_portrait = tkinter.StringVar(value=0.5)
svo_status = tkinter.StringVar(value="状态：空闲")

ivo_landscape = tkinter.IntVar(value=1)
ivo_portrait = tkinter.IntVar(value=1)
ivo_other = tkinter.IntVar(value=1)
ivo_sortSubdir = tkinter.IntVar(value=1)
ivo_retainStruct = tkinter.IntVar(value=1)
ivo_retainSource = tkinter.IntVar(value=1)

lbl_landscape = tkinter.ttk.Label(window, text="横向比例：")
lbl_portrait = tkinter.ttk.Label(window, text="纵向比例：")
lbl_selectImgFolder = tkinter.ttk.Label(window, text="图片文件夹：")
lbl_selectOutFolder = tkinter.ttk.Label(window, text="输出文件夹：")
lbl_status = tkinter.ttk.Label(window, textvariable=svo_status)

txt_landscape = tkinter.ttk.Entry(window, textvariable=svo_landscape, width=10)
txt_portrait = tkinter.ttk.Entry(window, textvariable=svo_portrait, width=10)
txt_selectImgFolder = tkinter.ttk.Entry(
    window, textvariable=svo_selectImgFolder, width=32
)
txt_selectOutFolder = tkinter.ttk.Entry(
    window, textvariable=svo_selectOutFolder, width=32
)

btn_run = tkinter.ttk.Button(window, text="运行", command=main.run)
btn_error = tkinter.ttk.Button(window, text="保持联系", command=feedback)
btn_selectImgFolder = tkinter.ttk.Button(window, text="选择文件夹", command=selectImgFolder)
btn_openImgFolder = tkinter.ttk.Button(window, text="打开文件夹", command=openImgFolder)
btn_selectOutFolder = tkinter.ttk.Button(window, text="选择文件夹", command=selectOutFolder)
btn_openOutFolder = tkinter.ttk.Button(window, text="打开文件夹", command=openOutFolder)

chk_landscape = tkinter.ttk.Checkbutton(window, text="需要横图", variable=ivo_landscape)
chk_portrait = tkinter.ttk.Checkbutton(window, text="需要竖图", variable=ivo_portrait)
chk_other = tkinter.ttk.Checkbutton(window, text="需要其它", variable=ivo_other)
chk_sortSubdir = tkinter.ttk.Checkbutton(window, text="分类子目录", variable=ivo_sortSubdir)
chk_retainStruct = tkinter.ttk.Checkbutton(
    window, text="保留目录结构", variable=ivo_retainStruct
)
chk_retainSource = tkinter.ttk.Checkbutton(
    window, text="保留源文件", variable=ivo_retainSource
)

prg_progressbar = tkinter.ttk.Progressbar(window, length=640)

lbl_landscape.grid(row=0, column=0, padx=5, pady=5)
txt_landscape.grid(row=0, column=1, padx=5, pady=5)
lbl_portrait.grid(row=0, column=2, padx=5, pady=5)
txt_portrait.grid(row=0, column=3, padx=5, pady=5)
btn_run.grid(row=0, column=4, padx=5, pady=5)
btn_error.grid(row=0, column=5, padx=5, pady=5)

lbl_selectImgFolder.grid(row=1, column=0, padx=5, pady=5)
txt_selectImgFolder.grid(row=1, column=1, padx=5, pady=5, columnspan=3)
btn_selectImgFolder.grid(row=1, column=4, padx=5, pady=5)
btn_openImgFolder.grid(row=1, column=5, padx=5, pady=5)

lbl_selectOutFolder.grid(row=2, column=0, padx=5, pady=5)
txt_selectOutFolder.grid(row=2, column=1, padx=5, pady=5, columnspan=3)
btn_selectOutFolder.grid(row=2, column=4, padx=5, pady=5)
btn_openOutFolder.grid(row=2, column=5, padx=5, pady=5)

chk_landscape.grid(row=3, column=0, padx=5, pady=5)
chk_portrait.grid(row=3, column=1, padx=5, pady=5)
chk_other.grid(row=3, column=2, padx=5, pady=5)
chk_sortSubdir.grid(row=3, column=3, padx=5, pady=5)
chk_retainStruct.grid(row=3, column=4, padx=5, pady=5)
chk_retainSource.grid(row=3, column=5, padx=5, pady=5)

prg_progressbar.grid(row=4, column=0, columnspan=6, padx=5, pady=5)

lbl_status.grid(row=5, column=0, columnspan=6, padx=5, pady=5)
window.mainloop()
