# -*- coding: utf-8 -*-
"""

Swiss Army Cryptographic Toolset
Rushi Patel
Yash Patel 
Jeet Desai
Moaz Khan

"""

from Crypto import Random
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256
from cryptography.hazmat.primitives import keywrap

def DES3CIPHER(): 
    #ask user for message to encrypt
    print("\n -- 3DES -- \nIt is a symmetric-key block cipher. It performs encryption and decryption"
          " of fixed data sized blocks (multiple of 8 characters (8 bytes).",
          " 3DES has the same functionality as DES, however 3DES applies the DES cipher 3 times")
    print("\nNote: Input strings must be a multiple of 8 characters in length!")
    print("Enter a message you would like to encrypt: ")
    message = input() #store user inpunt in a string variable 
 
    #checking whether the length of user input is multiple of 8. 
    #To check if its multiple of 8, taking the modulo of the input length by 8.
    #If the remainder is 0, do encryption/decryption of user's message. 
    #If remainder is not 0, continue asking the user for input in appropriate message length
    while len(message) % 8 != 0:
        print("\nInput strings must be a multiple of 8 characters in length!")
        print("Please enter your message again: ")
        message = input()

    #define key in 16 bytes
    key = 'Sixteen byte key'

    #define initialization vector
    iv = Random.new().read(DES3.block_size) #DES3.block_size==8
 
    #encrypt message
    cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
    encrypted_text = cipher_encrypt.encrypt(message) 


    print("\nMessage length is appropriate")
    
    print("\nEncrypted Text: ", encrypted_text)
    print("\nEncryption Process: ")
    print("Triple DES takes 3 keys for encryption. Each key is 64 bits long," 
          " however 8 bits from the key are striped and saved for redundancy."
          " After taking out the bits, the key becomes 168 bits."
          " The key from the user is broken down into three keys and padded if the bits" 
          " don't make up to a valid key size.")
    print("1) First encrypt the plaintext blocks using single DES with key K1.")
    print("2) Now decrypt the output of step 1 using single DES with key K2.")
    print("3) Finally, encrypt the output of step 2 using single DES with key K3.")
    print("4) The output of step 3 is the ciphertext.")

    #Decrypt message
    cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) 
    Decrypted_text = cipher_decrypt.decrypt(encrypted_text) 

    print("\nDecrypted Text: ", Decrypted_text)
    print("\nDecryption Process: ")
    print("1) Decryption of a ciphertext is in reverse process.") 
    print("2) User first decrypt using K3, then encrypt with K2, and finally decrypt with K1.")
    
    print("\nWould you like to know the parameters that were used in encryption/decryption process? yes or no")
    decision = input()
    
    if (decision == "yes"):
        print("\nKey: ", key)
        print("\nRandomly Generated IV: ", iv)
        print("IV is used as an initial n-bit input block for the Ouput Feedback Mode")
        print("\nMode of Operation used: Output Feedback Mode (OFB)")
        print("The mode works as such, initially it uses an IV as the input for encryption," 
              " the output from the encryption function is used again in the next round as" 
              " input for encrypting the next block of plaintext.")
    elif (decision == "no"):
        exit
    
