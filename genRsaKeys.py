import os
from cryptography.hazmat.backends.interfaces import EllipticCurveBackend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class RSAKeyGeneration():

    def genKeys(self):
        self.privateKeyObject = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.publicKeyObject = self.privateKeyObject.public_key()


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

    def writeToFile(self, path, name):


        if os.path.isdir(path):
            keyPath = os.path.join(path, name)
        else:
            print("Invalid Path")

        if isinstance(self.privateKeyObject, rsa.RSAPrivateKey):
            try:
                pem = self.privateKeyObject.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                    )
                with open ("key.private", "wb") as f:
                    f.write(pem)
            except Exception as e:
                print(e)

        if isinstance(self.publicKeyObject, rsa.RSAPublicKey):
            try:
                pem = self.publicKeyObject.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo            
                    )
                with open ("key.public", "wb") as f:
                    f.write(pem)
            except Exception as e:
                print(e)
