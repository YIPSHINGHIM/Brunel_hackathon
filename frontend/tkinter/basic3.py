import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk() #creates single window for application gui
input_dictionary = {} #stores inputs to be sent to database with API
input = ["", "", "", ""] #array to seperate inputs

#creates top title
frame_title1 = tk.Frame()
#label_title = tk.Label(master=frame_title1, width=60, height = 10, text="Welcome to the stock selector")
#label_title.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
title_image = Image.open("frontend/tkinter/gui_title.png")
title_image = ImageTk.PhotoImage(title_image)
label_title_image = tk.Label(master = frame_title1, image=title_image)
label_title_image.pack()

#text to enter in the stock abbreviation and amount
frame_top = tk.Frame()
label_stock_input1 = tk.Label(master=frame_top, width=30, height = 6, text="Type in the abbreviation of the stock")
label_stock_input1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label_weight_input1 = tk.Label(master=frame_top, width=30, height = 6, text="Type in the amount of the stock")
label_weight_input1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label_stock_input2 = tk.Label(master=frame_top, width=30, height = 6, text="Type in the abbreviation of the stock")
label_stock_input2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label_weight_input2 = tk.Label(master=frame_top, width=30, height = 6, text="Type in the amount of the stock")
label_weight_input2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#fields for users to input data
frame_mid = tk.Frame()
stock_name1 = tk.Entry(master=frame_mid, width=30)
stock_name1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

stock_name2 = tk.Entry(master=frame_mid, width=30)
stock_name2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

stock_weight1 = tk.Entry(master=frame_mid, width=30)
stock_weight1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

stock_weight2 = tk.Entry(master=frame_mid, width=30)
stock_weight2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#button to send data to backend
frame_bot = tk.Frame()
button1 = tk.Button(master=frame_bot, text="Click when complete", width=60 ,height=8, bg="purple")
button2 = tk.Button(master=frame_bot, text="Click to clear fields",width=60 ,height=8, bg="purple")

def handle_click1(event):
    input[0] = stock_name1.get()
    input[1] = stock_weight1.get()
    input[2] = stock_name2.get()
    input[3] = stock_weight2.get()

    if input[0] != "":
        input_dictionary[input[0]] = input[1]
    
    if input[2] != "":
        input_dictionary[input[2]] = input[3]

#button clears text for ease of use
def handle_click2(event):
    input[0] = stock_name1.get()
    input[1] = stock_weight1.get()
    input[2] = stock_name2.get()
    input[3] = stock_weight2.get()
    
    stock_name1.delete(0, len(input[0]))
    stock_name2.delete(0, len(input[1]))
    stock_weight1.delete(0, len(input[2]))
    stock_weight2.delete(0, len(input[3]))

button2.bind("<Button-1>", handle_click2)
button1.bind("<Button-1>", handle_click1)
button1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
button2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Terminal = tk.Text(width=100, height = 10)
Terminal.pack()

#textframe = tk.Frame(master=window)
#Terminal1 = tk.Text(master = textframe, width=100, height = 130)
#Terminal1.pack()
#textframe.pack()

#load gui
frame_title1.pack()
frame_top.pack()
frame_mid.pack()
frame_bot.pack()

window.mainloop()