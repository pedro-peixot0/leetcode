import collections

class Solution: 
    @staticmethod
    def kSimilarity(s1: str, s2: str) -> int:
        all_permutations = collections.deque([s1])

        seen_set = set()

        permutation_count=0
        
        while all_permutations:
            # looping all current permutations of the word
            for _ in range(len(all_permutations)):
                current_perm = all_permutations.popleft()
                
                if current_perm == s2:
                    return permutation_count

                i=0 # finding first letter index that does not match with target
                while current_perm[i] == s2[i]:
                    i+=1
                
                # Looping through all letters ahead of the current letter
                # To find a letter to make the swap
                for j in range(i+1,len(current_perm)):
                    # if letter checked is the right one for the target swap
                    # if letter checked is not already in its own right position
                    if current_perm[j] == s2[i] != s2[j]:
                        #
                        new_perm = current_perm[:i] + current_perm[j] + current_perm[i+1:j] + current_perm[i] + current_perm[j+1:]

                        if new_perm not in seen_set:
                            seen_set.add(new_perm)
                            all_permutations.append(new_perm)
                
            permutation_count += 1
