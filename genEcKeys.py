import os
from cryptography.hazmat.backends.interfaces import EllipticCurveBackend
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.hazmat.primitives import serialization


class ECKeyGeneration():
    # Luo EC avaimet. Käyrän nimi: SECP192R1

    def genKeys(self):
        self.privateKeyObject = ec.generate_private_key(ec.SECP192R1)
        self.publicKeyObject = self.privateKeyObject.public_key()

    # Näyttää luodut avaimet. Tätä funktiota ei kutsuta missään.
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
    # Tekee luoduista avaimista tiedostoja.
    def writeToFile(self, path=None, name="Key"):


        if os.path.isdir(path):
            pathPrivate = os.path.join(path, f"{name}.private")
            pathPublic = os.path.join(path, f"{name}.public")
        else:
            path = os.getcwd()
            pathPrivate = os.path.join(path, f"{name}.private")
            pathPublic = os.path.join(path, f"{name}.public")

            
        if isinstance(self.privateKeyObject, ec.EllipticCurvePrivateKey):
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

        if isinstance(self.publicKeyObject, ec.EllipticCurvePublicKey):
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

