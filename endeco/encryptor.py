'''
This is script is open source
to uses simple encryption to
encrpyt text Files Locally,
without Leaving any Digital Traces.
This script is still in development
stage so use at your own risk.

Discord     :    KAYABA#5276
github  >> https://github.com/SetoKayaba/

'''



#ASCII MAP INITIALIZATION
ascii_map={i: chr(i) for i in range(128)}
ascii_map={value : key for (key, value) in ascii_map.items()}



#Encryption Function
def encrypt(keystring,msg='Message.txt'):


#Opening Msg file and storing the message as a python string variable
    msg=str(msg)
    if (msg=='Message.txt'):
        m_handle=open('Message.txt','r+')
        message=m_handle.read()
    elif '.txt' in msg:
        m_handle=open(msg,'r+')
        message=m_handle.read()
    else:
        message=str(msg)

#Next >>> Breaking Up The Message into Bytes.

    ##Breaking Message into ASCII Character Positions and int equivelent.
    _msg_array=[]
    for char in message:
        if char in ascii_map.keys():
            _msg_array.append(ascii_map[char])

#Next >>> Breaking Up the Key into Bytes.

    ##Conver the Key characters into an intiger array using their ASCII Positions
    _key_array=[]
    for char in keystring:
        if char in ascii_map.keys():
            _key_array.append(ascii_map[char])


#Next >>> Performing XOR Cypher on Message array using the Key array

    ##Performing single char XOR For Each digit in the key Array against the message array
    _encrypted_msg_bytes=_msg_array
    for key_byte in _key_array:
        container=[]
        for msg_byte in  _encrypted_msg_bytes:
            encrypted_byte = msg_byte ^ key_byte
            container.append(encrypted_byte)
        _encrypted_msg_bytes=container


#Next >>> Converting from Bytes to readable Plain Test

    ##Converting bytes to Encrypted Plaintext Result
    encrypted_message=''
    reverse_ascii_map={value : key for (key, value) in ascii_map.items()}
    for char in _encrypted_msg_bytes:
        if char in reverse_ascii_map.keys():
            encrypted_message=encrypted_message+reverse_ascii_map[char]

#Return Function to return Encrypted Message
    return encrypted_message

'''
To call function use encrypt()
The Function takes 2 arguements
The first is the ASCII Keystring 
that will be used to encrypt the
files and the second is the msg
or file to be encrypted this will
return an encrypted file, the same
function and key can then be used
to decrypt the encrypted message.
eg: encrypt(keystring, message)
'''
