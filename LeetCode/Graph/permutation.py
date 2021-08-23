'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            if index == len(nums):
                result.append(tmp[:])
                return
            for i in range(len(nums)):
                if check[i] == 0:
                    check[i] = 1
                    tmp[index] = nums[i]
                    dfs(index+1)
                    check[i] = 0
        
        check = [0] * len(nums)
        tmp = [0] * len(nums)
        result = []
        
        dfs(0)
        
        return result
'''

# itertools 사용하기


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
