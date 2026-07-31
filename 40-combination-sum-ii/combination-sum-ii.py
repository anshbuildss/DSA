class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()

        ans = []
        subset = []

        def dfs(i, total):

            if total == target:
                ans.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # Pick
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # Backtrack
            subset.pop()

            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Not Pick
            dfs(i + 1, total)

        dfs(0, 0)
        return ans