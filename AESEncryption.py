import base64
from cryptography import fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class AESenc():


    def setPassword(self, password):
        # Asetetaan salasana, joka käy cryptography kirjastolle
        bPassword = bytes(password, "utf-16")
        kdf = PBKDF2HMAC(
            hashes.SHA3_256(),
            length=32,
            salt=bPassword, # Käytetään salasanaa suolana. Ei saisi tehdä näin mutta olen laiska miettimään mitään parempaa.
            iterations=100000,
        )

        self.key = base64.urlsafe_b64encode(kdf.derive(bPassword))
    
    # Salataan tiedosto.
    def encryptMessage(self, message):
        fernetObject = Fernet(self.key)
        self.encryptedMessage = fernetObject.encrypt(message)
        return self.encryptedMessage # Palauttaa fernetToken, joka on base64 string

    # Purkaa tiedoston käyttäen fernetToken.
    def decryptMessage(self, fernetToken):
        fernetObject = Fernet(self.key)
        self.encryptedMessage = fernetObject.decrypt(fernetToken)
        return self.encryptedMessage

    def readFile(self, filePath):
        with open(filePath, "rb") as readF:
            read = readF.read()
            return read

    def writeFile(self, filePath, data):
        with open(filePath, "wb") as readF:
            readF.write(data)

