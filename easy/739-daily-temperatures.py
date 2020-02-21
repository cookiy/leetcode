"""
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高的天数。如果之后都不会升高，请输入 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的都是 [30, 100] 范围内的整数。

线性扫描，开辟额外栈，每次扫描的新的元素 T[i] 时，

如果栈为空，就直接将元素下标 i 压到栈里，

如果栈不为空，而且栈顶 s[-1] 对应的气温 T[s[-1] ] 大于等于当前元素 T[i] ，说明气温没有回升，也把元素下标 i 压到栈里,而且栈顶 s[-1] 对应的气温 T[s[-1] ] 小于当前元素 T[i] ， 说明气温已经回升，

那么对应的天数就是 i - s[-1]， 重复上行和本行直到栈顶元素比当前元素大为止。

"""
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0] * len(T)
        s = []
        # print res
        for i in range(0, len(T)):
            while(s and T[i] > T[s[-1]]):
                res[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)            
        return res
    

