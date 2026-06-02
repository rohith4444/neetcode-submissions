class Solution:
    def maxArea(self, heights: List[int]) -> int:
        Totalsum=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                sum=min(heights[i],heights[j])*(j-i)
                if Totalsum<sum:
                    Totalsum=sum
        return(Totalsum)