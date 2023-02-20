def roman_to_int(s:str)->int:
    translation = 0
    numbers = {'CM':900, 'CD':400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV':4,
                'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for a in numbers:
        translation += numbers[a] * s.count(a)
        s = s.replace(a, '')
    return translation

def int_to_roman(num:int)->str:
    translation = ''
    count = 0
    numbers = {900: 'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV',
                1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    power = len(str(num)) - 1
    for i in range(len(list(str(num)))):
        grade = 10 ** power
        count = int(list(str(num))[i]) * grade
        check = 5 * grade
        remainder = count % check
        if count != 0:
            if remainder != 0 and remainder != (4 * grade):
                if count >= check:
                    translation += numbers[check]
                    for i in range (remainder // grade):
                        translation += numbers[grade]
                else:
                    for i in range (count // grade):
                        translation += numbers[grade]
            else:
                translation += numbers[count]
        power -= 1
    return translation