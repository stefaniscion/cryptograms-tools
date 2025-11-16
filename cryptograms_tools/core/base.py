from abc import ABC, abstractmethod
from typing import Any


class Cipher(ABC):
    """Base interface for all ciphers."""

    name = "base"

    @abstractmethod
    def encrypt(self, data: bytes, key: Any) -> bytes: ...

    @abstractmethod
    def decrypt(self, data: bytes, key: Any) -> bytes: ...

    def normalize_key(self, key: str) -> Any:
        return key
