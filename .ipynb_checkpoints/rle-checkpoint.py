import sys # For at kunne bruge argV og argC
from time import sleep # for at hente sleep

def RLE_D(mess):
    
    sleep(1)
    
    fail = "fail"
    
    #empty string
    if mess == '':
        return fail
    
    # if not string
    if not isinstance(mess, str):
        return fail
    
    
    #string
    count = 1
    decres = []
    
    decode = ''
    counter = ''
    count = 0
    for char in mess[0:]:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            counter += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            count = int(counter)
            decode += char * count
            decres.append(decode)
            count = 0
            counter = ''
            decode = ''
    return ''.join(decres)
    
def RLE_E(mess):
    
    sleep(1)
    
    fail = "fail"
    
    #empty string
    if mess == '':
        return fail
    
    # if not string
    if not isinstance(mess, str):
        return fail
    
    old = mess[0]
    count = 1
    encres = []
    
    for c in mess[1:]:
        if c == old:
            count += 1
        else:
            encres.append(f'{count}{old}')
            count = 1
            old = c
    encres.append(f'{count}{old}')
    return ''.join(encres)
    
if __name__ == "__main__":
    res = []
    
    if sys.argv[1] == '-e':
        res = RLE_E(sys.argv[2])
        
    if sys.argv[1] == '-d':
        res = RLE_D(sys.argv[2])
    
    print(res)