from cryptograms_tools.cyphers.caesar import CaesarCipher
from cryptograms_tools.cyphers.vigenere import VigenereCipher
from cryptograms_tools.cyphers.atbash import AtbashCipher
# from cryptograms_tools.cyphers.a1z26 import A1Z26Cipher

cyphers = {
    "caesar": CaesarCipher(),
    "vigenere": VigenereCipher(),
    "atbash": AtbashCipher(),
    # "a1z26": A1Z26Cipher(),
}

available_cyphers = list(cyphers.keys())
