import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# For testing purposes
# WORK_MIN = .1
# SHORT_BREAK_MIN = .1
# LONG_BREAK_MIN = .1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    # reactivate start button
    start_button["state"] = "normal"


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    # disable start button after click
    start_button["state"] = "disabled"

    # convert the number of minutes into seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # print(count)
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    # python dynamic typing (a variable can hold changeable data types ex:a = 3 a = "bmn")
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Make the window pop to forefront of screen
        window.attributes('-topmost',True)
        # Allow for window to be pushed to the background
        window.after_idle(window.attributes,'-topmost',False)
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx = 108, pady = 54, bg = YELLOW)

# canvas
# so that we can use an image in the window
# highlightthickness = 0 to get rid of visible
# border around the canvas
canvas = tkinter.Canvas(width=200, height=226, bg = YELLOW, highlightthickness = 0)
tomato_img = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 135, text = "00:00", 
                    fill = "white", 
                    font = (FONT_NAME, 35, "bold")
)
canvas.grid(row = 1, column = 1)

#"Timer" label
timer_label = tkinter.Label(text = "Timer", 
                            font = ("Arial", 35, "normal"), 
                            fg = GREEN, bg = YELLOW
)
timer_label.grid(row = 0, column = 1)

# start button
start_button = tkinter.Button(text = "Start",
                                highlightthickness = 0,
                                command = start_timer,
                                font = ("Arial", 18, "normal"), 
                                fg = "white", bg = "blue"
)
start_button.grid(row = 2, column = 0)

# reset button
reset_button = tkinter.Button(text = "Reset",
                                highlightthickness = 0,
                                command = reset_timer,
                                font = ("Arial", 18, "normal"),
                                fg = "white", bg = "blue"
)
reset_button.grid(row = 2, column = 2)

# check marks
# marks = ["✔", "✔"]
marks = ""
check_marks = tkinter.Label(text = marks, 
                            font = ("Arial", 16, "bold"),
                            fg = GREEN, bg = YELLOW
)
check_marks.grid(row = 3, column = 1)


window.mainloop()