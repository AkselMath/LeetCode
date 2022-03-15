class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                result += i.lower()
        if result == result[::-1]:
            return True
        return False

a = Solution()
s = "aa"
print(a.isPalindrome(s))