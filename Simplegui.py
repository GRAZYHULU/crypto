import os
from tkinter.constants import E
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import TabGroup
from cryptography import fernet
from cryptography.hazmat import primitives
from AESEncryption import AESenc
from genEcKeys import ECKeyGeneration
from genRsaKeys import RSAKeyGeneration
from MessageHashing import HashingMessage


# FileEncryption hoitaa tiedoston salauksen
def FileEncryption(inputFile, password):
    # Tarkistaa löytyykö salasana ja tiedosto
    try:
        if not os.path.isfile(inputFile):
            print("File not found")
        
        if not password:
            print("Give password")

        AESobject = AESenc()
        AESobject.setPassword(password=password) # Asettaa salasanan
        readFile = AESobject.readFile(inputFile) 
        encryptedMessage = AESobject.encryptMessage(readFile) # Luo tiedostosta salataun version. Luo base64 string.
        outFile = f"{inputFile}.enc" # Luodaan uusi nimi tiedostolle
        AESobject.writeFile(outFile, encryptedMessage)
        os.remove(inputFile) # Poistetaan salaamaton tiedosto.
    except Exception:
        pass
        

# FileDecryption hoitaa tiedoston pukamisen.
# Toimii kuin FileEncryption
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
    sg.theme('Dark Blue 3')
# Luodaan tab lauoutit
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

    global window
    window = sg.Window('Get filename example', layout)
    while True:
        # Hoidetaan erinlaiset tapahtumat
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
            # Salaus/purkaminen
        elif event == "Encrypt":
            FileEncryption(inputFile=values[0], password=values[1])

        elif event == "Decrypt":
            FileDecryption(inputFile=values[0], password=values[1])
        # RSA ja Elliptical curve yksityisen ja julkisen avaimen luominen
        elif event == "Generate":
            if values[4]:
                ecObject = ECKeyGeneration()
                ecObject.genKeys()
                ecObject.writeToFile(values["Browse1"], values[3])


            elif values[5]:
                rsaObject = RSAKeyGeneration()
                rsaObject.genKeys()
                rsaObject.writeToFile(values["Browse1"], values[3])
        
        # Tiedoston tiiviste
        elif event == "HASH":
            try:
                with open(values["Browse0"], "rb") as f:
                    bReadFile = f.readline()
                    digest = HashingMessage().hashMessage(bReadFile)
                    window['-TEXT-'].update(digest)

            except Exception as e:
                print(e)

        # print(event, values) debug
    window.close()


if __name__ == "__main__":
    main()
