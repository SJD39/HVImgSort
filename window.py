import os
import tkinter
import tkinter.ttk
from tkinter import filedialog
from tkinter import messagebox


# 反馈
def feedback():
    messagebox.showinfo("反馈渠道", "Q群：609062643\r邮箱：sanjiudao@qq.com")


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
svo_status = tkinter.StringVar(value="状态：空闲")

ivo_landscape = tkinter.IntVar(value=1)
ivo_portrait = tkinter.IntVar(value=1)
ivo_other = tkinter.IntVar(value=1)
ivo_sortSubdir = tkinter.IntVar(value=1)
ivo_retainStruct = tkinter.IntVar(value=1)
ivo_retainSource = tkinter.IntVar(value=1)

lbl_landscape = tkinter.ttk.Label(window, text="横向比例：")
lbl_portrait = tkinter.ttk.Label(window, text="纵向比例：")
lbl_selectFolder = tkinter.ttk.Label(window, text="目标文件夹：")
lbl_status = tkinter.ttk.Label(window, textvariable=svo_status)

txt_landscape = tkinter.ttk.Entry(window, textvariable=svo_landscape, width=10)
txt_portrait = tkinter.ttk.Entry(window, textvariable=svo_portrait, width=10)
txt_selectFolder = tkinter.ttk.Entry(
    window, textvariable=svo_selectFolderPath, width=32
)

btn_run = tkinter.ttk.Button(window, text="运行")
btn_error = tkinter.ttk.Button(window, text="反馈", command=feedback)
btn_selectFolder = tkinter.ttk.Button(window, text="选择文件夹", command=selectFolder)
btn_openFolder = tkinter.ttk.Button(window, text="打开文件夹", command=openFolder)

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

lbl_selectFolder.grid(row=1, column=0, padx=5, pady=5)
txt_selectFolder.grid(row=1, column=1, padx=5, pady=5, columnspan=3)
btn_selectFolder.grid(row=1, column=4, padx=5, pady=5)
btn_openFolder.grid(row=1, column=5, padx=5, pady=5)

chk_landscape.grid(row=2, column=0, padx=5, pady=5)
chk_portrait.grid(row=2, column=1, padx=5, pady=5)
chk_other.grid(row=2, column=2, padx=5, pady=5)
chk_sortSubdir.grid(row=2, column=3, padx=5, pady=5)
chk_retainStruct.grid(row=2, column=4, padx=5, pady=5)
chk_retainSource.grid(row=2, column=5, padx=5, pady=5)

prg_progressbar.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

lbl_status.grid(row=4, column=0, columnspan=6, padx=5, pady=5)
window.mainloop()
