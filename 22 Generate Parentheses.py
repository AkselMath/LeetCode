class Solution(object):
    def generateParenthesis(self, n):
        def istr(rt):
            m = 0
            t = False
            while m < len(rt):
                if rt[m] != '(' or rt[m + 1] != ')':
                    t = True
                m += 2
            return t

        def mensg(ar, k):
            if k > 1:
                ar = mensg(ar, k-1)
            if k == 1:
                ar = ['()']
            else:
                po = []
                for i in range(len(ar)):
                    po.append('(' + ar[i] + ')')
                    po.append(ar[i] + '()')
                    if istr(ar[i]):
                        po.append('()' + ar[i])
                ar = po
            return ar

        lp = []
        lp = mensg(lp, n)

        return lp

sd = Solution()
print(sorted(sd.generateParenthesis(3)))