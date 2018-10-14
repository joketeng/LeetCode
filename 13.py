class Soution:
    def romanToInt(self, s):
        roman1 = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        roman2 = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
        rum1 = ['1000', '500', '100', '50', '10', '5', '1']
        rum2 = ['900', '400', '90', '40', '9', '4']
        num = 0
        while s:
            for i, c in enumerate(roman2):
                if c in s:
                    s = s.replace(c, '', 1)
                    num += int(rum2[i])
            for i, c in enumerate(roman1):
                if c in s:
                    s = s.replace(c, '', 1)
                    num += int(rum1[i])
        return num

    # 罗马数字特殊情况计算数值的应用
    def romanToInt2(self, s):
        r = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in range(len(s)-1):
            print(i)
            if r[s[i]] >= r[s[i+1]]:
                sum += r[s[i]]
            else:
                sum -= r[s[i]]
        sum += r[s[-1]]
        return sum