def AESCIPHER():
    #ask user for message to encrypt
    print("\n -- AES Chosen -- \nAES is a symmetric encryption algorithm. It’s operation works as such," 
          " replacing inputs and shuffling bits around." 
          " AES performs its computations based on rounds. The rounds in AES depends on the length of the key." 
          "\n(10 rounds - 128-bit keys, 12 rounds - 192-bit keys, 14 rounds - 256-bit keys)" 
          " Each round uses a different 128-bit round key.")
    print("\nNote: Input strings must be a multiple of 16 characters in length!")
    print("Enter a message you would like to encrypt: ")
    message = input() #store user inpunt in a string variable 

    #checking whether the length of user input is multiple of 16. 
    #To check if its multiple of 8, taking the modulo of the input length by 16.
    #If the remainder is 0, do encryption/decryption of user's message. 
    #If remainder is not 0, continue asking the user for input in appropriate message length 
    while len(message) % 16 != 0:
        print("\nInput strings must be a multiple of 16 characters in length!")
        print("Please enter your message again: ")
        message = input()

    #define key in 16 bytes
    key = 'Sixteen byte key'

    #define initialization vector
    iv = Random.new().read(AES.block_size) 

    #encrypt message
    cipher_encrypt = AES.new(key, AES.MODE_CFB, iv)
    encrypted_text = cipher_encrypt.encrypt(message) 


    print("\nMessage length is appropriate")
    
    print("\nEncrypted Text: ", encrypted_text) 
    print("\nEncryption Process: ")
    print("Each round has 4 sub processes: ")
    print("1) Byte substitution - 16 byte input is substituted with values from a fixed table (S-box)." 
             " The result is stored in a 4 by 4 matrix")
    print("2) Shift Rows - each of the four rows from the byte substitution is shifted to the left." 
          " Any entries from the matrix that fall off are inserted again to the right side of the row. ")
    print("   First row is not shifted")    
    print("   Second row is shifted to the left by one position")
    print("   Third row is shifted to the left by two positions")
    print("   Fourth row is shifted to the left by three positions")
    print("3) Mix Columns - each column of four bytes are transformed using a mathematical function." 
         " This takes a column as one input and outputs a different different column with different bytes." 
         " At the end it results in a new 4 by 4 matrix. This step is not done in the last round")
    print("4) Add round key - the 16 bytes of the matrix are considered as 128 bits and are XORed to" 
         " the 128 bits of the round key." 
         " The resulted 128 bits are used as 16 bytes in the next round." 
         " In the last round the output is the cipher text.")
    
    
    #Decrypt message
    cipher_decrypt = AES.new(key, AES.MODE_CFB, iv) 
    Decrypted_text = cipher_decrypt.decrypt(encrypted_text) 

    print("\nDecrypted Text: ", Decrypted_text)
    print("\nDecryption Process: ")
    print("Each round has four sub processes. Does decryption in reverse order of encryption process")
    print("1) Add round key")
    print("2) Mix columns")
    print("3) Shift rows")
    print("4) Byte substitution")
    
    print("\nWould you like to know the parameters that were used in encryption/decryption process? yes or no")
    decision = input()
    
    if (decision == "yes"):
        print("\nKey: ", key)
        print("\nRandomly Generated IV: ", iv)
        print("IV is used as an initial n-bit input block for the Cipher Feedback Mode (CFB)")
        print("\nMode of Operation used: Cipher Feedback Mode (CFB)")
        print("The mode works as such, initially an IV is used for encrypting a block of plaintext," 
              " then the output is XORed with the plaintext. The result of the XOR is fed into the next" 
              " round as the 'IV' for encrypting the next block of plaintext.") 
        print("")
    elif (decision == "no"):
        exit

#----------------------------------------------------------RSA--------------------------------------

def RSA():

    print("=========================")
    print("Welcome to RSA encryption")
    print("=========================")
    print(" ")
    print("Key_terms: ")
    print("---> public exponent = e ")
    print("---> RSA modulus = n ")
    print("---> private exponent = d ")
    print("---> plain text = M ")
    print("---> cipher text = C ")
    print(" ")
    print(" ")
    e = 257
    n = 2048

    plain_text = str(input ("Please Enter the plaintext 'M' Alice wishes to send: " ))
       
    print("---> Generating Alice's private and public keys... ")
    print("---> Generating Bob's private and public keys... ")
    alice_private_key = rsa.generate_private_key(e,n,backend=default_backend())
    alice_public_key = alice_private_key.public_key()
    print(" ")
    selection1 = input("do you wish to know how to generate  the n value?: 'y' or 'n' ?")
    if(selection1 =='y'):
        print("the n value(RSA Modulus) is the product of 2 prime numbers")
        print("---> n = p*q = ",n)
    elif(selection1=='n'):
            print (" ")
    else: print("invalid operation!")
    
    selection2 = input("do you wish to know how to generate the e value?: 'y' or 'n' ?")
    if(selection2 =='y'):
        print("e must be smaller than the toitent of n and is coprime to n")
        print("--->e= ", e)
    elif(selection2=='n'):
            print (" ")
    else: print("invalid operation!")
    

    bob_private_key = rsa.generate_private_key(e,n,backend=default_backend())
    bob_public_key = alice_private_key.public_key()

    #Encodes the plain text
    plain_text_encoded= (plain_text).encode("utf-8")


