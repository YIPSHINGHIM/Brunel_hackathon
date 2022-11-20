import tkinter as tk

#creates single window for application gui
window = tk.Tk()

input = ["", "", "", ""] #array to store text input

#creates top title
frame_title1 = tk.Frame()
label_title = tk.Label(master=frame_title1, width=60, height = 10, text="Welcome to the stock selector")
label_title.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#text to enter in the stock abbreviation and amount
frame_top1 = tk.Frame()
label_stock_input1 = tk.Label(master=frame_top1, width=30, height = 10, text="Type in the abbreviation of the stock")
label_stock_input1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label_weight_input1 = tk.Label(master=frame_top1, width=30, height = 10, text="Type in the amount of the stock")
label_weight_input1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#fields for users to input data
frame_mid1 = tk.Frame()
stock_name1 = tk.Entry(master=frame_mid1, width=30)
stock_name1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

stock_weight1 = tk.Entry(master=frame_mid1, width=30)
stock_weight1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#button to send data to backend
frame_bot1 = tk.Frame()
button1 = tk.Button(master=frame_bot1, text="Click when complete", width=60 ,height=8, bg="purple")

#once the button is clicked the text in the fields is stored in an array
def handle_click1(event):
    input[0] = stock_name1.get()
    input[1] = stock_weight1.get()

button1.bind("<Button-1>", handle_click1)
button1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#text to enter in the stock abbreviation and amount
frame_top2 = tk.Frame()
label_stock_input2 = tk.Label(master=frame_top2, width=30, height = 10, text="Type in the abbreviation of the stock")
label_stock_input2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label_weight_input2 = tk.Label(master=frame_top2, width=30, height = 10, text="Type in the amount of the stock")

#fields for users to input data
frame_mid2 = tk.Frame()
stock_name2 = tk.Entry(master=frame_mid2, width=30)
stock_name2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

stock_weight2 = tk.Entry(master=frame_mid2, width=30)
stock_weight2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#button to send data to backend
frame_bot2 = tk.Frame()
button2 = tk.Button(master=frame_bot2, text="Click once finished, again",width=60 ,height=8, bg="purple")

#once the button is clicked the text in the fields is stored in an array
def handle_click2(event):
    input[2] = stock_name2.get()
    input[3] = stock_weight2.get()

button2.bind("<Button-1>", handle_click2)
button2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#load first set of inputs
frame_title1.pack()
frame_top1.pack()
frame_mid1.pack()
frame_bot1.pack()
#load second set of inpts
frame_top2.pack()
frame_mid2.pack()
frame_bot2.pack()

window.mainloop()