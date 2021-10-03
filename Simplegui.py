import os
import PySimpleGUI as sg

def readFile(filePath):
        with open(filePath, "rb") as readF:
            read = readF.read()
            return read

def writeFile(filePath, data):
    with open(filePath, "wb") as readF:
        readF.write(data)

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()],
            [sg.Input("Password")],
            [sg.Button("Encrypt"), sg.Button("Decrypt"), sg.Button("Exit")]] 

window = sg.Window('Get filename example', layout)
while True:

    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
       break

window.close()


