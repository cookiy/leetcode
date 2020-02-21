class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadset = set(deadends)
        if (target in deadset) or ("0000" in deadset): return -1
        que = collections.deque()
        que.append("0000")
        visited = set(["0000"])
        step = 0
        while que:
            step += 1
            size = len(que)
            for i in range(size):
                point = que.popleft()
                for j in range(4):
                    for k in range(-1, 2, 2):
                        newPoint = [i for i in point]
                        newPoint[j] = chr((ord(newPoint[j]) - ord('0') + k + 10) % 10 + ord('0'))
                        newPoint = "".join(newPoint)
                        if newPoint == target:
                            return step
                        if (newPoint in deadset) or (newPoint in visited):
                            continue
                        que.append(newPoint)
                        visited.add(newPoint)
        return -1

    #def openLock(self, deadends: List[str], target: str) -> int:
     #   if '0000' in deadends: return -1
      #  deadends, q = set(deadends), [('0000', 0)]
       # while q:
           # node, step = q.pop(0)
            #for i, add in zip([*range(4)] * 2, [1] * 4 + [-1] * 4):
                #cur = node[:i] + str((int(node[i]) + add) % 10) + node[i+1:]
                #if cur == target: return step + 1
                #if not cur in deadends:
                    #q.append((cur, step + 1))
                    #deadends.add(cur)
        #return -1