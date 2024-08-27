# DO NOT CHANGE ANYTHING UNLESS YOU KNOW WHAT YOU'RE DOING
# money tracker by @cn3z on Discord

# alamak
import tkinter as tk # gui
import time # importing time from a land faraway
import math
from tkinter import filedialog
from PIL import Image, ImageTk
d = { # important variables in a dictionary named "d" (stfu ik it's bad naming but whatever)
    "rate_hour": 0,
    "rate_hour_recent": 0,
    "rate_hour_difference": 0,
    "time_difference": 0,
    "money_memory": 0,
    "money_recent": 0,
    "result_placeholder": 0,
    "result_memory": 0,
    "result_difference": 0,
    "time_beginning": 0,
    "time_recent": 0,
    "time_pause_start": 0,
    "time_pause_stop": 0,
    "time_pause_difference": 0,
    "time_pause_total": 0,
    "runtime_seconds": 0,
    "flag_pause": False,
    "flag_time": True,
    "lang": True,
}

language_dict = {
    "EN": {
        "label2_11": "Enter your current money:",
        "label2_21": "Money before start: ",
        "label2_31": "Money earned so far: ",
        "label2_41": "Money per hour: ",
        "label2_51": "Time taken since last update: ",
        "label2_61": "Program runtime: ",
        "button2_4": "ID",
    },
    "ID": {
        "label2_11": "Masukkan uang anda saat ini:",
        "label2_21": "Uang di awal: ",
        "label2_31": "Uang yang didapatkan: ",
        "label2_41": "Uang per jam: ",
        "label2_51": "Waktu sejak terakhir kali update: ",
        "label2_61": "Waktu program berjalan: ",
        "button2_4": "EN",
    }
}

