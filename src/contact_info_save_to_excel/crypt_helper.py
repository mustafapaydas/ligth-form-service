from CryptICE import IceKey
def generate_crypt_ice(email):
    notCharacter = [" ", "_", "*", "\\", "<", ">", "~", "'", ",", "|", '"', ".", "{", "}", "(", ")", ";", ":","^","]","[","?"]
    data = bytes(f"{email}", encoding="UTF-8")
    key = bytearray([0x25, 0x6C, 0xC7, 0x0A, 0x00, 0x30, 0x00, 0x5C])

    ice = IceKey(1, key)

    encrypted_data = ice.Encrypt(data, True)
    encrypted_data = str(encrypted_data)
    for data in encrypted_data:
        for character in notCharacter:
            if data == character:
                encrypted_data=encrypted_data.replace(character,"")
    return encrypted_data
