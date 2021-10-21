from cryptography.hazmat import primitives
from cryptography.hazmat.primitives import hashes
import base64

class HashingMessage():

    # Luo viestistä tiivisteen. Aika basic.
    def hashMessage(self, message):
        digest = hashes.Hash(hashes.SHA3_256())
        digest.update(message)
        rd = digest.finalize()
        rdb64 = base64.urlsafe_b64encode(rd).decode("utf-8")
        return rdb64 # palauttaa tiivisteen base64 str
