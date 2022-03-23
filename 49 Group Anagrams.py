class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        lo = {}
        for i in strs:
            if lo.get(''.join(sorted(i)), -1) == -1:
                lo[''.join(sorted(i))] = [i]
            else:
                lo[''.join(sorted(i))].append(i)

        return list(lo.values())