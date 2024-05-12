from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {}
        count_income_courses = {}
        list_course = []
        accepted_course = []
        def dfs(queue):
            if not queue:
                return
            temp = []
            while queue:
                course = queue.pop()
                accepted_course.append(course)
                if course in courses:
                    for course_n in courses[course]:
                        count_income_courses[course_n] -= 1
                        if count_income_courses[course_n] == 0:
                            temp.append(course_n)
                    del courses[course]
            dfs(temp)
        for i in range(numCourses):
            courses[i] = []
            count_income_courses[i] = 0
        for i in range(len(prerequisites)):
            if not prerequisites[i][0] in courses:
                courses[prerequisites[i][0]] = []
            courses[prerequisites[i][0]].append(prerequisites[i][1])
            if not prerequisites[i][0] in count_income_courses:
                count_income_courses[prerequisites[i][0]] = 0
            if prerequisites[i][1] in count_income_courses:
                count_income_courses[prerequisites[i][1]] += 1
            else:
                count_income_courses[prerequisites[i][1]] = 1
        for k, v in count_income_courses.items():
            if v == 0:
                list_course.append(k)
        dfs(list_course)
        accepted_course.reverse()
        if len(courses.keys()) == 0:
            return accepted_course
        else:
            return []


s = Solution()
print(s.findOrder(numCourses = 3, prerequisites = [[1,0]]))
