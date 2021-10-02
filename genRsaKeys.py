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
        print(privateKeypem)
        print(publicKeyPem)

    def writeToFile(self):

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

key = RSAKeyGeneration()
key.genKeys()
key.showKeys()
key.writeToFile()