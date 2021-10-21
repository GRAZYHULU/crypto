import os
from cryptography.hazmat.backends.interfaces import EllipticCurveBackend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class RSAKeyGeneration():

    # Luo RSA avaimet. Yksityisen avaimen koko on 2048bits
    def genKeys(self):
        self.privateKeyObject = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.publicKeyObject = self.privateKeyObject.public_key()

    # Näyttää luodut avaimet. Tätä funktiota ei kutsuta missään.
    def showKeys(self):
        privateKeypem = self.privateKeyObject.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        publicKeyPem = self.publicKeyObject.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo

        )

    # Tekee luoduista avaimista tiedostoja.
    def writeToFile(self, path=None, name="Key"):

        if os.path.isdir(path):
            pathPrivate = os.path.join(path, f"{name}.private")
            pathPublic = os.path.join(path, f"{name}.public")
        else:
            path = os.getcwd()
            pathPrivate = os.path.join(path, f"{name}.private")
            pathPublic = os.path.join(path, f"{name}.public")

        if isinstance(self.privateKeyObject, rsa.RSAPrivateKey):
            # Lukee yksityisen avaimen muistista ja kirjoittaa sen tiedostoon.
            try:
                pem = self.privateKeyObject.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                    )
                with open (pathPrivate, "wb") as f:
                    f.write(pem)
            except Exception as e:
                print(e)

        if isinstance(self.publicKeyObject, rsa.RSAPublicKey):
            # Lukee julkisen avaimen muistista ja kirjoittaa sen tiedostoon.
            try:
                pem = self.publicKeyObject.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo            
                    )
                with open (pathPublic, "wb") as f:
                    f.write(pem)
            except Exception as e:
                print(e)
