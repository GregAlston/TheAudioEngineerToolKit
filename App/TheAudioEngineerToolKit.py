import tkinter as tk

height = 1000
width = 1000
header_font = 80



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



root.mainloop()


