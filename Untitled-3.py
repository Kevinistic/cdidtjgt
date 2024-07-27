# DO NOT CHANGE ANYTHING UNLESS YOU KNOW WHAT YOU'RE DOING
# money tracker by @cn3z on Discord

# alamak
import tkinter as tk # gui
import time # importing time from a land faraway
rate_h = 0 # important variables
lasttime = 0
money1 = 0
money3 = 0
result1 = 0
result2 = 0
result3 = 0
time1 = 0
time2 = 0
runtime_seconds = 0
flag1 = True
def idiot_int(prompt): # idiot proof, for integer
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("enter an integer u dumbfuck")
def idiot_str(prompt): # idiot proof, for string
    while True:
        try:
            user_input = str(input(prompt))
            return user_input
        except ValueError:
            print("enter a string u dumbfuck")
def ms(n): # float to minutes and seconds
    m = int(n // 60) # minutes
    s = round(n % 60)
    return f"{m}m {s}s"
def hms(n): # float to hours, minutes and seconds
    h = int(n // 3600) # hours
    rs = n % 3600
    m = int(rs // 60)
    s = round(rs % 60)
    return f"{h}h {m}m {s}s"

def invalidentry(n):
    n.config(bg="red")
    root.after(100, lambda: n.config(bg="white"))
def show_frame(frame): # switcharoo!
    frame.tkraise()
def switch_and_exit(): # switch to frame3 and deth
    show_frame(frame3)
    root.after(1000, root.destroy) # 1000ms = 1s
def process_input(): # PLEASE DO NOT FUCK AROUND WITH THIS FUNCTION UNLESS YOU KNWO WHAT YOURE DOING!!!!!!!!!!
    global rate_h
    global lasttime
    global money1
    global money3
    global result1
    global result2
    global result3
    global time1
    global time2
    global flag1
    entry_string = entry2.get()
    try:
        money2 = int(entry_string) # m2=20 m1=10 m3=10 r1=10 r2=10 r3=10
        if money2 <= 0: raise ValueError # m2 entry, m1 memory, r1 compare, r2 memory-ish?
        result1 = money2-money1
        if is_close(result1, money2):
            money1 = money2 # updating entry to memory
            money3 = money2
        if money3 <= money2 and result1 > 0: # successful case
            result3 = money2-money3
            result2 = result1
            label2_32.config(text=f"{result2:,} (+{(result3):,})")
            if flag1:
                flag1 = False
                time3 = time.time()
                time1 = time3
                time2 = time3
            else:
                time3 = time.time()
                lasttime = time3 - time2
                time2 = time3
                dtime = time3 - time1
                if dtime > 0:
                    rate_s = result2 / dtime
                    rate_h = rate_s * 3600
                else:
                    rate_h = 0
            label2_42.config(text=f"{int(rate_h):,}")
            label2_52.config(text=f"{ms(lasttime)}")
            money3 = money2
        else:
            label2_32.config(text=f"{result2}")
            invalidentry(entry2)
            result1 = result2
        label2_22.config(text=f"{money1:,}")
    except ValueError:
        label2_32.config(text=f"{result2}")
        invalidentry(entry2)
def is_close(a, b, tol=1e-9):
    return abs(a - b) < tol
def runtimef():
    global runtime_seconds
    runtime_seconds += 1
    label2_62.config(text=hms(runtime_seconds))
    root.after(999, runtimef)
def combine1():
    show_frame(frame2)
    runtimef()
def reset():
    global rate_h
    global lasttime
    global money1
    global money3
    global result1
    global result2
    global result3
    global time1
    global time2
    global flag1
    rate_h = 0 # important variables
    lasttime = 0
    money1 = 0
    money3 = 0
    result1 = 0 
    result2 = 0
    result3 = 0
    time1 = 0
    time2 = 0
    flag1 = True
    label2_22.config(text=f"{money1}")
    label2_32.config(text=f"{result2}")
    label2_42.config(text=f"{round(rate_h, 2)}")
    label2_52.config(text=f"{ms(lasttime)}")

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
label1 = tk.Label(frame1, text="Welcome! This program is created to assist your CDID Truck Job grinding. For any inquiries, contact @cn3z on Discord. Click the button below to start.",
                  wraplength=320,
                  justify=tk.LEFT
                  )
label1.pack()

button1 = tk.Button(frame1, text="Here!", command=lambda: combine1())
button1.pack()

# frame 2 content
labelentry = tk.Frame(frame2)
labelentry.grid(row=0, column=0, sticky='w')
label2_1 = tk.Label(labelentry, text="Enter your current money:", justify=tk.LEFT)
label2_1.grid(row=0, column=0, sticky='w')

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

label2_22 = tk.Label(label_frame, text=f"{money1}", justify=tk.LEFT)
label2_32 = tk.Label(label_frame, text=f"{result2}", justify=tk.LEFT)
label2_42 = tk.Label(label_frame, text=f"{rate_h}", justify=tk.LEFT)
label2_52 = tk.Label(label_frame, text=f"{ms(lasttime)}", justify=tk.LEFT)
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
button2_3 = tk.Button(button_frame, text="Leave", command=switch_and_exit)
button2_1.grid(row=0, column=0, sticky='w')
button2_2.grid(row=0, column=1, sticky='w')
button2_3.grid(row=0, column=2, sticky='w')

# frame 3 content
label3 = tk.Label(frame3, text="thanks.",
                  font=("Arial",60),
                  wraplength=300,
                  justify=tk.LEFT
                  )
label3.pack()

# do NOT delete
show_frame(frame1)
root.mainloop()