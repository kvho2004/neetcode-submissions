class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lit = []

        for word in strs:
            found = False
            for group in lit:
                for i in group:
                    if sorted(i) == sorted(word):
                        group.append(word)
                        found = True
                        break;
                if (found == True):
                    break;
            if found == False:
                new = []
                new.append(word)
                lit.append(new)

        return lit