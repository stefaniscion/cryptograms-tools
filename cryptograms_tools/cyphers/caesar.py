from cryptograms_tools.core.base import Cipher
from typing import Any


class CaesarCipher(Cipher):
    name = "caesar"

    def normalize_key(self, key: str) -> int:
        try:
            return int(key) % 26
        except ValueError:
            raise ValueError("Key for caesar must be an integer")

    def encrypt(self, data: bytes, key: Any) -> bytes:
        shift = self.normalize_key(key)
        result = []
        for b in data:
            c = chr(b)
            if "a" <= c <= "z":
                base = ord("a")
                result.append(((ord(c) - base + shift) % 26) + base)
            elif "A" <= c <= "Z":
                base = ord("A")
                result.append(((ord(c) - base + shift) % 26) + base)
            else:
                result.append(b)
        return bytes(result)

    def decrypt(self, data: bytes, key: Any) -> bytes:
        shift = self.normalize_key(key)
        return self.encrypt(data, str(-shift))
