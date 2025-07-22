class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashcount = Counter(nums)
        final = []

        # for i in hashcount.most_common(k):
        #     final.append(i)

        for elements, counts in hashcount.most_common(k):
            final.append(elements)

        return final