#gets the ciphertext with a padding using mask generation function (MGF)
#for any given input, the desired output length will be the same
    cipher_text = alice_public_key.encrypt(plain_text_encoded,padding.OAEP
                                           (mgf=padding.MGF1(algorithm=hashes.SHA512()),algorithm=hashes.SHA512(),label=None))

    print("generating cipher text...")
    print(" ")
    print("the function used to encrypt = C = (M^e % n)")
    print(" ")
    print ("The Ciphertext 'C' that Bob receieves is " , cipher_text)
    selection3 = input ("would you like to know about signing process:'y' or 'n'? ")
    if (selection3== 'y'):
        print(" in RSA, a private key is used to sign a message")
        print("---> this allows anyone with the public key to verify ")
        print("that the message was from the correct private key holder ")
        print("Alice signed the message with her signature")
        print("---> this signature had a hash of SHA512")
        print("---> the padding OAEP is used to get a desired length of output ")
        print("---> regardless of the input used for bytesize  ")
    elif(selection3=='n'):
        print(" ")
    else:print("invalid operation!")

    print (" " )
#decodes the cipher text from its base 64
    decoded_cipher_text = base64.b64decode(
    cipher_text) if not isinstance(cipher_text, bytes) else cipher_text
    plain_text2 = alice_private_key.decrypt(decoded_cipher_text,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()),algorithm=hashes.SHA512(),label=None)
        )
