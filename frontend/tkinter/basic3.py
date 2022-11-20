import tkinter as tk

window = tk.Tk()

frame_top1 = tk.Frame()
#label_title = tk.Label(master=frame_top1, width=50, height = 10, text="Welcome to the stock selector")
#label_title.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx = 5, pady = 5, sticky = "n")


label_stock_input = tk.Label(master=frame_top1, width=50, height = 10, text="Type in the abbreviation of the stock", bg="blue")
label_stock_input.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame_mid1 = tk.Frame()
stock_name1 = tk.Entry(master=frame_mid1, width = 50, bg="blue")
stock_name1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame_bot1 = tk.Frame()
label_weight1 = tk.Label(width=50, height = 10, text="Type in the amount of the stock", bg="blue")
label_weight1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

stock_weight1 = tk.Entry(bg="blue")
stock_weight1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

button1 = tk.Button(text="Enter",width=50 ,height=8, bg="blue")
button1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
'''
frame_top2 = tk.Frame()
label_stock_input = tk.Label(master=frame_top2, width=50, height = 10, text="Type in the abbreviation of the stock")
label_stock_input.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx = 5, pady = 5)

stock_name2 = tk.Entry(master=frame_top2, padx = 5, pady = 5, bg="purple")

frame_bot2 = tk.Frame()
label_weight2 = tk.Label(master=frame_bot2, width=50, height = 10, text="Type in the amount of the stock")
label_weight2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx = 5, pady = 5)

stock_weight2 = tk.Entry(master=frame_bot2, padx = 5, pady = 5, bg="purple") 

button2 = tk.Button(master=frame_bot2, text="Enter",width=25 ,height=5, bg="purple")
'''
#frame_top1.pack()
#frame_bot1.pack()
#frame_top2.pack()
#frame_bot2.pack()

return_stock1 = ""
#return_stock2 = ""
return_weight1 = ""
#return_weight2 = ""

# Create an event handler
def handle_click(event):
    return_stock1 = stock_name1.get()
    #return_stock2 = stock_name2.get()
    return_weight1 = stock_weight1.get()
    #return_weight2 = stock_weight2.get()

#button2.bind("<Button-2>", handle_click)
frame_top1.pack()
frame_mid1.pack()
frame_bot1.pack()

print(return_stock1)
print(return_weight1)

window.mainloop()