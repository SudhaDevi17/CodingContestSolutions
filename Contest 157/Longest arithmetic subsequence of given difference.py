import collections
class Solution:
    def longestSubsequence(self, arr, D):
        count =  collections.defaultdict(int)
        for x in arr:

            prev = count[x-D] + 1
            curr = count[x]
            count[x] = max(curr, prev)

        print(max(count.values()))

s = Solution()
print(s.longestSubsequence([1,5,7,8,5,3,4,2,1], -2))

