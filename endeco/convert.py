import string
def to_num(value,base):
    value=str(value)
    base=str(base).lower()
    decimal=0
    count=len(value.split('.')[0])
    if base in ('2','binary','bin'):
        for i in value.replace('.', ''):
            count-=1
            if i=='1':
                decimal=decimal+(2**count)
    elif base in ('16','hex','hexadecimal'):
        value=value.lower()
        hexmap=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        hexmap={v:k for k,v in enumerate('0123456789abcdef')}
        for i in value.replace('.',''):
            if i in hexmap.keys():
                count-=1
                decimal=decimal+hexmap[i]*(16**count)
    elif base in ('26','alphabets','alpha','Base26'):
        value=value.lower()
        alphamap=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alphamap={alphamap[i]:i for i in range(len(alphamap))}
        for i in value.replace('.',''):
            if i in alphamap.keys():
                count-=1
                decimal=decimal+alphamap[i]*(26**count)
    elif base in ('32','base32','base 32'):
        value=value.upper()
        basemap=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','2','3','4','5','6','7']
        basemap={basemap[i]:i for i in range(len(basemap))}
        for i in value.replace('.',''):
            if i in basemap.keys():
                count-=1
                decimal=decimal+basemap[i]*(32**count)
    elif base in ('64','base64', 'base 64'):
        basemap=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
        basemap={basemap[i]:i for i in range(len(basemap))}
        for i in value.replace('.',''):
            if i in basemap.keys():
                count-=1
                decimal=decimal+basemap[i]*(64**count)
    elif base in ('128','ascii', 'base 128','base128'):
        basemap={i: chr(i) for i in range(128)}
        basemap={value : key for (key, value) in basemap.items()}
        for i in value.replace('.',''):
            if i in basemap.keys():
                count-=1
                decimal=decimal+basemap[i]*(64**count)
    return decimal
def to_base(value,base):
    base=str(base).lower()
    answer=str()
    value=int(value)
    if base in ('2','binary','bin'):
        while value != 0:
            remainder=value%2
            value=value//2
            answer=str(remainder)+answer
    return answer
x=322.011
print(f'Input:  {x} ')
print(f'Decimal Value:  {to_base(x,"bin")}')

