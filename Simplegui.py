import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import TabGroup
from cryptography.hazmat import primitives
from AESEncryption import AESenc
from genEcKeys import ECKeyGeneration
from genRsaKeys import RSAKeyGeneration
from MessageHashing import HashingMessage

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
              [sg.Text(), sg.FileBrowse()],
              [sg.Input('', key='-TEXT-')],
              [sg.Button("HASH")]]

    tab3_layout = [[sg.Text("File key location")],
                [sg.Input(), sg.FolderBrowse()],
                [sg.Text("File name (optional)")],
                [sg.Input()],
                [sg.Radio("EC", "KEYGEN", default=True), sg.Radio("RSA", "KEYGEN")],
                [sg.Button("Generate")]]

    layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout), sg.Tab("Tab 3", tab3_layout)]])],
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

        elif event == "Generate":
            if values[4]:
                # if not values[3]:
                #     path = os.getcwd()
                # else:
                #     path = values[3]
                ecObject = ECKeyGeneration()
                ecObject.genKeys()
                ecObject.writeToFile(values[3], values[6])


            elif values[5]:
                # if not values[3]:
                #     path = os.getcwd()
                # else:
                #     path = values[3]
                rsaObject = RSAKeyGeneration()
                rsaObject.genKeys()
                rsaObject.writeToFile(values[3], values[6])

        elif event == "HASH":
            try:
                with open(values["Browse0"], "rb") as f:
                    bReadFile = f.readline()
                    digest = HashingMessage().hashMessage(bReadFile)
                    window['-TEXT-'].update(digest)

            except Exception as e:
                print(e)

        #print(event, values)
    window.close()


if __name__ == "__main__":
    main()
