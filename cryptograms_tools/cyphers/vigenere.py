from typing import Any, List
from ..core.base import Cipher


class VigenereCipher(Cipher):
    name = "vigenere"

    def normalize_key(self, key: str) -> List[int]:
        if not isinstance(key, str):
            raise ValueError("Key for vigenere must be a string")

        letters = [c.lower() for c in key if c.isalpha()]
        if not letters:
            raise ValueError(
                "Key for vigenere must contain at least one alphabetic character"
            )

        shifts = [ord(c) - ord("a") for c in letters]  # 0..25
        return shifts

    def _crypt(self, text: str, key: str, decrypt: bool = False) -> str:
        shifts = self.normalize_key(key)
        out_chars = []
        j = 0  # indice nella chiave

        for ch in text:
            if ch.isalpha():
                shift = shifts[j % len(shifts)]
                if decrypt:
                    shift = -shift

                if "a" <= ch <= "z":
                    base = ord("a")
                    new_code = (ord(ch) - base + shift) % 26 + base
                    out_chars.append(chr(new_code))
                elif "A" <= ch <= "Z":
                    base = ord("A")
                    new_code = (ord(ch) - base + shift) % 26 + base
                    out_chars.append(chr(new_code))
                else:
                    out_chars.append(ch)

                j += 1  # avanza nella chiave solo per le lettere
            else:
                out_chars.append(ch)

        return "".join(out_chars)

    def encrypt(self, data: bytes, key: Any) -> bytes:
        text = data.decode("utf-8")
        result = self._crypt(text, str(key), decrypt=False)
        return result.encode("utf-8")

    def decrypt(self, data: bytes, key: Any) -> bytes:
        text = data.decode("utf-8")
        result = self._crypt(text, str(key), decrypt=True)
        return result.encode("utf-8")
