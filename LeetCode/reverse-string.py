class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 둘 중 하나로 하면 됨
        # s.reverse()
        s[:] = s[::-1]
        """
        Do not return anything, modify s in-place instead.
        """
