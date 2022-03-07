class Solution():
    def compress(self, chars):
        start = -1
        end = 0
        k = 0
        while start < len(chars) and end < len(chars):
            if end + 1 < len(chars) and chars[end] == chars[end + 1]:
                end += 1
            else:
                chars[k] = chars[end]
                if end - start >= 10:
                    for i in range(len(str(end - start))):
                        chars[k + i + 1] = str(end - start)[i]
                    k += len(str(end - start))+1
                elif end - start != 0 and end - start != 1:
                    chars[k + 1] = str(end - start)
                    k += 2
                else:
                    k += 1

                start = end
                end += 1

        return len(chars[:k])