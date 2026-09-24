class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for each in strs:
            dupl = "".join(sorted(each))
            if(not groups.get(dupl)):
                groups.update({dupl: [each]})
            else:
                groups[dupl].append(each)
        grouped = []
        for key in groups:
            grouped.append(groups.get(key))
        return grouped
        
        
        