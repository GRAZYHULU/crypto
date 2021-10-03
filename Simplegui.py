import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import TabGroup
from AESEncryption import AESenc


def FileEncryption(inputFile, password):
    try:
        if not os.path.isfile(inputFile):
            print("File not found")
        
        if not password:
            print("Give password")

        AESobject = AESenc()
        AESobject.setPassword(password=password)
        readFile = AESobject.readFile(inputFile)
        encryptedMessage = AESobject.encryptMessage(readFile)
        outFile = f"{inputFile}.enc"
        AESobject.writeFile(outFile, encryptedMessage)
        os.remove(inputFile)
    except Exception:
        pass
        


def FileDecryption(inputFile, password):
    try:
        if not os.path.isfile(inputFile):
            print("File not found")
        if not password:
            print("Give password")
            
        AESobject = AESenc()
        AESobject.setPassword(password=password)
        readFile = AESobject.readFile(inputFile)
        encryptedMessage = AESobject.decryptMessage(readFile)
        outFile = inputFile.rsplit(".", 1)[0]
        AESobject.writeFile(outFile, encryptedMessage)
        os.remove(inputFile)
    except Exception:
        pass


def main():
    sg.theme('Dark Blue 3')  # please make your creations colorful

    tab1_layout = [[sg.Text('Filename')],
              [sg.Input(), sg.FileBrowse()],
              [sg.Text("Password")],
              [sg.Input()],
              [sg.Button("Encrypt"), sg.Button("Decrypt")]]

    tab2_layout = [[sg.Text('Message')],
              [sg.Multiline()]]

    layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
            [sg.Button("Exit")]]

    window = sg.Window('Get filename example', layout)
    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == "Encrypt":
            FileEncryption(inputFile=values[0], password=values[1])

        elif event == "Decrypt":
            FileDecryption(inputFile=values[0], password=values[1])

    window.close()


if __name__ == "__main__":
    main()
