# check 없는 방법
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])

        dfs(0, [])
        return result


'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        check = [0] * len(nums)
        def dfs(v):
            if v == len(nums):
                result.append([nums[i] for i in range(len(nums)) if check[i] == 1])
                return
            
            check[v] = 1
            dfs(v+1)
            check[v] = 0
            dfs(v+1)
        
                
        dfs(0)
        return result
'''
