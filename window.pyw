import tkinter as builder
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from y2_logic import *
from contextlib import contextmanager
import string

# Connects Logic with window
def send_to_youtube():
    url = str(link_url.get())
    res = str(video_res.get())
    file_name = str(fileName.get())

    # link_url_ent.delete(0, 'end')
    fileName.delete(0, 'end')

    if res == "1080p":
        func0(url, file_name)
    elif res == "360p":
        func1(url, file_name)
    elif res == "Audio Only":
        func2(url, file_name)
    video_res_sel['state'] = "disabled"


# Directory Browser Function
def directory_browse():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

def updateList_url(url):
    if "https://www.youtube.com/watch?v=" in url and len(url) > 32:
        video_list = getResList(url)
        video_res_sel['values'] = video_list
        video_res_sel['state'] = "normal"
    else:
        video_res_sel['state'] = "disabled"


# Window Builder / INFO
window = builder.Tk()
window.title()
window.configure(background='#383838')
window.geometry("1000x450")
window.attributes("-alpha", 0.9)
window.title("Y2-Hub")
windowWidth = 1000
windowHeight = 450
posR = int(window.winfo_screenwidth()/2 - windowWidth/2)
posL = int(window.winfo_screenheight()/2.3 - windowHeight/2)
window.geometry("+{}+{}".format(posR, posL))

# VARIABLES
folder_path = builder.StringVar()
var = builder.IntVar()

# Entries for Title and link
link_url = builder.StringVar()
link_url.trace("w", lambda name, index, mode, link_url=link_url: updateList_url(link_url.get()))
# link_url_ent = builder.Entry(text="URL", fg="black", bg="grey", width=70, textvariable=link_url)
link_url_ent = builder.Text(window, width=70, height=3, fg="black", bg="grey")
link_url_ent.bind('<KeyRelease>', lambda *args: updateList_url(link_url_ent.get("1.0",END)))
fileName = builder.Entry(text="name", fg="black", bg="yellow", width=60)
link_url_ent.pack()
fileName.pack()

# Buttons (Download, Browse)
button = builder.Button(
    window,
    text = "Download",
    width=40,
    height=10,
    bg="black",                                                                                                                                                                                                                                                                                                                                                                         
    fg="white",
    command=send_to_youtube
)
button.pack()

button_file = builder.Button(window, text="Browse", command=directory_browse, width=20, height=10, bg="white")
button_file.pack()

video_res = builder.StringVar()
video_res_sel = ttk.Combobox(window, width="33", textvariable=video_res, state="disabled")
video_res_sel.pack()

window.mainloop()