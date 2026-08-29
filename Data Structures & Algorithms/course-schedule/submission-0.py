from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            pre[prereq].append(course)
            indegree[course] += 1

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for next_course in pre[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        return completed == numCourses           
