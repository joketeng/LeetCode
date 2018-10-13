class Solution:
    def reverse(self, x):
        sss = str(x)
        sum, index, tag = 0, 1, 1
        for x in sss:
            if x == '-':
                tag = -1
                continue
            sum += index * int(x)
            index = index * 10
        if sum * tag > (2**31)-1 or sum * tag < -2**31:
            return 0
        return sum * tag

    def reverse2(self, x):
        if x >= 0:
            tag = 1
            m = str(x)
        else:
            tag = -1
            m = str(-x)
        rever = int(m[::-1])
        if rever * tag > (2**31)-1 or rever * tag < -2**31:
            return 0
        return rever * tag