class Solution:
    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:
        three_sums = set()
        
        negatives = []
        positives = []
        zero_count = 0

        #separating positives, negatives and zeros
        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zero_count += 1

        # positive and negative sets
        positives_set = set(positives)
        negatives_set = set(negatives)

        # finding inverse numbers

        if zero_count > 2:
            three_sums.add((0, 0, 0))

        # finding inverse of a sum of 2 negative numbers
        for i1, n1 in enumerate(negatives):
            
            if zero_count and -n1 in positives_set:
                three_sums.add((n1, 0, -n1))

            for n2 in negatives[i1+1:]:
                if -(n1 + n2) in positives_set:
                    print([n1,n2,-(n1+n2)])
                    three_sums.add(
                        tuple(sorted([n1,n2,-(n1+n2)]))
                    )

       # finding inverse of a sum of 2 positive numbers
        for i1, p1 in enumerate(positives):
            for p2 in positives[i1+1:]:
                if -(p1 + p2) in negatives_set:
                    three_sums.add(
                        tuple(sorted([p1,p2,-(p1+p2)]))
                    )

        return three_sums