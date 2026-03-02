# week01-3.py 學習計畫 Array/String P2
# leetcode 1071. Greatest Common Divisor of Strings
#最大公因數GCD 很不直覺
class Solution:
	def gcdOfStrings(self, str1: str, str2: str) -> str:
		N1, N2 = len(str1), len(str2)
		N = gcd(N1, N2)

		ans = str1[:N]
		if (ans * int(N1 / N) != str1) or (ans * int(N2 / N) != str2):
		    return ""
		return ans