# signs the plain text in order for the correct user to receieve the information using the same hash type and padding
    signature_RSA = alice_private_key.sign(
            plain_text_encoded,
            padding.PSS(
                    mgf=padding.MGF1(hashes.SHA512()),
                    salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA512()
                    )

# Bob has to verify that the message is actually from Alice. only he can decrypt the message and verify the signature
    bob_public_key.verify(
    signature_RSA,
    plain_text_encoded,
    padding.PSS(
            mgf=padding.MGF1(hashes.SHA512()),
            salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA512()
            )
    selection4= input("Do you wish to see the signature? 'y' or 'n'? ")
    if(selection4 == 'y'):
        print("The Signature used for the RSA was: ", signature_RSA)
    elif(selection4=='n'):
        print (" ")
    else: print("invalid operation!")
    
    encrypted_message_receieved = plain_text2
    print(" ")
    print(" ")
    print("Bob encrypts the message, verifys the signature successfully and securely gets the original plain text: ",encrypted_message_receieved )
    print("===================================")
    print("Exiting RSA_ENCRYPTION tutorial...")

#------------------------------------------------HMAC---------------------------------------

#12345678901234567890123456789012
#bce392c515c14a62106335639038deebd22e757504edbd2756924c5515c869a9

#Function which creates hash code of the message with the private key using SHA256 algorithm 
def sender(key, message):
    h = HMAC.new(key, message, digestmod=SHA256)
    finalHash = h.hexdigest()
    print("\nYour message:", message)
    print("\nYour hash is", finalHash)

#Function which creates hash code of the message with the private key using SHA256 algorithm 
#This function also checks whether hashes match or not
def receiver(key,message, hashString):
    h1 = HMAC.new(key, message, digestmod=SHA256)
    finalHash = h1.hexdigest()
    compare = hashString   
    if(compare == finalHash):
        print("\nYour hash code and sender's hash matches! \n")
        print("Sender's Hash: " , compare)
        print("Your hash: " , finalHash)

    else:
        print("\nHashes do not match\n")
        print("Please make sure you are using the shared private key which is shared between you and the sender")
        print("If you are using the same private then the message or the hash have been altered\n")
        print("Sender's Hash: " , compare)
        print("Your hash: " , finalHash)
    
    
    
def HMAC1():
    print("----------------Hash Message Authentication Code (HMAC)----------------\n")
    #Asking user whether they are a sender or a receiver
    ask = input("Are you a sender(1) or receiver(2)? \n")
    
    while((ask != '1') & (ask != '2')):
        ask = input("Please enter 1 for sender or 2 for receiver \n")
        
    #If user is a sender then call the sender function which does hashing 
    if(ask == '1'):
        
        #Asking for a private key 
        userInput = input("\nEnter a key whose length is 32 characters: ")
         
        #If the key is not 32 characters long then ask the user to enter a key which is 32 characters long 
        while((len(userInput)  !=  32)):
            userInput = input("\nEnter a key whose length is 32 characters: ")
        
        #Convert the user input into a string 
        string = str(userInput)
        
        #converting strings to bytes
        key = string.encode('utf-8')
        
        #Asking user to enter a message to hash 
        messageInput = input("\nEnter a message to hash:")
        
        #Convert the user input into a string
        words = str(messageInput)
        
        #converting strings to bytes
        message = words.encode('utf-8')
        
        #Calling the function of sender
        sender(key, message)
        
        #Explaining the process which takes place on the sender's side 
        print("\n---------------------Sender's Process--------------------------")
        print("\nWhat just happened?")
        print("\nSender has a message which he/she wants to send it to someone")
        print("\nBut what is the guarantee that this message will not be altered on it's way to the receiver")
        print("\nHow would receiver know that this message was not changed or altered on its way?")
        print("\nThis problem questions the authenticity of the message")
        print("\nTo prevent this problem sender will use that message and a private key which is only shared between him and the receiver")
        print("\nSender will take this message and hash it with the private Key using SHA256 algorithm")
        print("\nSender will then append the original message with the hash created using the private key and send it to the receiver")
        print("\n--------------------END------------------------")
    
    #If user is a sender then call the sender function which does hashing 
    if(ask == '2'):
        
        #Asking for a private key 
        userInput = input("\nEnter a key which is shared between sender and yourself (Must be exactly 32 characters long): \n")
        
        #If the key is not 32 characters long then ask the user to enter a key which is 32 characters long 
        while(len(userInput) != 32):
            userInput = input("\n Enter a key whose length is 32 characters: ")
        
        #Convert the user input into a string 
        string = str(userInput)
        
        #converting strings to bytes
        key = string.encode('utf-8')
        
        #Asking user to enter the message they received  
        messageInput = input("\nEnter a message to hash: ")
        
        #Convert the user input into a string
        words = str(messageInput)
        
        #converting strings to bytes
        message = words.encode('utf-8')
        
        #Asking receiver to enter the hash code they received with the message
        hashInput = input("\nEnter the hash code you received with the message: ")
        
        #converting the hash code into a string 
        hashString = str(hashInput)
       
        #Calling a function to check the integrity of the message
        receiver(key,message, hashString)
        
        #Explaining the process which takes place on the receiver's end
        print("\n-------------------------Receiver's Process------------------------")
        print("\nWhat just happened?")
        print("\nReceiver receives a message from the sender with a hash attached to it")
        print("\nBut what is the guarantee that this message was not be altered on it's way to the receiver")
        print("\nHow would receiver know that this message was unchanged or altered on its way?")
        print("\nThis problem questions the authenticity of the message")
        print("\nTo prevent this problem receiver will use that message and a private key which is only shared between him and the sender")
        print("\Receiver will take this message and hash it with the private Key using SHA256 algorithm")
        print("\nReceiver will then compare the hash he/she received with the message sent my sender ")
        print("\n---------------------------END-------------------------------")

def AESKeyWrap():
    print("\n\n\n===========================================")
    print("Welcome to Key Wrap (KW) Mode of Operation")
    print("===========================================")
    print(" ")
    
    print("Key wrapping and un-wrapping requires 3 parameters in order to function correctly:\n")
    print("\n1) The key encrytion key or 'the wrapping key', which must be of 16, 24 or 32 bytes in value in order for AES to function.")
    print("2) The key that is to be wrapped 'key to wrap', this is also of 16, 24 or 32 bytes in value.")
    print("3) Finally, the wrapped key, this is the encrypted value of the key which is also used in the unwrapping process.")
    
    print("\nFor simplicity's sake, we have already defined a value for the key encryption key to be b'1234567890123456'.")
    
    wrappingKey = b'1234567890123456'# Must be 16,24,32 bytes
    userYN = input("Do you wish to change this value?(y/n):")
    if(userYN == "y"):
        wrappingKey = input("Enter a new value for the wrapping key(MUST BE OF 16, 24 OR 32 BYTES):")
        wrappingKey = wrappingKey.encode('utf-8')
        while (True):
            if((len(wrappingKey) % 8 == 0) and len(wrappingKey) >= 16 and len(wrappingKey) <= 32):
                break
            print("The wrapping key must be a valid AES key length")
            wrappingKey = input("Enter a new value for the wrapping key.(MUST BE OF 16, 24 OR 32 BYTES):")
            wrappingKey = wrappingKey.encode('utf-8')
    
    print("\nAnd again, for simplicity's sake we've defined the key that is to be wrapped to be b'wow-this-is-fun!'")
    
    keyToWrap = b'wow-this-is-fun!' # Must be 16,24,32 bytes
    
    userYN = input("Do you wish to change this value?(y/n):")
    if(userYN == "y"):
        keyToWrap = input("Enter a new value for key to be wrapped.(MUST BE OF 16, 24 OR 32 BYTES):")
        keyToWrap = keyToWrap.encode('utf-8')
        while (True):
            if((len(keyToWrap) % 8 == 0) and len(keyToWrap) >= 16 and len(keyToWrap) <= 32):
                break
            print("The wrapping key must be a valid AES key length")
            keyToWrap = input("Enter a new value for the wrapping key(MUST BE OF 16, 24 OR 32 BYTES):")
            keyToWrap = keyToWrap.encode('utf-8')
            
    wrappedKey = keywrap.aes_key_wrap(wrappingKey, keyToWrap, backend=default_backend())
    
    print("\nThe encrypted value for the wrapped key is:", wrappedKey)
    input("Press Enter to see how we computed the wrapped key value...")
    
    print("\nWhat just happened?")
    print("-------------------------------------")
    print("\nSo to go over how we got the encrypted value, lets take a moment to recall all the components involved.")
    print("First off, when the program asked about setting a key encryption key, this key value is what's going to remain constant in both wrapping and un-wrapping the new key (Defaulted to b'1234567890123456' if no input).")
    print("The 'new key' is essentially the symmetric key we are wrapping so that we have a safe transfer of keys from the sender side to the receiver.")
    print("This 'new key', we will dub it as the 'keyToWrap' value and this is the second value the program asked for your input. It was defaulted to b'wow-this-is-fun!' if there was no input.")
    print("\nSo now we have the following: ")
    print("1) Key Encryption Key 'wrappinKey' = b'1234567890123456' or whatever you inputted.")
    print("2) New Symmetric Key 'keyToWrap' = b'wow-this-is-fun!' or whatever you inputted.")
    print("\nFinally, the program used the 'wrappingKey' to encrypt the 'keyToWrap' and that's how we got our 'WrappedKey' value.")
    print("To clarify, the wrapped key is:", wrappedKey)
    
    input("Press Enter to see how we can return back to our 'keyToWrap' value...")
    print("\nWhat about un-wrapping?")
    print("-------------------------------------")
    print("\nNow if we wanted to get back our 'keyToWrap' which would be the symmetric key we wanted to exchange, it is actually quite simple given the parameters and values.")
    print("This is most helpful when trying to decrypt the wrapped key as the receiver of the new symmetric key.")
    print("\nJust like what we stated above when figuring out our wrapped key value, lets see what we have:")
    print("1) Key Encrytion key 'wrappingKey' = b'1234567890123456' or whatever it was you inputted. (REMEMBER THIS PARAMETER REMAINS CONSTANT FOR BOTH OPERATIONS)")
    print("2) 'wrappedKey' = ", wrappedKey)
    print("\nJust like before, using the two values and then decrypting using AES, we get back our 'keyToWrap' value")
    c = keywrap.aes_key_unwrap(wrappingKey, wrappedKey, backend=default_backend())
    
    print("After decrypting we end up with the symmetric key that was to be exchanged between sender and receiver:", c)

#MAIN DRIVER-----------------------------------------------------------

print("=====================================================")
print("Welcome to the Swiss Army Cryptographic Toolset")
print("=====================================================")
print("\nHere are five cryptographic certificates you can learn more about: ")
print("1) 3DES - Choose 1 to perform 3DES")
print("2) AES - Choose 2 to perform AES")
print("3) RSA - Choose 3 to perform RSA")
print("4) HMAC - Choose 4 to perform HMAC")
print("5) AES Key wrapper - Choose 5 to perform AES Key Wrapper")


while(True):
    answer = input("Enter your choice: ")
    if(answer == "1"):
        DES3CIPHER()
        break
    elif(answer == "2"):
        AESCIPHER()
        break
    elif(answer == "3"):
        RSA()
        break
    elif(answer == "4"):
        HMAC1()
        break
    elif(answer == "5"):
        AESKeyWrap()
        break
    else:
        print("Invalid Input! Please try again.")
    
