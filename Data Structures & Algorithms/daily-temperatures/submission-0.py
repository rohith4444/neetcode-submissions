class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results=[]
        for i in range(len(temperatures)):
            count = 1
            found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    results.append(count)
                    found = True
                    break
                else:
                    count += 1
            if not found:
                results.append(0)
        return results