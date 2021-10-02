from cryptography.hazmat.backends.interfaces import EllipticCurveBackend
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.hazmat.primitives import serialization

class ECKeyGeneration():

    def genKeys(self):
        self.privateKeyObject = ec.generate_private_key(ec.SECP192R1)
        self.publicKeyObject = self.privateKeyObject.public_key()


    def showKeys(self):
        privateKeypem = self.privateKeyObject.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        publicKeyPem = self.publicKeyObject.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo

        )
        print(privateKeypem)
        print(publicKeyPem)

    def writeToFile(self):

        if isinstance(self.privateKeyObject, ec.EllipticCurvePrivateKey):
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

        if isinstance(self.publicKeyObject, ec.EllipticCurvePublicKey):
            try:
                pem = self.publicKeyObject.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo            
                    )
                with open ("key.public", "wb") as f:
                    f.write(pem)
            except Exception as e:
                print(e)

key = ECKeyGeneration()
key.genKeys()
key.showKeys()
key.writeToFile()