class Solution:
    def intToRoman(self, num):
        roman = ['M', 'CM',  'D', 'CD',  'C', 'XC',  'L', 'XL',  'X', 'IX',  'V', 'IV',  'I']
        ber = ['1000', '900',  '500', '400',  '100', '90',  '50', '40',  '10', '9',  '5', '4',  '1']
        arr = ''
        while num:
            for i, c in enumerate(ber):
                if int(ber[i]) <= num:
                    num -= int(ber[i])
                    arr += roman[i]
                    break
        return arr
