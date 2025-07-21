class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for s in strs:

            # sort = sorted(s)
            sort2 = ''.join(sorted(s))
            # print("s: ", s)
            # print("sort: ", sort)
            # print("sort2: ", sort2)
            hashmap[sort2].append(s)
            # print("full hashmap: ", hashmap)
            # print("hashmap values: ", hashmap.values())
            # print("listed hashmap values: ", list(hashmap.values()))

        return list(hashmap.values())