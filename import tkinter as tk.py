import tkinter as tk

root = tk.Tk()

#Function for checking numbers in strings
test = 5

def numberchecker(entry_text):
    #I named the variabled placeholder because I suck at naming things
    placeholder = False
    for i in entry_text:
        if placeholder == False:
            if i.isnumeric(): # Checks if the string has a number or not
                placeholder = True
    else:
        return placeholder #Either returns True or False

#Function used for submitting and removing camp details

def submitall(event):
    #leader.config(text = "Leader: " + values[0])

    #Adds text which the user has the written into the GUI
    submit_leader()
    submit_location()
    submit_campers()
    submit_weather()

def removeall(event):

    #Puts text back into its original state
    leader.config(text = "Leader: ")
    location.config(text = "Location: ")
    campers.config(text = "Number Of Campers: ")
    weather.config(text = "Weather: ")

#Individual buttons


def submit_leader(event):

    warning = tk.Label(text="What sort of name has numbers?? Please enter a valid name ._.")

    if (numberchecker(leadervalue.get()) == False):
        leader.config(text = "Leader: " + leadervalue.get())
        warning.config(root, text=" ")
        
    
    if numberchecker(leadervalue.get()):
        warning.pack()
        warning.place(y=325, x=1400)
    

def submit_location(event):

    warning = tk.Label(text="What sort of name has numbers?? Please enter a valid name ._.")
    
    if numberchecker(locationvalue.get()) == False:
        location.config(text = "Location: " + locationvalue.get())

    if numberchecker(locationvalue.get()):
        warning.pack()
        warning.place(y=425, x=1400)

def submit_campers(event):

    warning = tk.Label(text="What sort of name has numbers?? Please enter a valid name ._.")

    if numberchecker(campersvalue.get()) == False:
        campers.config(text = "Number Of Campers: " + campersvalue.get())

    if numberchecker(campersvalue.get()) == False:
        warning.pack()
        warning.place(y=325, x=1400)

def submit_weather(event):

    warning = tk.Label(text="What sort of name has numbers?? Please enter a valid name ._.")
    
    if numberchecker(weathervalue.get()) == False:
        weather.config(text = "Weather: " + weathervalue.get())

    if numberchecker(weathervalue.get()) == False:
        warning.pack()
        warning.place(y=325, x=1400)

def remove_leader(event):
    leader.config(text = "Leader: ")

def remove_location(event):
    location.config(text = "Location: ")

def remove_campers(event):
    campers.config(text = "Number Of Campers: ")

def remove_weather(event):
    weather.config(text = "Weather: ")
    
#Labelling the camp details

leader = tk.Label(root, text = "Leader: ")
leader.pack()
leader.place(y = 300, x = 200)
location = tk.Label(root, text = "Location: ")
location.pack()
location.place(y = 400, x = 200)
campers = tk.Label(root, text = "Number Of Campers: ")
campers.pack()
campers.place(y = 500, x = 200)
weather = tk.Label(root, text = "Weather:  ")
weather.pack()
weather.place(y = 600, x = 200)

# User input
# Lets the camp leader add details
leadervalue = tk.Entry(root)
leadervalue.pack()
leadervalue.place(y = 300, x = 1400)
locationvalue = tk.Entry(root)
locationvalue.pack()
locationvalue.place(y = 400, x = 1400)
campersvalue = tk.Entry(root)
campersvalue.pack()
campersvalue.place(y = 500, x = 1400)
weathervalue = tk.Entry(root)
weathervalue.pack()
weathervalue.place(y = 600, x = 1400)

# Buttons 
# Allows the user to submit or remove details

submit_all = tk.Button(root, text = "Add All")
submit_all.bind("<ButtonPress>", submitall)
submit_all.pack()
submit_all.place(y = 700, x = 1400)

remove_all = tk.Button(root, text = "Remove All")
remove_all.bind("<ButtonPress>", removeall)
remove_all.pack()
remove_all.place(y=700, x=1475)

submitleader = tk.Button(root, text = "Add")
submitleader.bind("<ButtonPress>", submit_leader)
submitleader.pack()
submitleader.place(y= 300, x=1550)

submitlocation = tk.Button(root, text = "Add")
submitlocation.bind("<ButtonPress>", submit_location)
submitlocation.pack()
submitlocation.place(y=400, x=1550)

submitcampers = tk.Button(root, text = "Add")
submitcampers.bind("<ButtonPress>", submit_campers)
submitcampers.pack()
submitcampers.place(y=500, x=1550)

submitweather = tk.Button(root, text = "Add")
submitweather.bind("<ButtonPress>", submit_weather)
submitweather.pack()
submitweather.place(y=600, x=1550)



root.geometry("1920x1080")
root.title("Test")
root.mainloop()