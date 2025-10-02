class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1= []
        dict1={}
        for i in strs:
            c = "".join(sorted(i))
            if c not in dict1:
                dict1[c]=[i]
            else:
                dict1[c].append(i)
        for i in dict1.values():
            list1.append(i)
        return list1