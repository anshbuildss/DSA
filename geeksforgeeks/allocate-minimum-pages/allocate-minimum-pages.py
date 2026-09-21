class Solution:

    def findPages(self, arr, m):

        def countStudents(pages):
            students = 1
            pagesStudent = 0

            for book in arr:
                if pagesStudent + book <= pages:
                    pagesStudent += book
                else:
                    students += 1
                    pagesStudent = book

            return students

        n = len(arr)

        if m > n:
            return -1

        low = max(arr)
        high = sum(arr)

        while low <= high:

            mid = (low + high) // 2

            students = countStudents(mid)

            if students > m:
                low = mid + 1
            else:
                high = mid - 1

        return low
