class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictStr={}
        for i in strs:
            key="".join(sorted(i))

            if key not in dictStr:
                dictStr[key]=[]
            dictStr[key].append(i)
            
            lst=list(dictStr.values())
        return lst

strs = ["act","pots","tops","cat","stop","hat"]
obj=Solution()
print(obj.groupAnagrams(strs))