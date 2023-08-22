from other import *


def encode(plain_text, key):
    encoded_text = ""
    plain_text_i = [] #plain_text_i is the char positions of the given text
    key_i = [] #key_i is the char positions of the given key
    encoded_text_i = []
    
    for char in plain_text:
        position = alphabets.index(char) + 1
        plain_text_i.append(position)
    
    for char in key:
        position = alphabets.index(char) + 1
        key_i.append(position)
    
    for i in range(len(plain_text_i)):
        x = plain_text_i[i] + key_i[i]
        if x > alphabets_len:
            x %= alphabets_len
        encoded_text_i.append(x)
    
    for num in encoded_text_i:
        encoded_text += alphabets[num - 1]
    
    print(f"The {choice}d text is : \"{encoded_text}\"")
    
    
def decode(encoded_text, key):
    plain_text = ""
    encoded_text_i = []
    key_i = []
    plain_text_i = []
    
    for char in encoded_text:
        position = alphabets.index(char) + 1
        encoded_text_i.append(position)
    
    for char in key:
        position = alphabets.index(char) + 1
        key_i.append(position)
    
    for i in range(len(encoded_text_i)):
        x = encoded_text_i[i] - key_i[i]
        if x < 1:
            x = x + (alphabets_len * (int((x*(-1)) / alphabets_len)+1))
        plain_text_i.append(x)
    
    for num in plain_text_i:
        plain_text += alphabets[num - 1]
        
    print(f"The {choice}d text is : \"{plain_text}\"")
    
    
clear_display()
    
while True:
    choice = input("Type 'encode' to encrypt\nType 'decode' to decrypt\n==> ")
    if choice == "encode" or choice == "decode":
        text = input("Type your messege : ")
        key = input("Type the key (String) : ")
        
        print(text)
        print(key)
        
        text_len = len(text)
        key_len = len(key)
        
        if key_len > text_len:
            deff_len = key_len - text_len
            key = key[:key_len - deff_len]
            
        elif key_len < text_len:
            deff_len = text_len - key_len
            tmp_key = key
            for i in range(deff_len):
                key += key[i]
        
        print(text)
        print(key)
        
        if choice == "encode":
            encode(text, key)
        else:
            decode(text, key)
        
    else:
        print("\nWrong Selection\nYou need to type 'encode' to encrypt or 'decode' to decrypt\n")

    isContinue = input("Do you want to continue? (Y/N) : ")
    clear_display()
    if isContinue == 'n' or isContinue == 'N': break
    
print("\n\n---------------------------------------------------")
print("\nGoodbye\nThanks for using....")
print("---------------------------------------------------")