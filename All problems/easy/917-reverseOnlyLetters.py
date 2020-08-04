"""
917. 仅仅反转字母
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

 

示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
 

提示：

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "

"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        n=len(S)
        ans=['']*n
        i=-1
        for j in range(n):
            if not S[j].isalpha():ans[j]=S[j]
        for k in range(n):
            if S[k].isalpha():
                while i>=-n:
                    if ans[i]=='':
                        ans[i]=S[k]
                        break
                    else:i-=1
        return ''.join(ans)