class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        s1_count = {}
        for c in s1:
            if not s1_count.get(c):
                s1_count[c] = 0

            s1_count[c] += 1

        window_size = 0
        for r, c in enumerate(s2):            
            s1_c_count = s1_count.get(c)
            # if current character is in s1
            if s1_c_count is not None:
                # if the window does not contain all
                if s1_c_count > 0:
                    s1_count[c] -= 1
                    window_size += 1
                else:
                    while s2[r - window_size] != c:
                        s1_count[s2[r - window_size]] += 1
                        window_size -= 1
            else:
                while window_size:
                    s1_count[s2[r - window_size]] += 1
                    window_size -= 1

            if window_size == len_s1:
                return True

        return False
