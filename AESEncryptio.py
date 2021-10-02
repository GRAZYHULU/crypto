import base64
from cryptography import fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class AESenc():


    def setPassword(self, password):

        bPassword = bytes(password, "utf-16")
        kdf = PBKDF2HMAC(
            hashes.SHA3_256(),
            length=32,
            salt=bPassword,
            iterations=100000,
        )

        self.key = base64.urlsafe_b64encode(kdf.derive(bPassword))
        print(self.key)

    def encryptMessage(self, message):
        fernetObject = Fernet(self.key)
        self.encryptedMessage = fernetObject.encrypt(message)
        return self.encryptedMessage

    def decryptMessage(self, fernetToken):
        fernetObject = Fernet(self.key)
        self.encryptedMessage = fernetObject.decrypt(fernetToken)
        return self.encryptedMessage



def encfile():
    x = AESenc()
    x.setPassword("salasana")
    with open("C:\\Users\\alexh\\Desktop\\code\\pythonKoulu\\lataus.png", "rb") as f:
        file = f.read()
        token = x.encryptMessage(file)
        with open("image.enc", "wb") as fw:
            fw.write(token)
        #print(token)
        #de = x.decryptMessage(token)
        #print(de)



x = AESenc()
x.setPassword("salasana")
with open("C:\\Users\\alexh\\Desktop\\code\\pythonKoulu\\image.enc", "rb") as f:
    file = f.read()
    token = x.decryptMessage(file)
    with open("image.png", "wb") as fw:
        fw.write(token)