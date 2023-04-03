import tkinter as tk

height = 1000
width = 1000
header_font = 80
text_font =40


def bpm_function(bpm):
    hertz_result["text"] =round(int(str(bpm)) / 60, ndigits=3)

def pld_function(path_one, path_two):
    path_result["text"]= round(344/ (((float(str(path_two))) - (float(str(path_one))))*2), 2)

def atd_function(timeInput_one, timeInput_two):
    time_result["text"]= round(1/ (((float(str(timeInput_two))) - float(str(timeInput_one)))* 2), 2)


root = tk.Tk()


#main canvas
canvas = tk.Canvas(root, height=height, width=width, bg="black")
canvas.pack()

#inside frame
inside_frame = tk.Frame(root, bg="white")
inside_frame.place(relwidth=0.98, relheight=0.98, rely=0.01, relx=0.01)

#header label
header = tk.Label(inside_frame, font=header_font, text="The Audio Engineering Toolkit", fg="white")
header.place(relwidth= 0.2, relheight= 0.05, rely=0, relx=0.404)

#BPM to Hertz header label
bpm_header = tk.Label(inside_frame, font=header_font, text="BPM to Hertz", fg="white")
bpm_header.place(relheight=0.05, relwidth= 0.2, relx=0.404, rely=0.09)

#User input for bpm
bpm = tk.Entry(inside_frame, font=text_font, bg="white", fg="black", cursor="dot", justify="right")
bpm.place(relheight=0.03, relwidth= 0.05, relx=0.3, rely=0.19)

#Bpm label
bpm_text = tk.Label(inside_frame, font=text_font, text="BPM", bg="white", fg="black")
bpm_text.place(relheight=0.018, relwidth=0.03, rely=0.195, relx=0.35)

#BPM to hertz calculate button
bpm_calc_button= tk.Button(inside_frame, font=header_font, text="Calculate", bg="white", fg="black", command=lambda: bpm_function(bpm.get()))
bpm_calc_button.place(relheight=0.05, relwidth=0.2, relx=0.404, rely=0.18)

#Display result of bpm to hertz
hertz_result= tk.Label(inside_frame, font=text_font, bg="black", fg="white", borderwidth=1)
hertz_result.place(relheight=0.03, relwidth= 0.09, rely=0.193, relx=0.65)

#Hertz result
hertz_label = tk.Label(inside_frame, font=text_font, text="Hz", bg="white", fg="black", height=1)
hertz_label.place(relx=0.74, rely=0.195)

#Comb filtering Path lengh difference
comb_filter_PLD = tk.Label(inside_frame, font=header_font, text="Comb Filtering: \n Path Length Difference", bg="black", fg="white")
comb_filter_PLD.place(relheight=0.05, relwidth=0.2, rely=0.28, relx=0.404)

#User input for Path length one
path_one = tk.Entry(inside_frame, font=text_font, bg="white", fg="black", cursor="dot", justify="right")
path_one.place(relheight=0.03, relwidth= 0.05, relx=0.3, rely=0.36)

path_label_one = tk.Label(inside_frame, font=text_font, text="Path Length One", bg="white", fg="black")
path_label_one.place(relx=0.18, rely=0.365)

path_meter_label1 =tk.Label(inside_frame, font =text_font, text="Metre", bg="white", fg="black")
path_meter_label1.place(relx=0.35, rely=0.366)

#Note for user
note_PLD =tk.Label(inside_frame, font =text_font, text="Note: Path one must be the \n shortest distance from \nthe source", bg="yellow", fg="black")
note_PLD.place(relx=0.0, rely=0.366)

#User input for path length two
path_two = tk.Entry(inside_frame, font=text_font, bg="white", fg="black", cursor="dot", justify="right")
path_two.place(relheight=0.03, relwidth= 0.05, relx=0.3, rely=0.4)

path_label_two = tk.Label(inside_frame, font=text_font, text="Path Length Two", bg="white", fg="black")
path_label_two.place(relx=0.18, rely=0.405)

path_meter_label2 =tk.Label(inside_frame, font =text_font, text="Metre", bg="white", fg="black")
path_meter_label2.place(relx=0.35, rely=0.405)

#Calculate PLD Button
path_calButton = tk.Button(inside_frame, text="Calculate \n Speed of Sound 344m/s", bg="white", fg="black", command=lambda: pld_function (path_one.get(), path_two.get()))
path_calButton.place(relheight=0.05, relwidth=0.2, relx=0.404, rely= 0.38)

#Result of PLD
path_result = tk.Label(inside_frame, font=text_font, bg="black", fg="white", height=1)
path_result.place(relheight=0.03, relwidth= 0.09, relx=0.65, rely= 0.4)

path_hertz_label =tk.Label(inside_frame, font =text_font, text="Hz", bg="white", fg="black")
path_hertz_label.place(relx=0.74, rely=0.405)

#Comb filtering ATD
comb_filter_ATD = tk.Label(inside_frame, font=header_font, text="Comb Filtering: \n Time Arrival Difference", bg="black", fg="white")
comb_filter_ATD.place(relheight=0.05, relwidth=0.2, rely=0.49, relx=0.404)

#User input for ATD one
timeInput_one = tk.Entry(inside_frame, font=text_font, bg="white", fg="black", cursor="dot", justify="right")
timeInput_one.place(relheight=0.03, relwidth= 0.05, relx=0.3, rely=0.57)

time_label_one = tk.Label(inside_frame, font=text_font, text="Arrival Time One", bg="white", fg="black")
time_label_one.place(relx=0.18, rely=0.57)

Time_arrival_label1 =tk.Label(inside_frame, font =text_font, text="Sec", bg="white", fg="black")
Time_arrival_label1.place(relx=0.35, rely=0.575)

#Note for user
note_PLD =tk.Label(inside_frame, font =text_font, text="Note: Time one must be the \n shortest arrival time from \nthe source", bg="yellow", fg="black")
note_PLD.place(relx=0.0, rely=0.57)

#User input for ATD two
timeInput_two = tk.Entry(inside_frame, font=text_font, bg="white", fg="black", cursor="dot", justify="right")
timeInput_two.place(relheight=0.03, relwidth= 0.05, relx=0.3, rely=0.61)

time_label_two = tk.Label(inside_frame, font=text_font, text="Arrival Time Two", bg="white", fg="black")
time_label_two.place(relx=0.18, rely=0.61)

Time_arrival_label2 =tk.Label(inside_frame, font =text_font, text="Sec", bg="white", fg="black")
Time_arrival_label2.place(relx=0.35, rely=0.615)

#Calculate ATD Button
time_calButton = tk.Button(inside_frame, text="Calculate \n 1 / T", bg="white", fg="black", command=lambda: atd_function (timeInput_one.get(), timeInput_two.get()))
time_calButton.place(relheight=0.05, relwidth=0.2, relx=0.404, rely= 0.589)

time_result = tk.Label(inside_frame, font=text_font, bg="black", fg="white", height=1)
time_result.place(relheight=0.03, relwidth= 0.09, relx=0.65, rely= 0.609)

time_seconds_label =tk.Label(inside_frame, font =text_font, text="Hz", bg="white", fg="black")
time_seconds_label.place(relx=0.74, rely=0.615)

root.mainloop()


