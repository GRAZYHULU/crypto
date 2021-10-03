import os
import PySimpleGUI as sg
from AESEncryption import AESenc


def FileEncryption(inputFile, password):
    AESobject = AESenc()
    AESobject.setPassword(password=password)
    readFile = AESobject.readFile(inputFile)
    encryptedMessage = AESobject.encryptMessage(readFile)
    outFile = f"{inputFile}.enc"
    AESobject.writeFile(outFile, encryptedMessage)
    os.remove(inputFile)


def FileDecryption(inputFile, password):
    AESobject = AESenc()
    AESobject.setPassword(password=password)
    readFile = AESobject.readFile(inputFile)
    encryptedMessage = AESobject.decryptMessage(readFile)
    outFile = inputFile.rsplit(".", 1)[0]
    AESobject.writeFile(outFile, encryptedMessage)
    os.remove(inputFile)


def main():
    sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [[sg.Text('Filename')],
              [sg.Input(), sg.FileBrowse()],
              [sg.Text("Password")],
              [sg.Input()],
              [sg.Button("Encrypt"), sg.Button("Decrypt"), sg.Button("Exit")]]

    window = sg.Window('Get filename example', layout)
    while True:

        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == "Encrypt":
            FileEncryption(inputFile=values[0], password=values[1])

        elif event == "Decrypt":
            FileDecryption(inputFile=values[0], password=values[1])

    window.close()


if __name__ == "__main__":
    main()
