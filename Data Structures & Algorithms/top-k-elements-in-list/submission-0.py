class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        for each in nums:
            if(not frequency.get(each)):
                frequency.update({each:1})
            else:
                frequency.update({each:frequency[each]+1})
        frequency_s = sorted(frequency, key=frequency.get)
        l1 = frequency_s[len(frequency_s)-k:]
        return l1
        
        