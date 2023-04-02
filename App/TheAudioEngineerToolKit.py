import tkinter as tk

height = 1000
width = 1000
header_font = 80
text_font =40


def bpm_function(bpm):
    hert_result["text"] =round(int(str(bpm)) / 60, ndigits=3)

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

#BPM header label
bpm_header = tk.Label(inside_frame, font=header_font, text="BPM to Hertz", fg="white")
bpm_header.place(relheight=0.05, relwidth= 0.2, relx=0.404, rely=0.09)

#User input for bpm
bpm = tk.Entry(inside_frame, font=text_font, bg="white", fg="black")
bpm.place(relx=0.15, rely=0.19)

#Bpm symbol
bpm_text = tk.Label(inside_frame, font=text_font, text="BPM", bg="white", fg="black")
bpm_text.place(relheight=0.018, relwidth=0.04, rely=0.2, relx=0.349)

#BPM to hertz calculate button
bpm_calc_button= tk.Button(inside_frame, font=header_font, text="Calculate", bg="yellow", fg="black", command=lambda: bpm_function(bpm.get()))
bpm_calc_button.place(relheight=0.05, relwidth=0.2, relx=0.404, rely=0.18)

#Display result of bpm to hertz
hert_result= tk.Label(inside_frame, font=text_font, bg="black", fg="white", borderwidth=1)
hert_result.place(relheight=0.028, relwidth= 0.2, rely=0.19, relx=0.68)






root.mainloop()


