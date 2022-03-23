class Solution:
    def isValid(self, s: str) -> bool:
        lp = []
        for i in s:
            if i in ['(', '[', '{']:
                lp.append(i)
            elif len(lp) > 0:
                if lp[-1] + i == '()' or lp[-1] + i == '[]' or lp[-1] + i == '{}':
                    lp.pop(-1)
                else:
                    return False
            else:
                return False

        return True if lp == [] else False