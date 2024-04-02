card = [4546568735994633, 5566892315260104, 373521757791003, 222]

for i in card:
    str_i = str(i)
    if str_i[0] == '4' and (len(str_i) == 13 or len(str_i) == 16):
        print(i, "is a VISA card")
    elif 51 <= int(str_i[:2]) <= 55 and len(str_i) == 16:
        print(i, "is a Mastercard")
    elif str_i[:2] in ('34', '37') and len(str_i) == 15:
        print(i, 'is an AMEX card')
    else:
        print(i, "is an invalid card")