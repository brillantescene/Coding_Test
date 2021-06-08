import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        for word in strs:
            anagram[''.join(sorted(word))].append(word)
        return list(anagram.values())
