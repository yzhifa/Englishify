
# Define parameters
digits = '1,2,3,4,5,6,7,8,9,0'.split(',')
ones_eng ='one,two,three,four,five,six,seven,eight,nine,'.split(',')
special_tens = 'ten,eleven,twelve,thirteen,forteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
tens_eng = "twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety,".split(',')
template = "{hundred1} hundred and {tens}"

# Create dictionaries to store info - for referencing later
dict_one = {}
for i, j in zip(digits, ones_eng):
    dict_one[i] = j

dict_teens = {}
for i, j in zip(digits[1:], tens_eng):
    dict_teens[i] = j

dict_special_tens = {}
for i, j in zip(digits, special_tens):
    dict_special_tens[i] = j
dict_special_tens['10'] = 'nineteen'


# Define helper functions to call out words
def returnSpecialTens(s):
    sum = str(int(s[0]) + int(s[1]))
    return dict_special_tens[sum]

def returnDigit(s):
    return dict_one[s]

def returnTeens(s):
    return dict_teens[s]

def returnHundred(s):
    if s == "0":
        return ""
    else:
        return dict_one[s] + " hundred"

def returnWord2D(s):
    # up to 2 digits
    if s[0] == "1":
        text = returnSpecialTens(s)
    else:
        text = "{a} {b}".format(a = returnTeens(s[0]),  b = returnDigit(s[1]))
    
    return text

def returnWord3D(s):
    # up to 3 digits
    hundred = s[0]
    tens = s[1:]

    part2 = returnWord2D(tens)
    
    if tens == "00":
        and_text2 = ""
    else:
        and_text2 = "and"
    
    if len(s) == 3:
        and_text1 = ""
    else:
        and_text1 = "and"
    
    return "{and_text1} {part1} {and_text2} {part2}".format(and_text1 = and_text1, and_text2 = and_text2, part1 = returnHundred(hundred), part2 = part2)

def returnThousand(s):
    # 3 digits
    if len(s) == 3:
        part1 = returnWord3D(s)
    if len(s) == 2:
        if s[0] == "1":
            part1 = returnSpecialTens(s)
        else:
            part1 = "{a} {b}".format(a = returnTeens(s[0]),  b = returnDigit(s[1]))
    if len(s) == 1:
        part1 = returnDigit(s)

    return "{part1} thousand".format(part1 = part1)

# Define englishify() - consolidation of helper functions
def englishify(a):
    word_list = []
    a_str = str(a)
    if len(a_str) > 6:
        print("This function is not applicable.")
    if a == 0:
        return "Zero"
    if len(a_str) == 1:
        word_list.append(returnDigit(a_str))
    if len(a_str) == 2:
        word_list.append(returnWord2D(a_str))
    if len(a_str) == 3:
        word_list.append(returnWord3D(a_str))
    if len(a_str) > 3 and len(a_str) <= 6:
        grp_of_three = format(a, ',').split(',')

        for i, n in enumerate(grp_of_three):
            if i == 0:
                word_list.append(returnThousand(n))
            if i == 1:
                w3D = returnWord3D(n)
                if 'hundred' in w3D:
                    commar = ","
                else:
                    commar = ""
                word_list.append(commar)
                word_list.append(w3D)
    
    # Remove unncessary spaces
    text = [i.title() for i in "".join(word_list).split(' ') if i is not ""]
    
    return " ".join(text)


print(englishify(13140))




