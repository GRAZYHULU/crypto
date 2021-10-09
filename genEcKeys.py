import os
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

    def writeToFile(self, path=None, name="Key"):


        if os.path.isdir(path):
            pathPrivate = os.path.join(path, f"{name}.private")
            pathPublic = os.path.join(path, f"{name}.private")
        else:
            path = os.getcwd()
            pathPrivate = os.path.join(path, f"{name}.private")
            pathPublic = os.path.join(path, f"{name}.private")

            
        if isinstance(self.privateKeyObject, ec.EllipticCurvePrivateKey):
            try:
                pem = self.privateKeyObject.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                    )
                with open (privateKeyPath, "wb") as f:
                    f.write(pem)
            except Exception as e:
                print(e)

        if isinstance(self.publicKeyObject, ec.EllipticCurvePublicKey):
            try:
                pem = self.publicKeyObject.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo            
                    )
                with open (publicKeyPath, "wb") as f:
                    f.write(pem)
            except Exception as e:
                print(e)

