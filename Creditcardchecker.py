for detail in card:
    detail_str = str(detail)
    if detail_str[0] == '4' and (len(detail_str) == 13 or len(detail_str) == 16):
        print(detail_str, 'is a Visa card')
    elif detail_str[:2] >= '51' and detail_str[:2] <= '55' and len(detail_str) == 16:
        print(detail_str, 'is a Mastercard')
    elif (detail_str[:2] == '34' or detail_str[:2] == '37') and len(detail_str) == 15:
        print(detail_str, 'is an Amex card')
    else:
        print("Invalid card number")