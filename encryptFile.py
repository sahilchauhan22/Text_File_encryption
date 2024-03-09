def encryp():
    # 1) Read key from file
    key = ''
    with open('SecretKey.key', 'rb') as file:
        key = file.read()

    # 2) Read data from file
    data = ''
    filename=input("\nEnter file name - ")  #'toBeSecret.txt'
    with open(filename, 'rb') as file:
        data = file.read()

    # 3) Encrypt data
    from cryptography.fernet import Fernet

    f = Fernet(key)

    encryptedData = f.encrypt(data)


    # 4) Save the encrypted data into a file
    with open('encrypted_file.txt', 'wb') as file:
        file.write(encryptedData)