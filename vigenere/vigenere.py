import string

alphabet = string.ascii_uppercase + " "
skiplist = []


def encrypt(text: str, key: str) -> str:
    key = key.upper()
    text = text.upper()

    ekey = key * (len(text)//len(key) + 1)
    cipher = ""

    for i in range(0, len(text)):
        if text[i] in skiplist:
            cipher += text[i]
        else:
            cipher += alphabet[(alphabet.index(text[i]) + alphabet.index(ekey[i])) % len(alphabet)]
    return cipher


def decrypt(cipher: str, key: str) -> str:
    key_inverse = "".join([alphabet[(len(alphabet) + len(alphabet) - alphabet.index(letter)) % len(alphabet)] for letter in key])
    return encrypt(cipher, key_inverse)


enc = encrypt("HALLO WELT WIE GEHTS DIR", "KEY")
dec = decrypt(enc, "KEY")

#print(enc)
#print(dec)

#print(decrypt("NRPOYBVXBBWSJZPHSSSDXHXKCQWIJNUHVDLBQHYD WOQFASMFVFHXAJMB LYAZBVSODIXKAYSFBSAOJZJORJOZQTFNFVIHCESVDOOHAUBBS OTEPFWBTETSHXUXTDSUJOCESMYYBAFMYBOCEHFQCZEKFEXXFHIQTESJPYWDEOZ WSSSDDTKSCPQOTHMYXKXAXQFBSPOHBXVVODXKGNNZBGSASTEHS YVD AQRQTPJNFVFHXERZKOEOXKB DSJIVGLSWVXJXEFVKSXGJMRFWSXQFBSRSVPTJNIVFHSJDHATFNQHLGKSJWLFLFMYOXLGOQFBSROHXATGRVJPLWBTETFNUHVDLBQHYD WOQDTEOMYQOFBCMBBWWQVOKXWBVXVXFMYYWSRSVPOBSNE WSADHXXENQVETA ODXSASJUBILFMYBBS KTEHXAJHBVXAJXBQJODTEONBXQBXFSWQY KNODFVEOJSBZTAXJBBSFHIQTENFVIR SBQAIJQRQAPKNDBQFTNBOPHX JXBZFOMAQOOHAUBOSN", "KRYPTO"))
