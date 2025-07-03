# from collections import deque
# def nsrl(nums):
#         s = deque()
#         ans=[]
#         indexed_nums = list(enumerate(nums))
#         for i,n in indexed_nums[::-1]:
#             while s and s[-1][1]>=n:
#                 s.pop()
#             if s:
#                 ans.append((i,s[-1][0]))
#             else:
#                 ans.append((i,-1))
#             s.append((i,n))

#         return ans[::-1]
# def nsel(nums):
#         s= deque()
#         ans=[]
#         indexed_nums = list(enumerate(nums))
#         for i,n in indexed_nums:
#             while s and s[-1][1]>=n:
#                 s.pop()
#             if s:
#                 ans.append((i,s[-1][0]))
#             else:
#                 ans.append((i,-1))
#             s.append((i,n))
#         return ans
        

        
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
       
#         nsr = nsrl(heights)
#         nsl = nsel(heights)
#         print(nsr)
#         print(nsl)
#         ans=0
#         for i,h in enumerate(heights):
#             val = (nsr[i][1]-nsl[i][1]-1)*h
#             ans=max(ans,val)
#         return ans
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        # 1. Nearest Smaller to Left
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # 2. Nearest Smaller to Right
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # 3. Calculate max area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        
        return max_area
