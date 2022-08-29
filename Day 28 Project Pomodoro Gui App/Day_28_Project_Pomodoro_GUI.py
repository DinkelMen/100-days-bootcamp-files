from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
marks = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global marks, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label1.config(text='Timer')
    marks = ''
    label2['text'] = marks
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label1['text'] = 'Rest!'
        label1['fg'] = RED
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label1['text'] = 'Rest!'
        label1['fg'] = PINK
        count_down(short_break_sec)
    else:
        label1['text'] = 'Work!'
        label1['fg'] = GREEN
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, marks
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks += '✔'
            label2['text'] = marks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 27, 'bold'))
canvas.grid(column=1, row=1)

# count_down(5)

label1 = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
label1.grid(column=1, row=0)

label2 = Label(text=marks, font=(FONT_NAME, 10, 'bold'), fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

button1 = Button(text='Start', command=start_timer)
button1.grid(row=2, column=0)

button2 = Button(text='Reset', command=reset_timer)
button2.grid(row=2, column=2)


window.mainloop()
