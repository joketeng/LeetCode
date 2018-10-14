class Solution:
    def longestCommonPrefix(self, strs):
        '''
        a = [1,2,3]
        b = [4,5,6]
        c = [4,5,6,7,8]
        zipped = zip(a,b) # 打包为元组的列表
        [(1, 4), (2, 5), (3, 6)]
        zip(a,c) # 元素个数与最短的列表一致
        [(1, 4), (2, 5), (3, 6)]
        zip(*zipped) # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
        [(1, 2, 3), (4, 5, 6)]
       '''
        str = ''
        for i, c in enumerate(zip(*strs)):
            if len(set(c)) > 1:
                # set() 函数创建一个无序不重复元素集
                return str
            else:
                str += c[0]
        return str