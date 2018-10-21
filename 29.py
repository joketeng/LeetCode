class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            pis = 1
        else:
            pis = 0
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        temp, i = divisor, 1
        while temp <= dividend:
            # �������ڱ������������С�뻮�ָ���
            temp <<= 1
            i <<= 1
        while dividend >= divisor:
            temp >>= 1
            i >>= 1
            # ������������ڼȶ������С���̼����ϻ��ָ���
            if temp <= dividend:
                dividend -= temp
                result += i
        if not pis:
            result = -result
        return min(min(result, 2**31 -1), max(result, -2**31))