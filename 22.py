class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate([], n, n, result)
        return result
        
    def generate(self,partial, left , right, result):
        # ��������������Ϊ��ʱ����partialԪ�������result��
        if left == 0 and right == 0:
            result.append(''.join(partial))
        # ��ָ��������������Ϊ��ʱ��Ԫ������ӣ��������������Ǽ�һ
        if left != 0:
            self.generate(partial + ['('], left-1, right, result)
        # ����������С����������ʱ��Ԫ����ӣ�����������������һ
        if left < right:
            self.generate(partial + [')'], left, right-1, result)