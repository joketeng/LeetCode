class Solution:
    def longestCommonPrefix(self, strs):
        '''
        a = [1,2,3]
        b = [4,5,6]
        c = [4,5,6,7,8]
        zipped = zip(a,b) # ���ΪԪ����б�
        [(1, 4), (2, 5), (3, 6)]
        zip(a,c) # Ԫ�ظ�������̵��б�һ��
        [(1, 4), (2, 5), (3, 6)]
        zip(*zipped) # �� zip �෴��*zipped �����Ϊ��ѹ�����ض�ά����ʽ
        [(1, 2, 3), (4, 5, 6)]
       '''
        str = ''
        for i, c in enumerate(zip(*strs)):
            if len(set(c)) > 1:
                # set() ��������һ�������ظ�Ԫ�ؼ�
                return str
            else:
                str += c[0]
        return str