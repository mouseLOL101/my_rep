def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {1: 'I', 5: 'V', 10: 'X', 50: 'L',
                         100: 'C', 500: 'D', 1000: 'M'}

        s = list(s)
        for i in range(len(s)):
            s[i] = get_key(d, s[i])
        print(s)
        i = 0
        length = len(s)
        if length > 3:
            ans = s[length - 1]
            while i < length - 1:
                if s[i] < s[i + 1] and i != length - 2:
                    ans += s[i + 1] - s[i]
                    i += 2
                elif s[i] < s[i + 1] and i == length - 2:
                    ans -= s[i]
                    i +=1
                else:
                    ans += s[i]
                    i += 1
        elif 1 < length <= 3:
            ans = s[length - 1]
            while i < length - 1:
                if s[i] < s[i + 1]:
                    ans -= s[i]
                    i += 2
                else:
                    ans += s[i]
                    i += 1
        else:
            ans = s[0]
        return ans

#  программа вывода
s = str(input())
s = Solution().romanToInt(s)
print(s)
