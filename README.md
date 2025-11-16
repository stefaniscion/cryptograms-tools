# cryptograms-tools

*To Crim, the first madmind who shared with me the joy of encrypt and decrypt data and getting lost in the strange poetry of cryptography.*

Cryptograms Tools is a lightweight interface for encrypting and decrypting data using classical ciphers.

## Installation

You can install the project by using:

```bash
poetry install
```

## Usage

You can encrypt or decrypt any data with:

```bash
cryptogram-tools -c [cypher] -k [key] -s [encrypt/decrypt] -i [input]
```

An example:

```bash
cryptograms-tool -c caesar -k 3 -s encrypt -i hello
khoor

cryptograms-tool -c caesar -k 3 -s decrypt -i khoor
hello
```