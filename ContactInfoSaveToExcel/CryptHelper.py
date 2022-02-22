from CryptICE import IceKey
def generateCryptICE(email):
    notCharacter = [" ", "_", "*", "\\", "<", ">", "~", "'", ",", "|", '"', ".", "{", "}", "(", ")", ";", ":","^","]","["]
    data = bytes(f"{email}", encoding="UTF-8")
    key = bytearray([0x25, 0x6C, 0xC7, 0x0A, 0x00, 0x30, 0x00, 0x5C])

    ice = IceKey(1, key)

    encryptedData = ice.Encrypt(data, True)
    encryptedData = str(encryptedData)
    for data in encryptedData:
        for character in notCharacter:
            if data == character:
                encryptedData=encryptedData.replace(character,"")
    return encryptedData
