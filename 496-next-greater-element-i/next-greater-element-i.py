from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        g= dict()
        stack = deque()
        for e in nums2[::-1]:
            if not stack:
                g[e]=-1
            else:
                top = stack[-1]
                if top>e:
                    g[e] = top
                else:
                    while not (top>e):
                        # print(top,"<",e)
                        stack.pop()
                        # print(stack)
                        if not stack:
                            top=-1
                            print(g)
                            break
                        else:
                            top = stack[-1]

                    g[e] = top
            stack.append(e)
        result = []
        for i in nums1:
            result.append(g[i])

        print(g)
        return result

