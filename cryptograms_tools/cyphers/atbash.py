from typing import Any
from ..core.base import Cipher


class AtbashCipher(Cipher):
    name = "atbash"

    def _transform_char(self, ch: str) -> str:
        if "a" <= ch <= "z":
            return chr(ord("z") - (ord(ch) - ord("a")))
        if "A" <= ch <= "Z":
            return chr(ord("Z") - (ord(ch) - ord("A")))
        return ch

    def encrypt(self, data: bytes, key: Any) -> bytes:
        text = data.decode("utf-8")
        transformed = "".join(self._transform_char(c) for c in text)
        return transformed.encode("utf-8")

    def decrypt(self, data: bytes, key: Any) -> bytes:
        # Atbash è involutivo: cifrare = decifrare
        return self.encrypt(data, key)
