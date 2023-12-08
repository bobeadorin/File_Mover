import os
import tkinter as tk


source = r"C:\Users\bobea\Desktop"
destination = r"C:\Users\bobea\Desktop\PDF" + "\\"
musicDestination = r"C:\Users\bobea\Desktop\songs" + "\\"


def fileMove(firstLocation, destinationInput, fileType):
    output = ''
    try:
        for path, dir, files in os.walk(firstLocation):
            for file in files:
                if fileType in file:
                    os.rename(path + '\\' + file,
                              destinationInput + "\\" + file)
        output = 'succes'

    except FileNotFoundError:
        output = 'failed'
    return output


def button_click():

    firstLocation = filesLocation.get()
    destinationInput = destinationFolder.get()
    fileType = selected_choice.get()
    outputText = fileMove(firstLocation, destinationInput, fileType)
    text.config(text=outputText)


root = tk.Tk()

root.grid()

root.title('Move Files')
root.geometry('300x200')

fileLocationName = tk.Label(text='File Location Path')
fileLocationName.grid(row=1, column=1)

filesLocation = tk.Entry(root)
filesLocation.grid(row=1, column=2)

destinationLabel = tk.Label(text='Destination path')
destinationLabel.grid(row=2, column=1)


destinationFolder = tk.Entry(root)
destinationFolder.grid(row=2, column=2)

button = tk.Button(root, text='move', command=button_click)
button.grid(row=4, column=2)


choices = [".pdf", ".wav",  ".jpeg",".PNG"]
selected_choice = tk.StringVar()
selected_choice.set(choices[0])

dropdownLabel = tk.Label(text='select file terminal')
dropdownLabel.grid(row=3, column=1)
dropdown = tk.OptionMenu(root, selected_choice, *choices)
dropdown.grid(row=3, column=2)


text = tk.Label(text='')
text.grid(row=5, column=2)

root.mainloop()
