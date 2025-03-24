class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        else:
            strs.sort()
            beginning = strs[0]
            end = strs[-1]
            minLength = len(beginning)
            i = 0
            lcp = ""
            while i < minLength and beginning[i] == end[i]:
                lcp += beginning[i]
                i += 1
                
        return lcp
            
                
if __name__ == "__main__":
    arr = ["cats", "catch", "category", "called"]
    solved = Solution()
    print(solved.longestCommonPrefix(arr))