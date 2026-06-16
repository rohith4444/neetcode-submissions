class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: course → list of prerequisites
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        # Three states: unvisited, visiting (in current path), visited (done)
        visiting = set()
        visited = set()
        
        def dfs(course):
            if course in visiting:    # found a cycle!
                return False
            if course in visited:     # already checked, no cycle
                return True
            
            visiting.add(course)      # mark as "currently exploring"
            
            for pre in graph[course]:
                if not dfs(pre):      # if any prerequisite has cycle
                    return False
            
            visiting.remove(course)   # done exploring this path
            visited.add(course)       # mark as "fully checked"
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True