class Solution:
    def permute(self) -> int:
        nums = str(input())
        res = 0
        # print([False] * len(nums))
        result = self.solve([False] * len(nums), "", nums, res)

        print(int(result))
    
    def solve(self, visited, partial, nums, res) -> int:
        if len(partial) == len(nums):
            numInt = int(nums)
            if int(partial) > numInt:
                if res == 0:
                    res = int(partial)
                else:
                    res = min(res, int(partial))
            
            return res
        else:
            for i, n in enumerate(nums):
                if not visited[i]:
                    partial += nums[i]
                    visited[i] = True
                    res = self.solve(visited, partial, nums, res)
                    visited[i] = False
                    partial = partial[:-1]

        return res

obj = Solution()
obj.permute()
