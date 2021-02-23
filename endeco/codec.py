#Initializing Encode Maps and Key Mappings

hexmap=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
hexmap={hexmap[i]:i for i in range(len(hexmap))}
alphamap=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphamap={alphamap[i]:i for i in range(len(alphamap))}
base32=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','2','3','4','5','6','7']
base32={base32[i]:i for i in range(len(base32))}
base64=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
base64={base64[i]:i for i in range(len(base64))}
base128={i: chr(i) for i in range(128)}
base128={value : key for (key, value) in base128.items()}


#Function to convert base to intiger form

def to_int(value,base):                             #Value = 'Base form Input' / Base = Base Form.

    value=str(value)                                #To Allow with value as a sequence.
    base=str(base).lower()                          #Input Formatting
    output=0                                        #Initializing int output at 0
    count=len(value)                                #Counting the Length of the now string 'Value'.

#Different Base Type Detection

    if base in ('2','binary','bin'):
        for i in value:
            count-=1
            if i=='1':
                output=output+(2**count)

    elif base in ('16','hex','hexadecimal'):
        value=value.lower()
        for i in value:
            if i in hexmap.keys():
                count-=1
                output=output+hexmap[i]*(16**count)

    elif base in ('26','alphabets','alpha','Base26'):
        value=value.lower()
        for i in value:
            if i in alphamap.keys():
                count-=1
                output=output+alphamap[i]*(26**count)

    elif base in ('32','base32','base 32'):
        value=value.upper()
        for i in value:
            if i in base32.keys():
                count-=1
                output=output+base32[i]*(32**count)

    elif base in ('64','base64', 'base 64'):
        for i in value:
            if i in base64.keys():
                count-=1
                output=output+base64[i]*(64**count)

    elif base in ('128','ascii', 'base 128','base128'):
        for i in value:
            if i in base128.keys():
                count-=1
                output=output+base128[i]*(128**count)

    return output       #Function returns Intiger as output


#Function to Convert from intiger to Base Form

def to_base(value,base):                #Function Takes in intiger Value and desired base type
    value=int(value)                    #Making sure our value is dealed with as an intiger
    base=str(base).lower()              #Formatting base input
    answer=''                           #Initializing Variable to store Base Answer


#Different base Level Detection
    if base in ('2','binary','bin'):
        while value != 0:                           #Loop till value becomes 0
            remainder=value%2
            value=value//2
            answer=str(remainder)+answer

    elif base in ('16','hex','hexadecimal'):
        _reversed_hexmap = {value : key for (key, value) in hexmap.items()}  #Decode Map initilization
        while value !=0:
            remainder=value%16
            value=value//16
            hexkey=_reversed_hexmap[remainder]                       #Replacing the value with hexadecimal value
            answer=str(hexkey)+answer                                #Appending hexavalue to answer

    elif base in ('26','alpha','alphabets'):
        _reversed_alphamap = {value : key for (key, value) in alphamap.items()}
        while value !=0:
            remainder=value%26
            value=value//26
            alphakey=_reversed_alphamap[remainder]
            answer=str(alphakey)+answer

    elif base in ('32','base32','base 32'):
        _reversed_base32 = {value : key for (key, value) in base32.items()}
        while value !=0:
            remainder=value%32
            value=value//32
            base32_key=_reversed_base32[remainder]
            answer=str(base32_key)+answer

    elif base in ('64','base64','base 64'):
        _reversed_base64 = {value : key for (key, value) in base64.items()}
        while value !=0:
            remainder=value%64
            value=value//64
            base64_key=_reversed_base64[remainder]
            answer=str(base64_key)+answer

    elif base in ('128','base 128','base128','ascii'):
        _reversed_base128 = {value : key for (key, value) in base128.items()}
        while value !=0:
            remainder=value%128
            value=value//128
            base128_key=_reversed_base128[remainder]
            answer=str(base128_key)+answer
    return answer

