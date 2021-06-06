import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(
    '[^\w]', ' ', paragraph).lower().split() if word not in banned]

counts = collections.defaultdict(int)
for word in words:
    counts[word] += 1

print(max(counts, key=counts.get))
