from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        #initialize adjacency list

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for nei in adj_list[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
            
        return completed == numCourses
