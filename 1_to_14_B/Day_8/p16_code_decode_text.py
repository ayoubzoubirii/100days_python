alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
text_list = list(text)
print(text_list)


new_position = []
ecode = []
ecode1 = []
word = ''

def encode(text,shift) :
    while len(new_position) != len(text_list) :
        for n in range(len(text_list)) :
            for x in range(len(alphabet)) :
                if text[n] == alphabet[x] :
                    new_position.append(x+shift)
    print(new_position)
    for n in range(0,len(new_position)) :
        for x in range(0,len(alphabet)+26):
            if new_position[n] == x :
                z = x - 26
                print(new_position[n])
                print(x)
                print(z)
                ecode.append(z)
                # print(x)
                
    print(ecode)
    for n in range(len(ecode)) :
        for x in range(len(alphabet)+26):
            if ecode[n] == x-26 :
                ecode1.append(alphabet[x-26])
                # print(x)
    print(ecode1)
    word = ''.join(ecode1) 
    print(word)
       
def decode(text,shift) :
    while len(new_position) != len(text_list) :
        for n in range(len(text_list)) :
            for x in range(len(alphabet)) :
                if text[n] == alphabet[x] :
                    new_position.append(x-shift)
    print(new_position)
    for n in range(0,len(new_position)) :
        for x in range(0,len(alphabet)+26):
            if new_position[n] == x :
                z = x - 26
                print(new_position[n])
                print(x)
                print(z)
                ecode.append(z)
                # print(x)
                
    print(ecode)
    for n in range(len(ecode)) :
        for x in range(len(alphabet)+26):
            if ecode[n] == x-26 :
                ecode1.append(alphabet[x-26])
                # print(x)
    print(ecode1)
    word = ''.join(ecode1) 

    print(word)
 
if direction == "encode" :
    encode(text,shift)
elif direction == "decode" :
    decode(text,shift)