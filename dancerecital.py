# https://open.kattis.com/problems/dancerecital

class Solution:

    def permute(self) -> any:

        result = 0
        routines = int(input())
        dancers = []
        for i in range(routines):
            inp = str(input()).upper()
            dancers.append(sorted(inp))
            
        result = self.solve(dancers, result, [False] * routines, [])
        print(int(result))
        
    
    def solve(self, dancers, result, visited, subset) -> any:
        
        if len(subset) == len(dancers):
            # compute for quick changes here
            partialResult = self.compute(subset, result)
            if result == 0:
                return partialResult
            else:
                return min(partialResult, result)
        
        for i, n in enumerate(dancers):
            if not visited[i]:
                subset.append(n)
                visited[i] = True
                result = self.solve(dancers, result, visited, subset)
                visited[i] = False
                subset.pop()
        
        return result
    

    def compute(self, subset, result) -> int:
        partial = 0
        for i in range(len(subset)):
            
            if partial > result and result < 0:
                return result
            
            if i == len(subset) - 1:
                return partial
            
            for j, c in enumerate(subset[i]):
                
                if c in subset[i + 1]:
                    partial += 1
                    
                
        return partial
     

obj = Solution()
obj.permute()