def ms(n): # float to minutes and seconds
    m = int(n // 60) # minutes
    s = math.floor(n % 60)
    return f"{m}m {s}s"

def hms(n): # float to hours, minutes and seconds
    h = int(n // 3600) # hours
    rs = n % 3600
    m = int(rs // 60)
    s = round(rs % 60)
    return f"{h}h {m}m {s}s"

def start_pause():
    global d
    d["time_pause_start"] = time.time()
    d["flag_pause"] = True
    show_frame(frame3)

def stop_pause():
    global d
    d["time_pause_stop"] = time.time()
    d["time_pause_difference"] = d["time_pause_stop"] - d["time_pause_start"]
    d["time_pause_total"] += d["time_pause_difference"]
    show_frame(frame2)

def invalidentry(n):
    n.config(bg="red")
    root.after(100, lambda: n.config(bg="white"))

def show_frame(frame): # switcharoo!
    frame.tkraise()

def process_input(): # PLEASE DO NOT FUCK AROUND WITH THIS FUNCTION UNLESS YOU KNWO WHAT YOURE DOING!!!!!!!!!!
    global d
    entry_string = entry2.get()
    try:
        money_input = int(entry_string)
        if money_input <= 0: raise ValueError
        d["result_placeholder"] = money_input - d["money_memory"]
        if is_close(d["result_placeholder"], money_input):
            d["money_memory"] = money_input
            d["money_recent"] = money_input
        if d["money_recent"] <= money_input and d["result_placeholder"] > 0: # successful case
            d["result_difference"] = money_input - d["money_recent"]
            d["result_memory"] = d["result_placeholder"]
            d["rate_hour_recent"] = d["rate_hour"]
            label2_32.config(text=f"{d['result_memory']:,} (+{d['result_difference']:,})")
            if d["flag_time"]:
                d["flag_time"] = False
                time_input = time.time()
                d["time_beginning"] = time_input
                d["time_recent"] = time_input
            else:
                time_input = time.time()
                if d["flag_pause"]:
                    d["time_difference"] = time_input - d["time_recent"] - d["time_pause_difference"]
                    d["flag_pause"] = False
                else:
                    d["time_difference"] = time_input - d["time_recent"]
                d["time_recent"] = time_input
                time_delta = time_input - d["time_beginning"] - d["time_pause_total"]
                if time_delta > 0:
                    rate_second = d["result_memory"] / time_delta
                    d["rate_hour"] = rate_second * 3600
                else:
                    d["rate_hour"] = 0
            d["rate_hour_difference"] = d["rate_hour"] - d["rate_hour_recent"]
            d["rate_hour_difference"] = f"+{int(d['rate_hour_difference']):,}" if d["rate_hour_difference"] >= 0 else f"{int(d['rate_hour_difference']):,}"
            label2_42.config(text=f"{int(d['rate_hour']):,} ({d['rate_hour_difference']})")
            label2_52.config(text=f"{ms(d['time_difference'])}")
            d["money_recent"] = money_input
        else:
            label2_32.config(text=f"{d['result_memory']}")
            invalidentry(entry2)
            d["result_placeholder"] = d["result_memory"]
        label2_22.config(text=f"{d['money_memory']:,}")
    except ValueError:
        label2_32.config(text=f"{d['result_memory']}")
        invalidentry(entry2)

def is_close(a, b, tol=1e-9):
    return abs(a - b) < tol

def runtimef():
    global d
    d["runtime_seconds"] += 1
    label2_62.config(text=hms(d["runtime_seconds"]))
    root.after(999, runtimef)

def go():
    runtimef()
    show_frame(frame2)

def reset():
    global d
    for key in d.keys():
        if key in ["flag_time", "runtime_seconds", "lang", "flag_pause"]:
            continue
        d[key] = 0
    label2_22.config(text=f"{d['money_memory']}")
    label2_32.config(text=f"{d['result_memory']}")
    label2_42.config(text=f"{round(d['rate_hour'], 2)}")
    label2_52.config(text=f"{ms(d['time_difference'])}")

def language():
    global d
    lang_code = "ID" if d["lang"] else "EN"
    for key, sentence in language_dict[lang_code].items():
        globals()[key].config(text=sentence)
    d["lang"] = not d["lang"]

# main shit
root = tk.Tk()
root.title("CDID Truck Job Grind Tracker")
root.geometry("320x150")  # size in px
root.resizable(False, False) # nuh uh
root.attributes("-topmost", True) # always on top
root.rowconfigure(0, weight=1) # snap to geometry()
root.columnconfigure(0, weight=1)
frame1 = tk.Frame(root) # frames for gui
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame1.grid(row=0, column=0, sticky='nsew') # grids for frames
frame2.grid(row=0, column=0, sticky='nsew')
frame3.grid(row=0, column=0, sticky='nsew')

# frame 1 content
label1 = tk.Label(frame1, text="""Welcome! This program is created to assist your CDID Truck Job grinding. For any inquiries, contact @cn3z on Discord. Click the button below to start.""",
                  wraplength=320,
                  justify=tk.LEFT
                  )
label1.pack()

button1 = tk.Button(frame1, text="Here!", command=lambda: go())
button1.pack()

# frame 2 content
labelentry = tk.Frame(frame2)
labelentry.grid(row=0, column=0, sticky='w')
label2_11 = tk.Label(labelentry, text="Enter your current money:", justify=tk.LEFT)
label2_11.grid(row=0, column=0, sticky='w')

entry2 = tk.Entry(labelentry, justify=tk.LEFT)
entry2.grid(row=0, column=1, sticky='w')

label_frame = tk.Frame(frame2)
label_frame.grid(row=1, column=0, sticky='w')
label2_21 = tk.Label(label_frame, text="Money before start: ", justify=tk.LEFT)
label2_31 = tk.Label(label_frame, text="Money earned so far: ", justify=tk.LEFT)
label2_41 = tk.Label(label_frame, text="Money per hour: ", justify=tk.LEFT)
label2_51 = tk.Label(label_frame, text="Time taken since last update: ", justify=tk.LEFT)
label2_61 = tk.Label(label_frame, text="Program runtime: ", justify=tk.LEFT)
label2_21.grid(row=0, column=0, sticky='w')
label2_31.grid(row=1, column=0, sticky='w')
label2_41.grid(row=2, column=0, sticky='w')
label2_51.grid(row=3, column=0, sticky='w')
label2_61.grid(row=4, column=0, sticky='w')

label2_22 = tk.Label(label_frame, text=f"{d['money_memory']}", justify=tk.LEFT)
label2_32 = tk.Label(label_frame, text=f"{d['result_memory']}", justify=tk.LEFT)
label2_42 = tk.Label(label_frame, text=f"{d['rate_hour']}", justify=tk.LEFT)
label2_52 = tk.Label(label_frame, text=f"{ms(d['time_difference'])}", justify=tk.LEFT)
label2_62 = tk.Label(label_frame, text="", justify=tk.LEFT)
label2_22.grid(row=0, column=1, sticky='w')
label2_32.grid(row=1, column=1, sticky='w')
label2_42.grid(row=2, column=1, sticky='w')
label2_52.grid(row=3, column=1, sticky='w')
label2_62.grid(row=4, column=1, sticky='w')

button_frame = tk.Frame(label_frame)
button_frame.grid(row=5, column=0, sticky='w')
button2_1 = tk.Button(button_frame, text="Update", command=process_input)
button2_2 = tk.Button(button_frame, text="Restart", command=reset)
button2_3 = tk.Button(button_frame, text="Pause", command=start_pause)
button2_4 = tk.Button(button_frame, text="ID", command=language)
button2_1.grid(row=0, column=0, sticky='w')
button2_2.grid(row=0, column=1, sticky='w')
button2_3.grid(row=0, column=2, sticky='w')
button2_4.grid(row=0, column=3, sticky='w')

# frame 3 content
label3 = tk.Label(frame3, text="The program is currently paused. Click the button below to continue.",
                  wraplength=320,
                  justify=tk.LEFT
                  )
label3.pack()

button3 = tk.Button(frame3, text="Here!", command=stop_pause)
button3.pack()

# do NOT delete
show_frame(frame1)
root.mainloop()