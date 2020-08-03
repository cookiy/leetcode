"""
面试题 16.15. 珠玑妙算
珠玑妙算游戏（the game of master mind）的玩法如下。

计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。作为用户，你试图猜出颜色组合。打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。

给定一种颜色组合solution和一个猜测guess，编写一个方法，返回猜中和伪猜中的次数answer，其中answer[0]为猜中的次数，answer[1]为伪猜中的次数。

示例：

输入： solution="RGBY",guess="GGRR"
输出： [1,1]
解释： 猜中1次，伪猜中1次。
提示：

len(solution) = len(guess) = 4
solution和guess仅包含"R","G","B","Y"这4种字符
"""

"""
建立两个字典，存放solution和guess颜色出现的个数
因为题目中说“猜中”不能算入“伪猜中”，因此“猜中”的优先级更高
先计算猜中的次数，对应的字典-1
再计算伪猜中的次数，对应的字典-1
最后返回结果即可

作者：tian-dao-yao-xing
链接：https://leetcode-cn.com/problems/master-mind-lcci/solution/shuang-100-by-tian-dao-yao-xing/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        dicts=Counter(solution)
        dictg=Counter(guess)
        answer=[0,0]
        for i in range(len(solution)):
            if solution[i]==guess[i]:
                answer[0]+=1
                dicts[solution[i]]-=1
                dictg[guess[i]]-=1
        for i in range(len(solution)):
            if guess[i] in solution and dicts[guess[i]]>0 and dictg[guess[i]]>0:
                answer[1]+=1
                dicts[guess[i]]-=1
                dictg[guess[i]]-=1
        return answer



"""
计数器算出两个颜色个数，然后取交集，即最小。得到的计数器就是颜色相等的（包含cao相等的）
最后再计算颜色+cao相等得到猜中，total-right就是伪猜中的。

作者：boille
链接：https://leetcode-cn.com/problems/master-mind-lcci/solution/6xing-pythoncounterjiao-ji-by-boille/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def masterMind(self, solution: str, guess: str):
        from collections import Counter
        total = sum((Counter(solution) & Counter(guess)).values())
        right = sum(1 for (i, j) in zip(solution, guess) if i == j)
        return [right, total - right]