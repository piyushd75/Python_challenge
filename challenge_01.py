# decode string by considering below
# k -> m
# o -> q
# e -> g

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new_string = ""

for character in string:
    #ignor space
    if character == " ":
        new_string += character
    # check whether it is character or not
    elif ord(character) >= 67 and ord(character) <= 122:
        temp_string = chr(ord(character)+2)
        # for not update y,z into special characters
        if ord(temp_string) >=122:
            temp_string = chr(ord(temp_string)-26)
        new_string += temp_string
print(new_string)
